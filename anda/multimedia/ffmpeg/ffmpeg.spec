%global _lto_cflags %{nil}

%global avcodec_soversion 61
%global avdevice_soversion 61
%global avfilter_soversion 10
%global avformat_soversion 61
%global avutil_soversion 59
%global postproc_soversion 58
%global swresample_soversion 5
%global swscale_soversion 8

Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg
Version:        7.1.1
Release:        3%?dist
License:        LGPL-3.0-or-later
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://%{name}.org/releases/%{name}-%{version}.tar.xz

# https://github.com/OpenVisualCloud/SVT-VP9/tree/master/ffmpeg_plugin
Patch0:         %{name}-svt-vp9.patch
# https://github.com/HandBrake/HandBrake/tree/e117cfe7fca37abeec59ea4201e5d93ed7477746
Patch2:         %{name}-HandBrake.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2240127
# Reference: https://crbug.com/1306560
Patch3:         %{name}-chromium.patch
# Fix build with recent NVCC:
Patch4:         %{name}-nvcc.patch

BuildRequires:  AMF-devel >= 1.4.28
BuildRequires:  bzip2-devel
BuildRequires:  codec2-devel
BuildRequires:  doxygen
BuildRequires:  frei0r-devel
BuildRequires:  gmp-devel
BuildRequires:  gsm-devel
BuildRequires:  ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  ladspa-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libklvanc-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libxavs-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nasm
BuildRequires:  ocl-icd-devel
BuildRequires:  openal-soft-devel
BuildRequires:  opencore-amr-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  snappy-devel
BuildRequires:  soxr-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  xvidcore-devel
BuildRequires:  xz-devel

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom) >= 1.0.0
BuildRequires:  pkgconfig(aribb24) >= 1.0.3
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dav1d) >= 0.5.0
BuildRequires:  pkgconfig(davs2) >= 1.6.0
BuildRequires:  pkgconfig(dvdnav) >= 6.1.1
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kvazaar) >= 0.8.1
BuildRequires:  pkgconfig(lc3) >= 1.1.0
BuildRequires:  pkgconfig(lcms2) >= 2.13
BuildRequires:  pkgconfig(lcevc_dec) >= 2.0.0
BuildRequires:  pkgconfig(libaribcaption) >= 1.1.1
BuildRequires:  pkgconfig(libass) >= 0.11.0
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
#BuildRequires:  pkgconfig(lensfun) > 0.3.95
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmysofa)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libplacebo) >= 4.192.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libqrencode)
#BuildRequires:  pkgconfig(libquirc)
BuildRequires:  pkgconfig(librabbitmq) >= 0.7.1
BuildRequires:  pkgconfig(librist) >= 0.2.7
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libvvenc) >= 1.11.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
#BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rav1e) >= 0.4.0
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(shaderc) >= 2019.1
#BuildRequires:  pkgconfig(shine)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(uavs3d) >= 1.1.41
BuildRequires:  pkgconfig(vapoursynth-script) >= 42
BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(vulkan) >= 1.3.277
BuildRequires:  pkgconfig(xavs2) >= 1.3.0
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x264)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zimg) >= 2.7.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28

%ifarch x86_64 aarch64
# Nvidia CUVID support and Performance Primitives based code
BuildRequires:  cuda-cudart-devel
BuildRequires:  cuda-nvcc
BuildRequires:  libnpp-devel
BuildRequires:  pkgconfig(ffnvcodec) >= 12.0.16.0
%endif

%ifarch x86_64
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libvmaf) >= 2.0.0
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.9.0
BuildRequires:  pkgconfig(SvtVp9Enc)
BuildRequires:  pkgconfig(vpl) >= 2.6
#BuildRequires:  pkgconfig(xevd) >= 0.4.1
#BuildRequires:  pkgconfig(xeve) >= 0.4.3
%endif

