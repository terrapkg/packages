#!/usr/bin/env bash
set -euo pipefail

# The Ultramarine fork is the controlled source for Surface patches/configs.
# This is the fork's fedora-43-6.19.8-3 release commit.
readonly linux_surface_repository="https://github.com/Ultramarine-Linux/linux-surface.git"
readonly linux_surface_commit="4cbbe2ed574d7ec3384c611fba32fad3bf7b6ee8"
readonly spec_name="kernel-surface"

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
# build-ark.py applies the Surface patches with git am, which creates commits.
# The ephemeral CI checkout has no configured author identity.
git -C "$workdir/kernel-ark" config user.name "Terra Build System"
git -C "$workdir/kernel-ark" config user.email "builds@terrapkg.com"

# The checkout already contains the pinned tag. Avoid build-ark.py's unbounded
# `git fetch --tags`, which would otherwise download kernel-ark's full history.
# Patch the helper with Python rather than shell-quoting a multi-line sed
# insertion. The injected code runs after build-ark.py resets kernel-ark.
python3 - "$workdir/linux-surface/pkg/fedora/kernel-surface/build-ark.py" <<'PY'
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = text.replace('system("git fetch --tags")\n', '')
needle = 'system("git reset --hard \'%s\'" % args.package_tag)\n'
injected = needle + '''
# Terra builds only x86_64.
for priority in ("fedora", "rhel"):
    priority_path = "redhat/configs/priority." + priority
    lines = Path(priority_path).read_text().splitlines(keepends=True)
    Path(priority_path).write_text("".join(
        line for line in lines
        if re.match(r"^(#|$|EMPTY|ORDER|x86_64)", line)
    ))
Path("redhat/Makefile").write_text(
    re.sub(r"^ARCH_LIST=.*$", "ARCH_LIST=x86_64", Path("redhat/Makefile").read_text(), flags=re.MULTILINE)
)
'''
if needle not in text:
    raise SystemExit("kernel-ark reset line not found")
path.write_text(text.replace(needle, injected, 1))
PY

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
