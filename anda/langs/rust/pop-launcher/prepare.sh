#!/bin/bash
set -x
spectool -g pop-launcher.spec || true

FOLDER="$PWD"

# Extract the tarball to /tmp/src/
mkdir -p /tmp/src
tar -xzf ./1.*.tar.gz -C /tmp/src

pushd /tmp/src/* || exit

just vendor

mv -v ./vendor.tar "$FOLDER"/vendor.tar


# tarball the .cargo folder

tar -czf "$FOLDER"/cargo-config.tar.gz .cargo


popd || exit

rm -rf /tmp/src
set +x