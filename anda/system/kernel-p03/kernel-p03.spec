# %tag pins the exact linux-p03 release this build fetches - update.rhai
# bumps it to the latest tag, and the %include below fetches from that
# same tag (not main), so this file is never the source of truth for
# anything except "which tag", and builds stay reproducible against a
# fixed ref instead of whatever's currently on the moving main branch.
%global tag 7.2.0-52.rc6.p03.13
%include %(f=$(mktemp); curl -fsSL https://raw.githubusercontent.com/CatPieLeaf/linux-p03/%{tag}/sources/kernel-p03/kernel-p03.spec -o "$f"; echo "$f")
