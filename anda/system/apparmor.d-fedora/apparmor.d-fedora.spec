# %tag pins the exact apparmor.d-fedora release this build fetches -
# update.rhai bumps it to the latest tag, and the %include below fetches
# from that same tag (not main), so this file is never the source of
# truth for anything except "which tag", and builds stay reproducible
# against a fixed ref instead of whatever's currently on the moving
# main branch.
%global tag v0.4910.0-3
%include %(f=$(mktemp); curl -fsSL https://raw.githubusercontent.com/CatPieLeaf/apparmor.d-fedora/%{tag}/dists/apparmor.d-fedora.spec -o "$f"; echo "$f")
