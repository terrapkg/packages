#!/usr/bin/bash

## Some sources need to be fetched BEFORE the build process
# Also I'm just better at scripting in Bash and calling the Rhai sh function hundreds of times times sounded like hell
# Have I mentioned I hate runtime languages?

node=backport
# Enable logs for debugging
set -x
# I guess just $PWD doesn't work for this
builddir=$(pwd)/anda/devs/$node

# We only need the tests folder so sourcing the whole repo is overkill, Git can make a tarball of specific directories

pushd $builddir
ver=$(cat ./*.spec | grep -P -m1 'Version:' | sed -e 's/Version://g' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
url=$(sed -n 's/^URL:\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' -e "s/%{module}/$node/")
dir=$node

git clone --recurse-submodules -j$(nproc) $url.git

pushd $dir
# I'm not sure why .tar.bz2 is the tar format of choice for this but it's also what Fedora does so it's what I'm doing
git archive --format=tar --prefix=tests/ v${ver}:src/test/ | bzip2 > ../tests-${ver}.tar.bz2
popd
rm -rf $dir

exit 0
