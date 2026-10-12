#!/usr/bin/env bash
# Turn selected NVIDIA groups into complete anda build matrices.
# PACKAGES is the JSON selection passed to nvidia-build.yml.
set -euo pipefail

fail() {
  echo "::error::$1" >&2
  exit 1
}

if [[ -n "${CUSTOM_BUILDER:-}" ]]; then
  fail "Full driver groups require architecture-specific runners; custom_builder is not supported"
fi

if ! jq -e 'type == "array" and all(.[]; (.pkg | type == "string") and ((.pkg | startswith("anda/system/nvidia/")) or (.pkg | startswith("anda/system/nvidia-580/"))))' <<< "${PACKAGES:-}" >/dev/null; then
  fail "Use the ordinary build workflow for packages outside the NVIDIA driver folders"
fi

selected_groups=()
for group in nvidia nvidia-580; do
  if jq -e --arg prefix "anda/system/$group/" 'any(.[]; .pkg | startswith($prefix))' <<< "$PACKAGES" >/dev/null; then
    selected_groups+=("$group")
  fi
done

group_json=$(jq -cn --args '$ARGS.positional' --args "${selected_groups[@]}")
blocked_groups='[]'

# `anda ci` knows each project's configured labels and architectures. Touch its
# marker just as the manual build workflow does, then ask anda for the matrix.
all_projects=$(anda list)
while IFS= read -r selected_pkg; do
  [[ -z "$selected_pkg" ]] && continue
  grep -Fq -- "$selected_pkg (" <<< "$all_projects" || fail "Unknown driver project: $selected_pkg"
done < <(jq -r '.[].pkg' <<< "$PACKAGES")

for group in "${selected_groups[@]}"; do
  mapfile -t project_dirs < <(
    printf '%s\n' "$all_projects" |
      sed -n "s@^\\(anda/system/${group}/[^ ]*/pkg\\) .*@\\1@p" |
      sed 's@/pkg$@@'
  )
  ((${#project_dirs[@]} > 0)) || fail "No projects found for $group"
  for project_dir in "${project_dirs[@]}"; do
    [[ -f "$project_dir/anda.hcl" ]] || fail "Missing project manifest: $project_dir/anda.hcl"
    touch "$project_dir/.build"
  done

done

if ((${#selected_groups[@]} > 0)); then
  git config user.name "github-actions[bot]"
  git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
  git add --all
  if ! git diff --cached --quiet; then
    git commit -m "ci: select complete NVIDIA driver groups"
  fi

  raw_matrix=$(anda ci | sed -E 's/^build_matrix=//')
  jq -e 'type == "array"' <<< "$raw_matrix" >/dev/null || fail "anda ci did not return a build matrix"
  packages=$(jq -c --argjson groups "$group_json" '[.[] | select(.pkg as $pkg | any($groups[]; . as $group | $pkg | startswith("anda/system/" + $group + "/")))]' <<< "$raw_matrix")
  jq -e 'length <= 256' <<< "$packages" >/dev/null || fail "Expanded build matrix exceeds GitHub's 256-job limit"

  # Only publish a driver group when every RPM in that group has one matching
  # source version. The container toolkit has an independent release cycle.
  for group in "${selected_groups[@]}"; do
    folder="anda/system/$group"
    if command -v fd >/dev/null; then
      mapfile -d '' -t specs < <(fd --type f --extension spec --print0 . "$folder")
    else
      mapfile -d '' -t specs < <(find "$folder" -type f -name '*.spec' -print0)
    fi
    versions=()
    for spec in "${specs[@]}"; do
      [[ "$spec" == "$folder/nvidia-container-toolkit/"* ]] && continue
      version=$(rpmspec -q --srpm --qf '%{VERSION}\n' "$spec" 2>/dev/null) || {
        versions=()
        break
      }
      [[ -n "$version" && "$version" != *$'\n'* ]] || {
        versions=()
        break
      }
      versions+=("$version")
    done
    if ((${#versions[@]} == 0)); then
      blocked_groups=$(jq -c --arg group "$group" '. + [$group]' <<< "$blocked_groups")
      echo "::warning::Not publishing $group: no readable driver versions found"
      continue
    fi
    mapfile -t unique_versions < <(printf '%s\n' "${versions[@]}" | sort -u)
    if ((${#unique_versions[@]} != 1)); then
      blocked_groups=$(jq -c --arg group "$group" '. + [$group]' <<< "$blocked_groups")
      echo "::warning::Not publishing $group: driver specs have mismatched versions"
    fi
  done
else
  packages='[]'
fi

[[ -n "${GITHUB_OUTPUT:-}" ]] || fail "GITHUB_OUTPUT is not set"
printf 'packages=%s\n' "$packages" >> "$GITHUB_OUTPUT"
printf 'blocked_groups=%s\n' "$blocked_groups" >> "$GITHUB_OUTPUT"
