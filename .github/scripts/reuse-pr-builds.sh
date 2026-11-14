#!/bin/bash
# Reuse packages already built for a merged pull request instead of rebuilding them.
#
# On a push, finds the PR that was merged into this commit and the autobuild run
# for its head commit. If that run is still going, it is cancelled and everything
# is rebuilt. Otherwise, for PRs from branches in this repository (not forks),
# each matrix entry whose artifact fingerprint (see build-fingerprint.sh) matches
# this commit gets a `prebuilt` field pointing at that artifact, and
# json-build.yml publishes it instead of building again.
#
# Reads the matrix from $BUILD_MATRIX and writes build_matrix to $GITHUB_OUTPUT.
set -euo pipefail

matrix=$BUILD_MATRIX
repo=$GITHUB_REPOSITORY

finish() {
	echo "build_matrix=$(jq -c . <<<"$matrix")" >>"$GITHUB_OUTPUT"
	exit 0
}

pr=$(gh api "repos/$repo/commits/$GITHUB_SHA/pulls" --jq "
	[.[] | select(.merged_at and .merge_commit_sha == \"$GITHUB_SHA\" and .base.ref == \"$GITHUB_REF_NAME\")][0] // empty")
if [ -z "$pr" ]; then
	echo "No merged pull request for this commit, building everything."
	finish
fi
pr_number=$(jq -r .number <<<"$pr")
head_sha=$(jq -r .head.sha <<<"$pr")
echo "Commit was merged from #$pr_number (head $head_sha)."

runs=$(gh api "repos/$repo/actions/workflows/autobuild.yml/runs?event=pull_request&head_sha=$head_sha&per_page=100" \
	--jq .workflow_runs)

running=$(jq -r '.[] | select(.status != "completed") | "\(.id) \(.html_url)"' <<<"$runs")
if [ -n "$running" ]; then
	while read -r id url; do
		echo "::notice::Cancelling unfinished PR build $url, packages will be rebuilt."
		gh api -X POST "repos/$repo/actions/runs/$id/cancel" >/dev/null
	done <<<"$running"
	finish
fi

# Only trust packages built from branches in this repository, not forks.
if [ "$(jq -r '.head.repo.full_name // ""' <<<"$pr")" != "$repo" ]; then
	echo "#$pr_number is from a fork, building everything."
	finish
fi

# Runs are returned newest first.
run_id=$(jq -r '.[0].id // empty' <<<"$runs")
if [ -z "$run_id" ]; then
	echo "No autobuild runs found for #$pr_number, building everything."
	finish
fi
run_url=$(jq -r '.[0].html_url' <<<"$runs")

artifacts=$(gh api --paginate "repos/$repo/actions/runs/$run_id/artifacts?per_page=100" \
	--jq '.artifacts[] | select(.expired | not) | .name')

for i in $(jq -r 'keys[]' <<<"$matrix"); do
	pkg=$(jq -r ".[$i].pkg" <<<"$matrix")
	arch=$(jq -r ".[$i].arch" <<<"$matrix")
	fp=$(./.github/scripts/build-fingerprint.sh "$pkg")
	prefix="${pkg//\//@}-$arch-"
	artifact=$(jq -Rr --arg p "$prefix" --arg s "+$fp" \
		'select(startswith($p) and endswith($s))' <<<"$artifacts" | head -n1)
	if [ -z "$artifact" ]; then
		echo "$pkg ($arch): no matching build in $run_url"
		continue
	fi
	echo "::notice::$pkg ($arch): reusing $artifact from $run_url"
	matrix=$(jq --argjson i "$i" --argjson run "$run_id" --arg art "$artifact" \
		'.[$i].prebuilt = {run_id: $run, artifact: $art}' <<<"$matrix")
done

finish
