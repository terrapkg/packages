#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

for tool in git make gcc bison flex python3 curl rpm2cpio rpmspec cpio xz tar; do
    if ! command -v "$tool" >/dev/null; then
        echo "Missing source preparation tool: $tool (run ci_setup.rhai first)" >&2
        exit 1
    fi
done

# The Ultramarine fork is the controlled source for Surface patches/configs.
# This is the fork's fedora-43-6.19.8-3 release commit.
readonly linux_surface_repository="https://github.com/Ultramarine-Linux/linux-surface.git"
readonly linux_surface_commit="4cbbe2ed574d7ec3384c611fba32fad3bf7b6ee8"
readonly spec_name="kernel-surface"
readonly kernel_version="6.19.8"
readonly rust_target_patch="https://github.com/torvalds/linux/commit/905b06d32a52afe32fcf5f30cf298c9ea6359f11.patch"

readonly workdir="$(mktemp -d)"

cleanup() {
    local status=$?
    if [[ ${KERNEL_SURFACE_KEEP_WORKDIR:-0} == 1 ]]; then
        echo "Source preparation work directory: $workdir" >&2
    else
        rm -rf "$workdir"
    fi
    exit "$status"
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
# Fedora's SRPM tarball is exported from MARKER=v<version>. Fetch that exact
# upstream tag, not the moving stable branch. Point the branch used by genspec
# at the same commit so source generation cannot pick up newer stable releases.
git -C "$workdir/kernel-ark" fetch --depth 1 origin \
    "refs/tags/v$kernel_version:refs/tags/v$kernel_version"
git -C "$workdir/kernel-ark" update-ref refs/remotes/origin/linux-6.19.y \
    "v$kernel_version^{}"

# Snapshot version detection requires merge-base/history unavailable in a
# shallow checkout. This is an exact release, so use its Makefile version.
export VERSION_ON_UPSTREAM=0

# build-linux-surface.py picks up kernel patches in filename order. Include
# the upstream Rust 1.98 ABI fix in its normal git-am/source-patch generation.
curl --fail --location --retry 3 "$rust_target_patch" \
    --output "$workdir/linux-surface/patches/6.19/0025-rust-1.98-target-spec.patch"
# build-ark.py applies the Surface patches with git am, which creates commits.
# The ephemeral CI checkout has no configured author identity.
git -C "$workdir/kernel-ark" config user.name "Terra Build System"
git -C "$workdir/kernel-ark" config user.email "builds@terrapkg.com"

# The checkout already contains the pinned tag. Avoid build-ark.py's unbounded
# `git fetch --tags`, which would otherwise download kernel-ark's full history.
sed -i '/system("git fetch --tags")/d' \
    "$workdir/linux-surface/pkg/fedora/kernel-surface/build-ark.py"

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

# Validate the generated spec before replacing the bootstrap and sources.
rpmspec --parse "$spec" >/dev/null

find . -maxdepth 1 -type f \( ! -name 'prepare-sources.sh' -a ! -name 'kernel-surface.spec' -a \( -name '*.patch' -o -name '*.config' -o -name '*.tar.*' -o -name '*.xz' \) \) -delete
rm -f kernel-surface.spec
cp -a "$workdir/extracted"/. .
