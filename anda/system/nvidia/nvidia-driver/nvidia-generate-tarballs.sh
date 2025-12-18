#!/bin/bash
set -e

set_vars() {
   export VERSION=${VERSION:-590.48.01}
   export TEMP_UNPACK=${ARCH}
   export PLATFORM=Linux-${ARCH}
   export RUN_FILE=NVIDIA-${PLATFORM}-${VERSION}.run
}

run_file_get() {
    printf "Downloading installer ${RUN_FILE}... "
    if [[ ! -f $RUN_FILE ]]; then
        # This is getting ridiculous:
        if wget -q -S --spider https://download.nvidia.com/XFree86/${PLATFORM}/${VERSION}/$RUN_FILE; then
            wget -q https://download.nvidia.com/XFree86/${PLATFORM}/${VERSION}/$RUN_FILE
        elif wget -q -S --spider https://us.download.nvidia.com/XFree86/${PLATFORM}/${VERSION}/$RUN_FILE; then
            wget -q https://us.download.nvidia.com/XFree86/${PLATFORM}/${VERSION}/$RUN_FILE
        else
            wget -q https://us.download.nvidia.com/tesla/${VERSION}/$RUN_FILE
        fi
    fi
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
    #   - GLVND test scripts
    #   - Closed source modules
    #   - Open source modules with precompiled c++ code
    rm -r \
        nvidia-xconfig* \
        nvidia-persistenced* \
        nvidia-modprobe* \
        libnvidia-gtk*.so* nvidia-settings* \
        libGLESv1_CM.so.* libGLESv2.so.* libGLdispatch.so.* libOpenGL.so.* libGLX.so.* libGL.so.1* libEGL.so.1* \
        libnvidia-egl-wayland.so.* libnvidia-egl-gbm.so.* libnvidia-egl-xcb.so.* libnvidia-egl-xlib.so.* \
        libnvidia-egl-wayland2.so.* \
        libOpenCL.so.1* \
        libEGL.so.${VERSION} \
        nvidia-installer* .manifest make* mk* libglvnd_install_checker \
        15_nvidia_gbm.json 10_nvidia_wayland.json 20_nvidia_xcb.json 20_nvidia_xlib.json \
        99_nvidia_wayland2.json \
        kernel kernel-open

    if [ "${ARCH}" == x86_64 ]; then
        rm -r \
          libnvidia-wayland-client.so* \
          32/libGLESv1_CM.so.* 32/libGLESv2.so.* 32/libGLdispatch.so.* 32/libOpenGL.so.* 32/libGLX.so.* 32/libGL.so.1* 32/libEGL.so.1* \
          32/libOpenCL.so.1* \
          32/libnvidia-egl-wayland.so.* 32/libnvidia-egl-gbm.so.* 32/libnvidia-egl-xcb.so.* 32/libnvidia-egl-xlib.so.* \
          32/libnvidia-egl-wayland2.so.* \
          32/libglvnd_install_checker

        cp -f *.json* 32/
    fi

    cd ..

    printf "OK\n"
}

create_tarball() {
    KMOD_COMMON=nvidia-kmod-common-${VERSION}
    USR_64=nvidia-driver-${VERSION}-${ARCH}
    USR_32=nvidia-driver-${VERSION}-i386

    rm -rf ${KMOD_COMMON} ${USR_64} ${USR_32}
    mkdir ${KMOD_COMMON} ${USR_64}
    mv ${TEMP_UNPACK}/firmware ${TEMP_UNPACK}/nvidia-bug-report.sh ${KMOD_COMMON}/

    if [ "$ARCH" == x86_64 ]; then
        mkdir ${USR_32} 
        mv ${TEMP_UNPACK}/32/* ${USR_32}/
        rm -fr ${TEMP_UNPACK}/32
    else
        USR_32=
    fi

    mv ${TEMP_UNPACK}/* ${USR_64}/
    rm -fr ${TEMP_UNPACK}

    for tarball in ${KMOD_COMMON} ${USR_64} ${USR_32}; do
        printf "Creating tarball $tarball... "
        XZ_OPT='-T0' tar --remove-files -cJf $tarball.tar.xz $tarball
        printf "OK\n"
    done
}

ARCHES=${ARCHES:-"x86_64 aarch64"}

for ARCH in $ARCHES; do
    set_vars
    run_file_get
    run_file_extract
    cleanup_folder
    create_tarball
done
