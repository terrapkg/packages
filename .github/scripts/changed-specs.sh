#!/usr/bin/env bash
# Write the .spec files a workflow run should process to "$1", NUL separated.
#
#   pull_request      the specs the pull request adds, modifies, or renames
#                     (BASE_REF is the branch it targets)
#   workflow_dispatch $PATHS pathspecs when given, otherwise the specs of the
#                     last commit on the checked out branch
#   push              the specs touched by the pushed commits (BEFORE), falling
#                     back to the last commit
#
# Entries are NUL separated and limited to added/copied/modified/renamed files.
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <output file>" >&2
  exit 2
fi

out=$1
: > "$out"

base=
case "${GITHUB_EVENT_NAME:-}" in
  pull_request)
    : "${BASE_REF:?BASE_REF is required for pull_request runs}"
    # a pull request checkout carries the merge commit, not the base branch,
    # so the base ref is fetched once when it is not there yet
    if ! git rev-parse --verify --quiet "origin/${BASE_REF}^{commit}" > /dev/null; then
      git fetch --no-tags --quiet origin "$BASE_REF"
    fi
    base=$(git merge-base HEAD "origin/$BASE_REF")
    ;;
  workflow_dispatch)
    if [ -n "${PATHS:-}" ]; then
      # PATHS carries one or more pathspecs, so the word splitting is wanted.
      # shellcheck disable=SC2086
      while IFS= read -r -d '' file; do
        case "$file" in
          *.spec) printf '%s\0' "$file" >> "$out" ;;
        esac
      done < <(git ls-files -z -- $PATHS)
      if [ ! -s "$out" ]; then
        echo "no .spec file matched: $PATHS" >&2
      fi
      exit 0
    fi
    base=HEAD^
    ;;
  push)
    base=${BEFORE:-}
    if [ -z "$base" ] || ! git rev-parse --verify --quiet "${base}^{commit}" > /dev/null; then
      base=HEAD^
    fi
    ;;
  *)
    base=HEAD^
    ;;
esac

if ! git rev-parse --verify --quiet "${base}^{commit}" > /dev/null; then
  echo "no earlier commit to compare against, nothing to do" >&2
  exit 0
fi

git diff --name-only -z --diff-filter=ACMR "$base" HEAD -- '*.spec' > "$out"
