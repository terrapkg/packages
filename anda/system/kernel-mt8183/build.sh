#!/bin/sh

set -eux -o pipefail

: "${DELETE_SOURCES:=1}"

pwd

export ANDA_BUILD_DIR="$PWD/../../../anda-build/rpm"

# Set the kernel-ark release build rev number
export KERNEL_ARK_REV='500'

# Set the Fyra kernel overlay version
export FYRA_KERNELOVERLAY_VER=$(cat version.txt)

if [ "$DELETE_SOURCES" = "1" ]; then
    rm -rf source
fi

# Acquire the latest supported kernel-ark branch
# Normally, this would be configured from the downstream repo, see kernel-fyra, but this is a temporary package anyways
export BRANCH="fedora-6.6"

echo branch: $BRANCH

# Fetch the source
git clone -b $BRANCH https://gitlab.com/cki-project/kernel-ark.git source

# Move into the source directory
pushd source
git checkout $BRANCH

# Set proper user name for commits
git config user.name 'Terra' ; git config user.email 'mail@example.com'

# Apply patches from elly's tree
curl https://raw.githubusercontent.com/ellyq/board-google-kukui/main/linux/patches/mt8183-6.7-rc6.patch | git apply

# Copy the kernel config
cp ../config .config

# Install dependencies
sudo dnf in -y make gcc bison flex

# Build the SRPM
make \
    IS_FEDORA=1 \
    BUILD=${KERNEL_ARK_REV} \
    SPECPACKAGE_NAME='kernel-mt8183' \
    DISTLOCALVERSION=".fyra${FYRA_KERNELOVERLAY_VER}" \
    dist-srpm -j$(nproc)


# find srpm in source/redhat/rpm/SRPMS

find redhat/rpm -type f

sudo dnf builddep -y redhat/rpm/SPECS/kernel-mt8183.spec

mkdir -p $ANDA_BUILD_DIR/rpms
mkdir -p $ANDA_BUILD_DIR/srpms

# Build the resulting SRPM
rpmbuild -rb \
    --without=debug \
    --without=configchecks \
    redhat/rpm/SRPMS/kernel-mt8183-*.src.rpm || exit 1

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
