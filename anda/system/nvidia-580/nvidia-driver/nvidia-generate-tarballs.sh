#!/bin/sh
# Slightly modified from negativo's tarball generator script

# instead of generating tarballs, we just make this script export
# the functions

CONTEXT=$(realpath $(dirname $0))
set -e

set_vars() {
   export VERSION=${VERSION:?"VERSION not set"}
   export DL_SITE=${DL_SITE:-http://download.nvidia.com/XFree86}
   export TEMP_UNPACK=${ARCH}
   export PLATFORM=Linux-${ARCH}
   export RUN_FILE=NVIDIA-${PLATFORM}-${VERSION}.run
}

run_file_get() {
    printf "Downloading installer ${RUN_FILE}... "
    [[ -f $RUN_FILE ]] || wget -c -q ${DL_SITE}/${PLATFORM}/${VERSION}/$RUN_FILE
    printf "OK\n"
}

run_file_extract() {
    rm -fr ${TEMP_UNPACK}
    sh ${RUN_FILE} --extract-only --target ${TEMP_UNPACK}
}

cleanup_folder() {

    printf "Cleaning up binaries... "

    cd ${TEMP_UNPACK}

    # Stuff not needed for packages:
    #   - Compiled from source
    #   - Interactive installer files
    #   - GLVND GL libraries
    #   - Internal development only libraries
    rm -fr \
        nvidia-xconfig* \
        nvidia-persistenced* \
        nvidia-modprobe* \
        libnvidia-gtk* libnvidia-wayland-client* nvidia-settings* \
        libGLESv1_CM.so.* libGLESv2.so.* libGLdispatch.so.* libOpenGL.so.* libGLX.so.* libGL.so.1* libEGL.so.1* \
        libnvidia-egl-wayland.so.* libnvidia-egl-gbm.so.* libnvidia-egl-xcb.so.* libnvidia-egl-xlib.so.* \
        libOpenCL.so.1* \
        libEGL.so.${VERSION} \
        nvidia-installer* .manifest make* mk* tls_test* libglvnd_install_checker

    if [ "${ARCH}" == x86_64 ]; then
        rm -fr \
          32/libGLESv1_CM.so.* 32/libGLESv2.so.* 32/libGLdispatch.so.* 32/libOpenGL.so.* 32/libGLX.so.* 32/libGL.so.1* 32/libEGL.so.1* \
          32/libOpenCL.so.1* \
          32/libGL.so.${VERSION} 32/libEGL.so.${VERSION} \
          32/libnvidia-egl-wayland.so.* 32/libnvidia-egl-gbm.so.* 32/libnvidia-egl-xcb.so.* 32/libnvidia-egl-xlib.so.*

        cp -f *.json* 32/
    fi

    cd ..

    printf "OK\n"
}

create_tarball() {

    KMOD=nvidia-kmod-${VERSION}-${ARCH}
    KMOD_COMMON=nvidia-kmod-common-${VERSION}
    USR_64=nvidia-driver-${VERSION}-${ARCH}

    mkdir ${KMOD} ${KMOD_COMMON} ${USR_64}
    mv ${TEMP_UNPACK}/kernel* ${KMOD}/
    mv ${TEMP_UNPACK}/firmware ${KMOD_COMMON}/

    if [ "$ARCH" == x86_64 ]; then

        USR_32=nvidia-driver-${VERSION}-i386

        mkdir ${USR_32} 
        mv ${TEMP_UNPACK}/32/* ${USR_32}/
        rm -fr ${TEMP_UNPACK}/32

    fi

    mv ${TEMP_UNPACK}/* ${USR_64}/

    rm -fr ${TEMP_UNPACK}

    for tarball in ${KMOD} ${KMOD_COMMON} ${USR_64} ${USR_32}; do

        printf "Creating tarball $tarball... "

        # XZ_OPT='-T0' tar --remove-files -cJf $tarball.tar.xz $tarball

        printf "OK\n"

    done
}

# pushd $CONTEXT

# ARCH=aarch64
# set_vars
# run_file_get
# run_file_extract
# cleanup_folder
# create_tarball

# ARCH=x86_64
# set_vars
# run_file_get
# run_file_extract
# cleanup_folder
# create_tarball

# popd