Obsoletes:      %{name}-free < %{epoch}:%{version}-%{release}
Provides:       %{name}-free = %{epoch}:%{version}-%{release}

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Metapackage for %{name} libraries
Requires:       libavcodec%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavdevice%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavfilter%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavformat%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libpostproc%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswresample%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswscale%{?_isa} = %{epoch}:%{version}-%{release}

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This metapackage pulls in all the %{name} libraries.

%package        devel
Summary:        Metapackage for %{name} development files
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video broadcasting
solution for Linux/Unix. It also includes a digital VCR. It can encode in real
time in many formats. This package contains development files for %{name}.

%package     -n libavcodec
Summary:        FFmpeg codec library
Obsoletes:      libavcodec-free < %{epoch}:%{version}-%{release}
Provides:       libavcodec-free = %{epoch}:%{version}-%{release}

%description -n libavcodec
The libavcodec library provides a generic encoding/decoding framework and
contains multiple decoders and encoders for audio, video and subtitle streams,
and several bitstream filters.

%package     -n libavcodec-devel
Summary:        Development files for FFmpeg's codec library
Requires:       libavcodec%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libavcodec-free-devel < %{epoch}:%{version}-%{release}
Provides:       libavcodec-free-devel = %{epoch}:%{version}-%{release}

%description -n libavcodec-devel
The libavcodec library provides a generic encoding/decoding framework and
contains multiple decoders and encoders for audio, video and subtitle streams,
and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%package     -n libavdevice
Summary:        FFMpeg devices muxing/demuxing library
Obsoletes:      libavdevice-free < %{epoch}:%{version}-%{release}
Provides:       libavdevice-free = %{epoch}:%{version}-%{release}

%description -n libavdevice
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package     -n libavdevice-devel
Summary:        Development files for FFMpeg devices muxing/demuxing library
Requires:       libavcodec-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavdevice%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavfilter-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavformat-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libavdevice-free-devel < %{epoch}:%{version}-%{release}
Provides:       libavdevice-free-devel = %{epoch}:%{version}-%{release}

%description -n libavdevice-devel
This subpackage contains the headers for FFmpeg libavdevice.

%package     -n libavfilter
Summary:        FFmpeg audio and video filtering library
Requires:       libavcodec%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavformat%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libpostproc%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswresample%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswscale%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libavfilter-free < %{epoch}:%{version}-%{release}
Provides:       libavfilter-free = %{epoch}:%{version}-%{release}

%description -n libavfilter
The libavfilter library provides a generic audio/video filtering framework
containing several filters, sources and sinks.

%package     -n libavfilter-devel
Summary:        Development files for FFmpeg's audio/video filter library
Requires:       libavcodec-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavfilter%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavformat-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libpostproc-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswresample-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswscale-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libavfilter-free-devel < %{epoch}:%{version}-%{release}
Provides:       libavfilter-free-devel = %{epoch}:%{version}-%{release}

%description -n libavfilter-devel
This subpackage contains the headers for FFmpeg libavfilter.

%package     -n libavformat
Summary:        FFmpeg's stream format library
Obsoletes:      libavformat-free < %{epoch}:%{version}-%{release}
Provides:       libavformat-free = %{epoch}:%{version}-%{release}

%description -n libavformat
The libavformat library provides a generic framework for multiplexing and
demultiplexing (muxing and demuxing) audio, video and subtitle streams.
It encompasses multiple muxers and demuxers for multimedia container formats.

%package     -n libavformat-devel
Summary:        Development files for FFmpeg's stream format library
Requires:       libavcodec-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavformat%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswresample-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libavformat-free-devel < %{epoch}:%{version}-%{release}
Provides:       libavformat-free-devel = %{epoch}:%{version}-%{release}

%description -n libavformat-devel
This subpackage contains the headers for FFmpeg libavformat.

%package     -n libavutil
Summary:        FFmpeg's utility library
Obsoletes:      libavutil-free < %{epoch}:%{version}-%{release}
Provides:       libavutil-free = %{epoch}:%{version}-%{release}

%description -n libavutil
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%package     -n libavutil-devel
Summary:        Development files for FFmpeg's utility library
Requires:       libavutil%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libavutil-free-devel < %{epoch}:%{version}-%{release}
Provides:       libavutil-free-devel = %{epoch}:%{version}-%{release}

