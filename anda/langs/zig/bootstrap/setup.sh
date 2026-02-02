#!/usr/bin/bash

version=0.16.0-dev.2459+37d14a4f3

mirrors=()

for m in $(curl -s https://ziglang.org/download/community-mirrors.txt); do
  mirrors+=($m)
done


# Self explanatory
function randomize_mirrors() {
  number=${#mirrors[@]}
  index=$(( RANDOM % number ))
  mirror=${mirrors[$index]}
}

if [ "$1" == "fetch" ]; then
   until curl -If ${mirror}/zig-${version}.tar.xz &>/dev/null && curl -If ${mirror}/zig-${version}.tar.xz.minisig &>/dev/null; do
     randomize_mirrors
   done
   echo -e "\033[0;32mNote:\033[0m Selected mirror $mirror"
   curl -A "rpmdev-spectool" -H "Accept-Encoding: identity" -O ${mirror}/zig-${version}.tar.xz?source=terra.fyralabs.com
   curl -A "rpmdev-spectool" -H "Accept-Encoding: identity" -O ${mirror}/zig-${version}.tar.xz.minisig?source=terra.fyralabs.com
elif [ "$1" == "version" ]; then
   echo $version
# Grab a random mirror. For debugging purposes.
elif [ "$1" == "mirror" ]; then
   randomize_mirrors
   echo "Your random mirror is $mirror"
elif [ "$1" == "mirrors" ]; then
   echo "$mirrors"
fi

exit 0
