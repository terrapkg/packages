# %tag below is only a cache-buster for Andaman's diff-based updater -
# the actual build content is fetched fresh from
# https://github.com/CatPieLeaf/linux-p03/blob/main/sources/kernel-p03/kernel-p03-gcc.spec
# at parse time, so this file is never the source of truth for anything
# except "did the tag change".
%global tag 7.1.5-201.p03.10
%include %(f=$(mktemp); curl -fsSL https://raw.githubusercontent.com/CatPieLeaf/linux-p03/main/sources/kernel-p03/kernel-p03-gcc.spec -o "$f"; echo "$f")