%description -n libavutil-devel
This subpackage contains the headers for FFmpeg libavutil.

%package     -n libpostproc
Summary:        FFmpeg post-processing library
Obsoletes:      libpostproc-free < %{epoch}:%{version}-%{release}
Provides:       libpostproc-free = %{epoch}:%{version}-%{release}

%description -n libpostproc
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package     -n libpostproc-devel
Summary:        Development files for the FFmpeg post-processing library
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libpostproc%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Obsoletes:      libpostproc-free-devel < %{epoch}:%{version}-%{release}
Provides:       libpostproc-free-devel = %{epoch}:%{version}-%{release}

%description -n libpostproc-devel
This subpackage contains the headers for FFmpeg libpostproc.

%package     -n libswresample
Summary:        FFmpeg software resampling library
Requires:       libavutil%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libavresemple < %{epoch}:%{version}-%{release}
Provides:       libavresemple = %{epoch}:%{version}-%{release}
Obsoletes:      libswresample-free < %{epoch}:%{version}-%{release}
Provides:       libswresample-free = %{epoch}:%{version}-%{release}

%description -n libswresample
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package     -n libswresample-devel
Summary:        Development files for the FFmpeg software resampling library
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswresample%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libavresemple-devel < %{epoch}:%{version}-%{release}
Provides:       libavresemple-devel = %{epoch}:%{version}-%{release}
Obsoletes:      libswresample-free-devel < %{epoch}:%{version}-%{release}
Provides:       libswresample-free-devel = %{epoch}:%{version}-%{release}

%description -n libswresample-devel
This subpackage contains the headers for FFmpeg libswresample.

%package     -n libswscale
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Obsoletes:      libswscale-free < %{epoch}:%{version}-%{release}
Provides:       libswscale-free = %{epoch}:%{version}-%{release}

%description -n libswscale
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package     -n libswscale-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Requires:       libavutil-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libswscale%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libswscale-free-devel < %{epoch}:%{version}-%{release}
Provides:       libswscale-free-devel = %{epoch}:%{version}-%{release}

%description -n libswscale-devel
This subpackage contains the headers for FFmpeg libswscale.

%prep
%autosetup -p1

# Uncomment to enable debugging while configuring
#sed -i -e 's|#!/bin/sh|#!/bin/sh -x|g' configure

%build
# Work around a new GCC15 change until FFmpeg updates for it
%if 0%{?fedora} >= 42
%if "%{version}" <= "7.1.1"
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
%endif
%endif
%set_build_flags

