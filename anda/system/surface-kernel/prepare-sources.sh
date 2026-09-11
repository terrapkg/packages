#!/usr/bin/env bash
set -euo pipefail

# The Ultramarine fork is the controlled source for Surface patches/configs.
# This is the fork's fedora-43-6.19.8-3 release commit.
readonly linux_surface_repository="https://github.com/Ultramarine-Linux/linux-surface.git"
readonly linux_surface_commit="4cbbe2ed574d7ec3384c611fba32fad3bf7b6ee8"
readonly package_name="terra-surface"
readonly spec_name="terra-surface-kernel"

readonly workdir="$(mktemp -d)"

cleanup() {
    rm -rf "$workdir"
}
trap cleanup EXIT

git clone --depth 1 "$linux_surface_repository" "$workdir/linux-surface"
git -C "$workdir/linux-surface" fetch --depth 1 origin "$linux_surface_commit"
git -C "$workdir/linux-surface" checkout --detach "$linux_surface_commit"

# build-ark.py clones the complete kernel-ark history when --ark-dir is absent.
# Seed it with the exact annotated tag instead, then let the upstream builder
# use that checkout to generate the patched SRPM.
git clone --depth 1 --branch kernel-6.19.8-0 \
    https://gitlab.com/cki-project/kernel-ark.git "$workdir/kernel-ark"
# kernel-ark derives the Fedora version by comparing the tagged build to this
# matching upstream branch; fetch only that ref instead of all tags/history.
git -C "$workdir/kernel-ark" fetch --depth 1 origin \
    linux-6.19.y:refs/remotes/origin/linux-6.19.y

# The checkout already contains the pinned tag. Avoid build-ark.py's unbounded
# `git fetch --tags`, which would otherwise download kernel-ark's full history.
sed -i \
    -e '/system("git fetch --tags")/d' \
    -e "s/SPECPACKAGE_NAME='kernel-%s'/SPECPACKAGE_NAME='$spec_name'/" \
    "$workdir/linux-surface/pkg/fedora/kernel-surface/build-ark.py"
sed -i \
    -e "s/^PACKAGE_NAME = \"surface\"$/PACKAGE_NAME = \"$package_name\"/" \
    "$workdir/linux-surface/pkg/fedora/kernel-surface/build-linux-surface.py"

pushd "$workdir/linux-surface/pkg/fedora/kernel-surface" >/dev/null
python3 build-linux-surface.py \
    --mode srpm \
    --ark-dir "$workdir/kernel-ark" \
    --outdir "$workdir/srpm"

srpm=("$workdir"/srpm/"$spec_name"-*.src.rpm)
if [[ ${#srpm[@]} -ne 1 || ! -f ${srpm[0]} ]]; then
    echo "Expected exactly one $spec_name SRPM" >&2
    exit 1
fi

popd >/dev/null

mkdir -p "$workdir/extracted"
rpm2cpio "${srpm[0]}" | (cd "$workdir/extracted" && cpio -idm --quiet)

spec="$workdir/extracted/$spec_name.spec"
if [[ ! -f $spec ]]; then
    echo "Generated SRPM does not contain $spec_name.spec" >&2
    exit 1
fi

find . -maxdepth 1 -type f \( ! -name 'prepare-sources.sh' -a ! -name 'surface-kernel.spec' -a \( -name '*.patch' -o -name '*.config' -o -name '*.tar.*' -o -name '*.xz' \) \) -delete
rm -f surface-kernel.spec
cp -a "$workdir/extracted"/. .
mv "$spec_name.spec" surface-kernel.spec
