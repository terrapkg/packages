# ref: https://github.com/rpmfusion/ffmpeg/blob/master/ffmpeg.spec
# TODO: add make test to %%check section

#global branch  oldabi-
#global date    20230221
#global commit  691d01989936d4b0681aa226aea8a19f06c04cea
#global rel %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} >= 37 || 0%{?rhel} >= 9
%bcond_without libavcodec_freeworld
%else
%bcond_with libavcodec_freeworld
%endif

%undefine _package_note_file

%ifarch %{ix86}
# Fails due to asm issue
%global _lto_cflags %{nil}
%endif

# Cuda and others are only available on some arches
%global cuda_arches x86_64

# Disable because of gcc issue
%global _without_lensfun  1
%ifnarch i686
%global _with_bs2b        1
%global _with_chromaprint 1
%global _with_ilbc        1
%global _with_openh264    1
%if 0%{?fedora}
%global _with_placebo     1
%endif
%global _with_rav1e       1
%global _with_rubberband  1
%global _with_smb         1
%global _with_snappy      1
%global _with_svtav1      1
%global _with_tesseract   1
%global _with_twolame     1
%global _with_wavpack     1
%global _with_webp        1
%global _with_zmq         1
%else
%global _without_vulkan   1
%endif
%ifarch x86_64
%global _with_vpl         1
%global _with_vapoursynth 1
%global _with_vmaf        1
%endif

# flavor nonfree
%if 0%{?_with_cuda:1}
%global debug_package %{nil}
%global flavor           -cuda
%global progs_suffix     -cuda
#global build_suffix     -lgpl
%ifarch %{cuda_arches}
%global _with_cuvid      1
%global _with_libnpp     1
%endif
%global _with_fdk_aac    1
%global _without_cdio    1
%global _without_frei0r  1
%global _without_gpl     1
%global _without_vidstab 1
%global _without_x264    1
%global _without_x265    1
%global _without_xvid    1
%undefine _with_smb
%endif

# Disable nvenc when not relevant
%ifnarch %{cuda_arches} aarch64
%global _without_nvenc    1
%endif

# extras flags
%if 0%{!?_cuda_version:1}
%global _cuda_version 11.2
%endif
%global _cuda_version_rpm %(echo %{_cuda_version} | sed -e 's/\\./-/')
%global _cuda_bindir %{_cuda_prefix}/bin
%if 0%{?_with_cuda:1}
%global cuda_cflags $(pkg-config --cflags cuda-%{_cuda_version})
%global cuda_ldflags $(pkg-config --libs cuda-%{_cuda_version})
%endif

%if 0%{?_with_libnpp:1}
%global libnpp_cflags $(pkg-config --cflags nppi-%{_cuda_version} nppc-%{_cuda_version})
%global libnpp_ldlags $(pkg-config --libs-only-L nppi-%{_cuda_version} nppc-%{_cuda_version})
%endif

%if 0%{?_with_rpi:1}
%global _with_omx        1
%global _with_omx_rpi    1
%global _with_mmal       1
ExclusiveArch: armv7hnl
%endif

%if 0%{?_without_gpl}
%global lesser L
%endif

%if 0%{!?_without_amr} || 0%{?_with_gmp} || 0%{?_with_smb} || 0%{?_with_vmaf}
%global ffmpeg_license %{?lesser}GPLv3+
%else
%global ffmpeg_license %{?lesser}GPLv2+
%endif