./configure \
    --arch=%{_target_cpu} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --disable-static \
    --disable-stripping \
    --enable-amf \
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-alsa \
    --enable-bzlib \
    --enable-chromaprint \
    --enable-frei0r \
    --enable-gcrypt \
    --enable-gmp \
    --enable-gpl \
    --enable-gray \
    --enable-iconv \
    --enable-ladspa \
    --enable-lcms2 \
    --enable-libass \
    --enable-libaom \
    --enable-libaribb24 \
    --enable-libaribcaption \
    --enable-libass \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libcaca \
    --enable-libcdio \
    --enable-libcodec2 \
    --enable-libdav1d \
    --enable-libdavs2 \
    --enable-libdc1394 \
    --enable-libdrm \
    --enable-libdvdnav \
    --enable-libdvdread \
    --enable-libfdk-aac \
    --enable-libfontconfig \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgme \
    --enable-libgsm \
    --enable-libharfbuzz \
    --enable-libiec61883 \
    --enable-libilbc \
    --enable-libjack \
    --enable-libjxl \
    --enable-libklvanc \
    --enable-libkvazaar \
    --enable-liblc3 \
    --disable-liblensfun \
    --enable-liblcevc-dec \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libmysofa \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --disable-libopencv \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopenmpt \
    --enable-libopus \
    --enable-libplacebo \
    --enable-libpulse \
    --enable-libqrencode \
    --disable-libquirc \
    --enable-librabbitmq \
    --enable-librav1e \
    --enable-librist \
    --enable-librsvg \
    --enable-librtmp \
    --enable-librubberband \
    --enable-libshaderc \
    --disable-libshine \
    --enable-libsmbclient \
    --enable-libsnappy \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libsrt \
    --enable-libssh \
    --disable-libtensorflow \
    --enable-libtesseract \
    --enable-libtheora \
    --disable-libtorch \
    --enable-libtwolame \
    --enable-libuavs3d \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libvvenc \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxavs2 \
    --enable-libxavs \
    --enable-libxcb \
    --enable-libxcb-shape \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxml2 \
    --enable-libxvid \
    --enable-libzimg \
    --enable-libzmq \
    --enable-libzvbi \
    --enable-lv2 \
    --enable-lzma \
    --enable-nonfree \
    --enable-manpages \
    --enable-openal \
    --enable-opencl \
    --enable-opengl \
    --enable-openssl \
    --enable-postproc \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --enable-v4l2-m2m \
    --enable-vaapi \
    --enable-vapoursynth \
    --enable-version3 \
    --enable-vdpau \
    --enable-vulkan \
    --enable-xlib \
    --enable-zlib \
    --extra-ldflags="%{build_ldflags}" \
    --incdir=%{_includedir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --optflags="%{build_cflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%ifarch x86_64 aarch64
    --enable-cuda-nvcc \
    --enable-cuvid \
    --enable-ffnvcodec \
    --enable-libnpp \
    --enable-nvdec \
    --enable-nvenc \
    --extra-cflags="-I%{_includedir}/cuda" \
%endif
%ifarch x86_64
    --enable-libsvtav1 \
    --enable-libsvtvp9 \
    --enable-libvmaf \
    --enable-libvpl \
#    --enable-libxevd \
#    --enable-libxeve \
%endif

%make_build V=1
make documentation V=1
make alltools V=1

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
rm -fr %{buildroot}%{_datadir}/examples
mkdir doc/html
mv doc/*.html doc/html

%files
%{_bindir}/%{name}
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
%{_datadir}/%{name}

%files libs
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES

%files devel
%doc doc/APIchanges doc/*.txt
%doc doc/html doc/examples

%files -n libavcodec
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavcodec.so.%{avcodec_soversion}*

%files -n libavcodec-devel
%{_includedir}/libavcodec
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/libavcodec.so
%{_mandir}/man3/libavcodec.3*

%files -n libavdevice
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavdevice.so.%{avdevice_soversion}*

%files -n libavdevice-devel
%{_includedir}/libavdevice
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/libavdevice.so
%{_mandir}/man3/libavdevice.3*

%files -n libavfilter
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavfilter.so.%{avfilter_soversion}*

%files -n libavfilter-devel
%{_includedir}/libavfilter
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/libavfilter.so
%{_mandir}/man3/libavfilter.3*

%files -n libavformat
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavformat.so.%{avformat_soversion}*

%files -n libavformat-devel
%{_includedir}/libavformat
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/libavformat.so
%{_mandir}/man3/libavformat.3*

%files -n libavutil
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavutil.so.%{avutil_soversion}*

%files -n libavutil-devel
%{_includedir}/libavutil
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/libavutil.so
%{_mandir}/man3/libavutil.3*

%files -n libpostproc
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libpostproc.so.%{postproc_soversion}*

%files -n libpostproc-devel
%{_includedir}/libpostproc
%{_libdir}/pkgconfig/libpostproc.pc
%{_libdir}/libpostproc.so

%files -n libswresample
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libswresample.so.%{swresample_soversion}*

%files -n libswresample-devel
%{_includedir}/libswresample
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/libswresample.so
%{_mandir}/man3/libswresample.3*

%files -n libswscale
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libswscale.so.%{swscale_soversion}*

%files -n libswscale-devel
%{_includedir}/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%{_libdir}/libswscale.so
%{_mandir}/man3/libswscale.3*

%changelog
%autochangelog
