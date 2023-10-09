#!/bin/sh

set -x

: "${DELETE_SOURCES:=1}"

pwd

export ANDA_BUILD_DIR="$PWD/../../../anda-build/rpm"

# Set the kernel-ark release build rev number
export KERNEL_ARK_REV='500'

# Set the Fyra kernel overlay version
export FYRA_KERNELOVERLAY_VER=$(cat version.txt)

if [ "$DELETE_SOURCES" = "1" ]; then
    rm -rf source patches
fi

# Fetch the patches
git clone https://github.com/FyraLabs/linux-kernel-patches.git patches

# Move into the patches' directory
pushd patches

# Acquire the latest supported kernel-ark branch
export BRANCH="$(cat current/commit)"

echo branch: $BRANCH

# Move out from the patches' directory
popd

# Fetch the source
git clone https://gitlab.com/cki-project/kernel-ark.git source

# Move into the source directory
pushd source
git checkout $BRANCH

# Set proper user name for commits
git config user.name 'Terra' ; git config user.email 'mail@example.com'

# Apply all patches
for patch in ../patches/current/patches/*.patch
    do git am $patch
done

# Build the SRPM
make \
    IS_FEDORA=1 \
    BUILD=${KERNEL_ARK_REV} \
    SPECPACKAGE_NAME='kernel-fyra' \
    DISTLOCALVERSION=".fyra${FYRA_KERNELOVERLAY_VER}" \
    dist-srpm -j$(nproc)


# find srpm in source/redhat/rpm/SRPMS

find redhat/rpm -type f

sudo dnf builddep -y redhat/rpm/SPECS/kernel-fyra.spec
sudo dnf in -y bison flex

mkdir -p $ANDA_BUILD_DIR/rpms
mkdir -p $ANDA_BUILD_DIR/srpms

# Build the resulting SRPM
rpmbuild -rb \
    --without=debug \
    --without=configchecks \
    redhat/rpm/SRPMS/kernel-fyra-*.src.rpm || exit 1

# Move the resulting RPM files into the target directory
for file in redhat/rpm/RPMS/*.rpm
    do mv -v $file $ANDA_BUILD_DIR/rpms/
done

# Also move the SRPM package file
for file in redhat/rpm/SRPMS/*.src.rpm
    do mv -v $file $ANDA_BUILD_DIR/srpms/
done

# We're done here
# exit 0