Summary:        Digital VCR and streaming server
Name:           ffmpeg%{?flavor}
Version:        6.0
Release:        18%{?date:.%{?date}%{?date:git}%{?rel}}%{?dist}
License:        %{ffmpeg_license}
URL:            https://ffmpeg.org/
%if 0%{?date}
Source0:        ffmpeg-%{?branch}%{date}.tar.bz2
%else
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz.asc
Source2:        https://ffmpeg.org/ffmpeg-devel.asc
%endif
Patch0:         0001-avfilter-vf_libplacebo-wrap-deprecated-opts-in-FF_AP.patch
Patch1:         0001-avfilter-vf_libplacebo-remove-deprecated-field.patch
Patch2:         0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
# Backport fix for segfault when passing non-existent filter option
# See: https://bugzilla.rpmfusion.org/show_bug.cgi?id=6773
Patch3:         0001-fftools-ffmpeg_filter-initialize-the-o-to-silence-th.patch
Conflicts:      %{name}-free
Provides:       %{name}-bin = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?_with_cuda:BuildRequires: cuda-minimal-build-%{_cuda_version_rpm} cuda-drivers-devel}
%{?_with_cuda:%{?!_with_cuda_nvcc:BuildRequires: clang}}
%{?_with_libnpp:BuildRequires: pkgconfig(nppc-%{_cuda_version})}
BuildRequires:  alsa-lib-devel
BuildRequires:  AMF-devel
BuildRequires:  bzip2-devel
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
%{?_with_flite:BuildRequires: flite-devel}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
%{?_with_gme:BuildRequires: game-music-emu-devel}
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
%{?_with_ilbc:BuildRequires: ilbc-devel}
BuildRequires:  lame-devel >= 3.98.3
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_jxl:BuildRequires: libjxl-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
%{!?_without_aom:BuildRequires:  libaom-devel}
%{!?_without_dav1d:BuildRequires:  libdav1d-devel}
%{!?_without_ass:BuildRequires:  libass-devel}
%{!?_without_bluray:BuildRequires:  libbluray-devel}
%{?_with_bs2b:BuildRequires: libbs2b-devel}
%{?_with_caca:BuildRequires: libcaca-devel}
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
%{?_with_chromaprint:BuildRequires: libchromaprint-devel}
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
%{!?_without_lensfun:BuildRequires: lensfun-devel}
%if 0%{?_with_ieee1394}
BuildRequires:  libavc1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libiec61883-devel
%endif
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libGL-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmysofa-devel
%{?_with_openh264:BuildRequires: openh264-devel}
BuildRequires:  libopenmpt-devel
%{?_with_placebo:BuildRequires: libplacebo-devel >= 4.192.0}
BuildRequires:  librsvg2-devel
# Disable rtmp because of rfbz: 6441 & 2399
%{?_with_rtmp:BuildRequires: librtmp-devel}
%{?_with_smb:BuildRequires: libsmbclient-devel}
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
%{?!_without_vaapi:BuildRequires: libva-devel >= 0.31.0}
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?_with_vapoursynth:BuildRequires: vapoursynth-devel}
%{?!_without_vpx:BuildRequires: libvpx-devel >= 1.4.0}
%{?_with_mfx:BuildRequires: pkgconfig(libmfx) >= 1.23-1}
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_netcdf:BuildRequires: netcdf-devel}
%{?_with_rpi:BuildRequires: raspberrypi-vc-devel}
%{!?_without_nvenc:BuildRequires: nv-codec-headers}
%{!?_without_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{?_with_omx:BuildRequires: libomxil-bellagio-devel}
BuildRequires:  libxcb-devel
BuildRequires:  libxml2-devel
%{!?_without_lv2:BuildRequires:  lilv-devel lv2-devel}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%if 0%{!?_without_opencl:1}
BuildRequires:  opencl-headers ocl-icd-devel
%{?fedora:Recommends: opencl-icd}
%endif
%{?_with_opencv:BuildRequires: opencv-devel}
BuildRequires:  openjpeg2-devel
%{!?_without_opus:BuildRequires: opus-devel >= 1.1.3}
%{!?_without_pulse:BuildRequires: pulseaudio-libs-devel}
BuildRequires:  perl(Pod::Man)
%{?_with_rav1e:BuildRequires: pkgconfig(rav1e)}
%{?_with_rubberband:BuildRequires: rubberband-devel}
%{!?_without_tools:BuildRequires: SDL2-devel}
%{?_with_snappy:BuildRequires: snappy-devel}
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  pkgconfig(srt)
%{?_with_svtav1:BuildRequires: svt-av1-devel >= 0.9.0}
%{?_with_tesseract:BuildRequires: tesseract-devel}
#BuildRequires:  texi2html
BuildRequires:  texinfo
%{?_with_twolame:BuildRequires: twolame-devel}
%{?_with_vmaf:BuildRequires: libvmaf-devel >= 1.5.2}
%{?_with_vpl:BuildRequires: pkgconfig(vpl) >= 2.6}
%{?_with_wavpack:BuildRequires: wavpack-devel}
%{!?_without_vidstab:BuildRequires:  vid.stab-devel}
%{!?_without_vulkan:BuildRequires:  vulkan-loader-devel pkgconfig(shaderc)}
%{!?_without_x264:BuildRequires: x264-devel >= 0.0.0-0.31}
%{!?_without_x265:BuildRequires: x265-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_zimg:BuildRequires:  zimg-devel >= 2.7.0}
BuildRequires:  zlib-devel
%{?_with_zmq:BuildRequires: zeromq-devel}
%{!?_without_zvbi:BuildRequires: zvbi-devel}

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}
Conflicts:      libavcodec-free
Conflicts:      libavfilter-free
Conflicts:      libavformat-free
Conflicts:      libavutil-free
Conflicts:      libpostproc-free
Conflicts:      libswresample-free
Conflicts:      libswscale-free
%{?_with_vmaf:Recommends:     vmaf-models}

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}

