#!/bin/bash

version=0.15.0-dev.1232+869ef0060
mirrorlist="https://pkg.machengine.org/zig https://zigmirror.hryx.net/zig https://zig.linus.dev/zig https://zig.squirl.dev https://zig.florent.dev https://zig.mirror.mschae23.de/zig https://zigmirror.meox.dev https://ziglang.freetls.fastly.net https://zig.tilok.dev https://zig-mirror.tsimnet.eu/zig https://zig.karearl.com/zig https://pkg.earth/zig https://fs.liujiacai.net/zigbuilds"
mirrors=()

for mirror in $mirrorlist; do
  mirrors+=($mirror)
done


# Self explanatory
function randomize_mirrors() {
  number=${#mirrors[@]}
  index=$(( RANDOM % number ))
  mirror=${mirrors[$index]}
}

if [ "$1" == "fetch" ]; then
   until curl -If $mirror/zig-${version}.tar.xz &>/dev/null && curl -If $mirror/zig-${version}.tar.xz.minisig &>/dev/null; do
     randomize_mirrors
   done
   curl -A "rpmdev-spectool" -H "Accept-Encoding: identity" -O $mirror/zig-${version}.tar.xz
   curl -A "rpmdev-spectool" -H "Accept-Encoding: identity" -O $mirror/zig-${version}.tar.xz.minisig
elif [ "$1" == "version" ]; then
   echo $version
# Grab a random mirror. For debugging purposes.
elif [ "$1" == "mirror" ]; then
   randomize_mirrors
   echo "Your random mirror is $mirror"
elif [ "$1" == "mirrorlist" ]; then
   echo "$mirrorlist"
fi

exit 0
