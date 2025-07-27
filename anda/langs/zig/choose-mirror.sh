#!/bin/bash

version=0.15.0-dev.1232+869ef0060

# Self explanatory
function randomize_mirrors() {
  mirrors=("https://pkg.machengine.org/zig" "https://zigmirror.hryx.net/zig" "https://zig.linus.dev/zig" "https://zig.squirl.dev" "https://zig.florent.dev")
  number=${#mirrors[@]}
  index=$(( RANDOM % number ))
  mirror=${mirrors[$index]}
}

# ONLY export mirrors to the update scripts if they connect on both files
until curl -If $mirror/zig-${version}.tar.xz &>/dev/null && curl -If $mirror/zig-${version}.tar.xz.minisig &>/dev/null; do
  randomize_mirrors
done

echo $mirror

exit 0