%package     -n libavdevice%{?flavor}
Summary:        Special devices muxing/demuxing library
Conflicts:      libavdevice-free
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description -n libavdevice%{?flavor}
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package        devel
Summary:        Development package for %{name}
Conflicts:      %{name}-free-devel
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       libavdevice%{?flavor}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

%if %{with libavcodec_freeworld}
%package -n     libavcodec-freeworld
Summary:        Freeworld libavcodec to complement the distro counterparts
# Supplements doesn't work well yet - we can rely on comps for now
#Supplements:    libavcodec-free >= %%{version}

%description -n libavcodec-freeworld
Freeworld libavcodec to complement the distro counterparts
%endif


# Don't use the %%configure macro as this is not an autotool script
%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --docdir=%{_docdir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="%{optflags}" \\\
    --extra-ldflags="%{?__global_ldflags} %{?cuda_ldflags} %{?libnpp_ldlags}" \\\
    --extra-cflags="%{?cuda_cflags} %{?libnpp_cflags} -I%{_includedir}/rav1e" \\\
    %{?flavor:--disable-manpages} \\\
    %{?progs_suffix:--progs-suffix=%{progs_suffix}} \\\
    %{?build_suffix:--build-suffix=%{build_suffix}} \\\
    %{!?_without_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    %{?_with_chromaprint:--enable-chromaprint} \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    --enable-fontconfig \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gcrypt \\\
    %{?_with_gmp:--enable-gmp --enable-version3} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    %{!?_without_aom:--enable-libaom} \\\
    %{!?_without_dav1d:--enable-libdav1d} \\\
    %{!?_without_ass:--enable-libass} \\\
    %{!?_without_bluray:--enable-libbluray} \\\
    %{?_with_bs2b:--enable-libbs2b} \\\
    %{?_with_caca:--enable-libcaca} \\\
    %{?_with_cuda_nvcc:--enable-cuda-nvcc --enable-nonfree} \\\
    %{?_with_cuvid:--enable-cuvid --enable-nonfree} \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_ieee1394:--enable-libdc1394 --enable-libiec61883} \\\
    --enable-libdrm \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_fdk_aac:--enable-libfdk-aac --enable-nonfree} \\\
    %{?_with_flite:--enable-libflite} \\\
    %{!?_without_jack:--enable-libjack} \\\
    %{!?_without_jxl:--enable-libjxl} \\\
    --enable-libfreetype \\\
    %{!?_without_fribidi:--enable-libfribidi} \\\
    %{?_with_gme:--enable-libgme} \\\
    --enable-libgsm \\\
    %{?_with_ilbc:--enable-libilbc} \\\
    %{!?_without_lensfun:--enable-liblensfun} \\\
    %{?_with_libnpp:--enable-libnpp --enable-nonfree} \\\
    --enable-libmp3lame \\\
    --enable-libmysofa \\\
    %{?_with_netcdf:--enable-netcdf} \\\
    %{?_with_mmal:--enable-mmal} \\\
    %{!?_without_nvenc:--enable-nvenc} \\\
    %{?_with_omx:--enable-omx} \\\
    %{?_with_omx_rpi:--enable-omx-rpi} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{!?_without_opencl:--enable-opencl} \\\
    %{?_with_opencv:--enable-libopencv} \\\
    %{!?_without_opengl:--enable-opengl} \\\
    %{?_with_openh264:--enable-libopenh264} \\\
    --enable-libopenjpeg \\\
    --enable-libopenmpt \\\
    %{!?_without_opus:--enable-libopus} \\\
    %{!?_without_pulse:--enable-libpulse} \\\
    %{?_with_placebo:--enable-libplacebo} \\\
    --enable-librsvg \\\
    %{?_with_rav1e:--enable-librav1e} \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    %{?_with_rubberband:--enable-librubberband} \\\
    %{?_with_smb:--enable-libsmbclient --enable-version3} \\\
    %{?_with_snappy:--enable-libsnappy} \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    --enable-libsrt \\\
    --enable-libssh \\\
    %{?_with_svtav1:--enable-libsvtav1} \\\
    %{?_with_tesseract:--enable-libtesseract} \\\
    --enable-libtheora \\\
    %{?_with_twolame:--enable-libtwolame} \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vidstab:--enable-libvidstab} \\\
    %{?_with_vmaf:--enable-libvmaf --enable-version3} \\\
    %{?_with_vapoursynth:--enable-vapoursynth} \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{!?_without_vulkan:--enable-vulkan --enable-libshaderc} \\\
    %{?_with_webp:--enable-libwebp} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_x265:--enable-libx265} \\\
    %{!?_without_xvid:--enable-libxvid} \\\
    --enable-libxml2 \\\
    %{!?_without_zimg:--enable-libzimg} \\\
    %{?_with_zmq:--enable-libzmq} \\\
    %{!?_without_zvbi:--enable-libzvbi} \\\
    %{!?_without_lv2:--enable-lv2} \\\
    --enable-avfilter \\\
    --enable-libmodplug \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    %{!?_without_gpl:--enable-gpl} \\\
    --disable-debug \\\
    --disable-stripping


