#!/usr/bin/env bash
# Publish only complete driver groups from the downloaded build artifacts.
# Inputs: PACKAGES, BLOCKED_GROUPS, SUBATOMIC_TOKEN, and VERSION.
set -euo pipefail
printf '%s\n' "$PACKAGES" > packages.json
mkdir -p nvidia-upload/rpms nvidia-upload/srpms

for group in nvidia nvidia-580; do
  if jq -e --arg group "$group" 'index($group) != null' <<< "$BLOCKED_GROUPS" > /dev/null; then
    echo "Not publishing $group: driver specs have mismatched or unreadable versions" >&2
    continue
  fi
  if [[ "$group" == "nvidia" ]]; then
    folder="anda/system/nvidia/"
  else
    folder="anda/system/nvidia-580/"
  fi
  mapfile -t builds < <(jq -r --arg folder "$folder" '[.[] | select(.pkg | startswith($folder)) | [.pkg, .arch, (.labels.no_upload_srpms // 0 | tostring)]] | unique[] | @tsv' packages.json)
  ((${#builds[@]} > 0)) || continue

  complete=true
  for build in "${builds[@]}"; do
    IFS=$'\t' read -r pkg arch no_upload_srpms <<< "$build"
    artifact_pkg=${pkg//\//@}
    artifact="driver-${group}-${artifact_pkg}-${arch}-${VERSION}"
    if [[ ! -f "artifacts/ready-${artifact}/nvidia-build-success" || ! -d "artifacts/${artifact}" ]]; then
      echo "Not publishing $group: $pkg ($arch) did not complete successfully" >&2
      complete=false
      break
    fi
    if ! find "artifacts/${artifact}/rpms" -maxdepth 1 -type f -name '*.rpm' -print -quit | grep -q .; then
      echo "Not publishing $group: no RPMs found for $pkg ($arch)" >&2
      complete=false
      break
    fi
    if [[ "$no_upload_srpms" != "1" ]] && ! find "artifacts/${artifact}/srpm" -maxdepth 1 -type f -name '*.rpm' -print -quit | grep -q .; then
      echo "Not publishing $group: no source RPM found for $pkg ($arch)" >&2
      complete=false
      break
    fi
  done
  [[ "$complete" == "true" ]] || continue

  echo "All packages in $group built successfully; including them in the repository upload."
  for build in "${builds[@]}"; do
    IFS=$'\t' read -r pkg arch no_upload_srpms <<< "$build"
    artifact_pkg=${pkg//\//@}
    artifact="artifacts/driver-${group}-${artifact_pkg}-${arch}-${VERSION}"
    find "$artifact/rpms" -maxdepth 1 -type f -name '*.rpm' -exec cp -n {} nvidia-upload/rpms/ \;
    if [[ "$no_upload_srpms" != "1" ]]; then
      find "$artifact/srpm" -maxdepth 1 -type f -name '*.rpm' -exec cp -n {} nvidia-upload/srpms/ \;
    fi
  done
done

shopt -s nullglob
rpms=(nvidia-upload/rpms/*.rpm)
srpms=(nvidia-upload/srpms/*.rpm)
if ((${#rpms[@]} == 0)); then
  echo "No NVIDIA RPMs were collected for upload" >&2
  exit 1
fi

subatomic-cli upload --prune \
  --server https://subatomic.fyralabs.com \
  --token "$SUBATOMIC_TOKEN" \
  "terra${VERSION}-nvidia" "${rpms[@]}"

if ((${#srpms[@]} > 0)); then
  subatomic-cli upload --prune \
    --server https://subatomic.fyralabs.com \
    --token "$SUBATOMIC_TOKEN" \
    "terra${VERSION}-nvidia-source" "${srpms[@]}"
fi
