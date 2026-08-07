# %tag below is only a cache-buster for Andaman's diff-based updater -
# the actual build content is fetched fresh from
# https://github.com/CatPieLeaf/apparmor.d-fedora/blob/main/dists/apparmor.d-fedora.spec
# at parse time, so this file is never the source of truth for anything
# except "did the tag change".
%global tag v0.4910.0-3
%include %(f=$(mktemp); curl -fsSL https://raw.githubusercontent.com/CatPieLeaf/apparmor.d-fedora/main/dists/apparmor.d-fedora.spec -o "$f"; echo "$f")