%prep
%if 0%{?date}
%autosetup -p1 -n ffmpeg-%{?branch}%{date}
echo "git-snapshot-%{?branch}%{date}-rpmfusion" > VERSION
%else
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n ffmpeg-%{version}
%endif
# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure
mkdir -p _doc/examples
cp -pr doc/examples/{*.c,Makefile,README} _doc/examples/

%build
%{?_with_cuda:export PATH=${PATH}:%{_cuda_bindir}}
%{ff_configure}\
    --shlibdir=%{_libdir} \
%if 0%{?_without_tools:1}
    --disable-doc \
    --disable-ffmpeg --disable-ffplay --disable-ffprobe \
%endif
%ifnarch %{ix86}
    --enable-lto \
%endif
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
    %{?_with_mfx:--enable-libmfx} \
    %{?_with_vpl:--enable-libvpl} \
%ifarch %{ix86} x86_64 %{power64}
    --enable-runtime-cpudetect \
%endif
%ifarch %{power64}
%ifarch ppc64
    --cpu=g5 \
%endif
%ifarch ppc64p7
    --cpu=power7 \
%endif
%ifarch ppc64le
    --cpu=power8 \
%endif
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%endif
%ifarch armv7hl armv7hnl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
%endif
%ifarch armv7hl
    --disable-neon \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif
    || cat ffbuild/config.log

%make_build V=1
make documentation V=1
make alltools V=1

%install
%make_install V=1
%if 0%{!?flavor:1}
rm -r %{buildroot}%{_datadir}/%{name}/examples
%endif
%if 0%{!?progs_suffix:1}
install -pm755 tools/qt-faststart %{buildroot}%{_bindir}
%endif

%if %{with libavcodec_freeworld}
# Install the libavcodec freeworld counterpart
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
mkdir -p %{buildroot}%{_libdir}/%{name}
echo -e "%{_libdir}/%{name}\n" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_lib}.conf
cp -pa %{buildroot}%{_libdir}/libavcodec.so.* \
 %{buildroot}%{_libdir}/%{name}
# Strip to prevent debuginfo duplication
strip %{buildroot}%{_libdir}/%{name}/libavcodec.so.*
%endif

%ldconfig_scriptlets  libs
%ldconfig_scriptlets -n libavdevice%{?flavor}

%if 0%{!?_without_tools:1}
%files
%{_bindir}/ffmpeg%{?progs_suffix}
%{_bindir}/ffplay%{?progs_suffix}
%{_bindir}/ffprobe%{?progs_suffix}
%{!?progs_suffix:%{_bindir}/qt-faststart}
%{!?flavor:
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
}
%{_datadir}/%{name}
%endif

%files libs
%doc  CREDITS README.md
%license COPYING.*
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice%{?build_suffix}.so.*
%{!?flavor:%{_mandir}/man3/lib*.3.*
%exclude %{_mandir}/man3/libavdevice.3*
}

%files -n libavdevice%{?flavor}
%{_libdir}/libavdevice%{?build_suffix}.so.*
%{!?flavor:%{_mandir}/man3/libavdevice.3*}

%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%doc _doc/examples
%doc %{_docdir}/%{name}/*.{css,html}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%if %{with libavcodec_freeworld}
%files -n libavcodec-freeworld
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_lib}.conf
%{_libdir}/%{name}/libavcodec.so.*
%endif


%changelog
%autochangelog
