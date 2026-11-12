#!/usr/bin/env bash
set -euo pipefail

mapfile -t packages < <(jq -c '.[]' <<<"$PACKAGES_JSON")
if ((${#packages[@]} == 0)); then
  echo "No packages to publish."
  exit 0
fi

fail() {
  echo "$*" >&2
  exit 1
}

list_files() { find "$1" -maxdepth 1 -type f 2>/dev/null | sort; }

load_package() {
  IFS=$'\x1f' read -r pkg arch subrepo skip_srpm < <(
    jq -r '[.pkg, .arch, .labels.subrepo // "", .labels.no_upload_srpms // ""] | join("\u001f")' <<<"$1"
  )
  local name="$UNIT_ID-$pkg-$arch-$BUILD_VERSION"
  dir="artifacts/${name//\//@}"
  target="terra$BUILD_VERSION${subrepo:+-$subrepo}"
}

rpm_targets=() rpm_dirs=() src_targets=() src_dirs=()
declare -A has_source=()

for package in "${packages[@]}"; do
  load_package "$package"

  [[ -n $(list_files "$dir/rpms") ]] || fail "No RPM artifact found for $pkg ($arch); publishing aborted."
  rpm_targets+=("$target")
  rpm_dirs+=("$dir/rpms")

  [[ -z ${has_source[$pkg]:-} && $skip_srpm != 1 ]] || continue
  [[ -n $(list_files "$dir/srpm") ]] || fail "No source RPM artifact found for $pkg ($arch); publishing aborted."
  src_targets+=("$target-source")
  src_dirs+=("$dir/srpm")
  has_source[$pkg]=1
done

targets=("${rpm_targets[@]}" "${src_targets[@]}")
dirs=("${rpm_dirs[@]}" "${src_dirs[@]}")
for i in "${!targets[@]}"; do
  mapfile -t files < <(list_files "${dirs[i]}")
  subatomic-cli upload --prune \
    --server https://subatomic.fyralabs.com \
    --token "$SUBATOMIC_TOKEN" \
    "${targets[i]}" "${files[@]}"
done
