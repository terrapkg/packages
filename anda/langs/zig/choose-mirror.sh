#!/bin/bash

version=0.15.0-dev.1232+869ef0060

# Self explanatory
function randomize_mirrors() {
  ## Benched mirrors (will be added back if issues with them are resolved):
  # "https://zig.squirl.dev"
  mirrors=("https://pkg.machengine.org/zig" "https://zigmirror.hryx.net/zig" "https://zig.linus.dev/zig" "https://zig.florent.dev")
  number=${#mirrors[@]}
  index=$(( RANDOM % number ))
  mirror=${mirrors[$index]}
}

# ONLY export mirrors to the update scripts if they connect on both files
until curl -If $mirror/zig-${version}.tar.xz &>/dev/null && curl -If $mirror/zig-${version}.tar.xz.minisig &>/dev/null; do
  echo "404"
  randomize_mirrors
done

echo $mirror

exit 0
