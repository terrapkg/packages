%global av_codec_soversion 61
%global av_device_soversion 61
%global av_filter_soversion 10
%global av_format_soversion 61
%global av_util_soversion 59
%global postproc_soversion 58
%global swresample_soversion 5
%global swscale_soversion 8

Name:           compat-ffmpeg7
Version:        7.1.5
Release:        1%{?dist}
Summary:        FFmpeg 7 compatibility runtime libraries
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz.asc
# https://ffmpeg.org/ffmpeg-devel.asc
# gpg2 --import --import-options import-export,import-minimal ffmpeg-devel.asc > ./ffmpeg.keyring
Source2:        ffmpeg.keyring

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  lame-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(zlib)

Packager:      Terra Packaging Team <terra@fyralabs.com>

%description
Runtime libraries for applications requiring the FFmpeg 7 library ABI.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n ffmpeg-%{version}
# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure

%conf
%set_build_flags

# This is not a normal configure script, don't use %%configure
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-ldflags="%{build_ldflags}" \
    --disable-autodetect \
    --disable-doc \
    --disable-programs \
    --disable-static \
    --disable-stripping \
    --enable-pic \
    --enable-shared \
    --enable-gpl \
    --enable-version3 \
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-alsa \
    --enable-bzlib \
    --enable-cuvid \
    --enable-ffnvcodec \
    --enable-gnutls \
    --enable-gray \
    --enable-iconv \
    --enable-libdav1d \
    --enable-libdrm \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libxml2 \
    --enable-lto \
    --enable-lzma \
    --enable-nvdec \
    --enable-nvenc \
    --enable-postproc \
    --enable-pthreads \
    --enable-swresample \
    --enable-swscale \
    --enable-v4l2-m2m \
    --enable-vaapi \
    --enable-zlib \
    || cat ffbuild/config.log

cat config.h
cat config_components.h

%build
%set_build_flags

%make_build V=1

%install
make install-libs DESTDIR=%{buildroot} V=1

# Drop unversioned development symlinks
rm -f %{buildroot}%{_libdir}/*.so

%files
%license COPYING.GPLv2 LICENSE.md
%{_libdir}/libavcodec.so.%{av_codec_soversion}{,.*}
%{_libdir}/libavdevice.so.%{av_device_soversion}{,.*}
%{_libdir}/libavfilter.so.%{av_filter_soversion}{,.*}
%{_libdir}/libavformat.so.%{av_format_soversion}{,.*}
%{_libdir}/libavutil.so.%{av_util_soversion}{,.*}
%{_libdir}/libpostproc.so.%{postproc_soversion}{,.*}
%{_libdir}/libswresample.so.%{swresample_soversion}{,.*}
%{_libdir}/libswscale.so.%{swscale_soversion}{,.*}

%changelog
* Fri Sep 11 2026 ammix <maxim@ammix.dev> - 7.1.5-1
- Add simplified FFmpeg 7 compatibility package

* Sun May 31 2026 Gilver E. <roachy@fyralabs.com> - 1:8.1.1-1
- Rebased build onto Fedora spec with full redistributable codec support
- Ported to Terra with permission

* Sat May 09 2026 Dominik Mierzejewski <dominik@greysector.net> - 8.1.1-1
- Update to 8.1.1
- Drop merged patch

* Wed Apr 15 2026 Nicolas Chauvet <kwizart@gmail.com> - 8.0.1-7
- Rebuilt for vmaf-3.1.0

* Thu Mar 19 2026 Nicolas Chauvet <kwizart@gmail.com> - 8.0.1-6
- Rebuilt for libplacebo

* Mon Mar 09 2026 Dominik Mierzejewski <dominik@greysector.net> - 8.0.1-5
- Rebuilt for libvpx 1.16.0

* Mon Feb 16 2026 Nick White <fedora@njw.name> - 8.0.1-4
- Enable mov_text encoder and decoder

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 04 2025 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 8.0.1-2
- disable dc1394 and ffnvcodec on risc-v

* Fri Nov 21 2025 Dominik Mierzejewski <dominik@greysector.net> - 8.0.1-1
- Update to 8.0.1 (resolves rhbz#2416044)
- Split configure step to conf stage

* Fri Nov 14 2025 Neal Gompa <ngompa@fedoraproject.org> - 8.0-2
- Disable lc3 only on RHEL 10

* Sun Nov 02 2025 Neal Gompa <ngompa@fedoraproject.org> - 8.0-1
- Rebase to version 8.0

* Sun Nov 02 2025 Dominik Mierzejewski <dominik@greysector.net> - 7.1.2-3
- Re-enable openal support (dropped by accident in commit 5917b714, resolves rhbz#2404091)

* Thu Oct 02 2025 Robert-André Mauchin <zebob.m@gmail.com> - 7.1.2-2
- Rebuild for svt-av1 soname bump

* Wed Sep 24 2025 Simone Caronni <negativo17@gmail.com> - 7.1.2-1
- Update to 7.1.2.
- Enable VANC processing for SDI.
- Explicitly list all implicitly enabled/disabled options.

* Tue Aug 26 2025 Neal Gompa <ngompa@fedoraproject.org> - 7.1.1-10
- Disable all subpackages except libavcodec-freeworld with the freeworld bcond

* Mon Aug 25 2025 Neal Gompa <ngompa@fedoraproject.org> - 7.1.1-9
- Enable support for MPEG-5/EVC

* Thu Aug 21 2025 Neal Gompa <ngompa@fedoraproject.org> - 7.1.1-8
- Reorganize spec to group subpackage definitions together
- Add freeworld conditional for third-party builds
- Drop unneeded scriptlets

* Fri Aug 01 2025 Neal Gompa <ngompa@fedoraproject.org> - 7.1.1-7
- Always verify sources

* Tue Jul 29 2025 Nicolas Chauvet <kwizart@gmail.com> - 7.1.1-6
- Rebuilt for libplacebo

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 13 2025 Neal Gompa <ngompa@fedoraproject.org> - 7.1.1-4
- Switch to regular upstream sources for package build
- Enable more codecs

* Sat Mar 22 2025 Songsong Zhang <U2FsdGVkX1@gmail.com> - 7.1.1-3
- Add missing source files for riscv64

* Thu Mar 13 2025 Fabio Valentini <decathorpe@gmail.com> - 7.1.1-2
- Rebuild for noopenh264 2.6.0

* Thu Mar 06 2025 Dominik Mierzejewski <dominik@greysector.net> - 7.1.1-1
- Update to 7.1.1 (resolves rhbz#2349351)
- Enable LC3 codec via liblc3
- Backport fix for CVE-2025-22921 (resolves rhbz#2346558)

* Fri Feb 07 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 7.1-1
- Rebase to 7.1 (rhbz#2273572)

* Wed Feb 05 2025 Robert-André Mauchin <zebob.m@gmail.com> - 7.0.2-13
- Rebuilt for aom 3.11.0

* Sun Feb 02 2025 Sérgio Basto <sergio@serjux.com> - 7.0.2-12
- Rebuild for jpegxl (libjxl) 0.11.1

* Wed Jan 29 2025 Simone Caronni <negativo17@gmail.com> - 7.0.2-11
- Rebuild for updated VapourSynth.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Michel Lind <salimma@fedoraproject.org> - 7.0.2-9
- Rebuilt for rubberband 4

* Tue Nov 12 2024 Sandro Mani <manisandro@gmail.com> - 7.0.2-8
- Rebuild (tesseract)

* Mon Oct 07 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 7.0.2-7
- Properly enable aribb24/libaribcaption
- Disable VANC dependency as it depends on decklink

* Mon Oct 07 2024 Neal Gompa <ngompa@fedoraproject.org> - 7.0.2-6
- Enable SDI data processing (Kernel Labs VANC) processing
- Enable Japanese DVD subtitles/teletext (aribb24/libaribcaption)

* Mon Oct 07 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 7.0.2-5
- Properly enable noopenh264

* Wed Oct 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 7.0.2-4
- Fix chromaprint bcond

* Wed Sep 25 2024 Michel Lind <salimma@fedoraproject.org> - 7.0.2-3
- Disable omxil completely, it's now retired
- Rebuild for tesseract-5.4.1-3 (soversion change from 5.4.1 to just 5.4)

* Fri Sep 20 2024 Neal Gompa <ngompa@fedoraproject.org> - 7.0.2-2
- Rebuild for newer ffnvcodec

* Fri Sep 06 2024 Neal Gompa <ngompa@fedoraproject.org> - 7.0.2-1
- Rebase to 7.0.2 (rhbz#2273572)
- Drop OpenH264 dlopen headers as we use noopenh264 now
- Use modern bconds

* Sat Aug 24 2024 Fabio Valentini <decathorpe@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Sat Jul 20 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.1.1-19
- Backport fixes for Mesa 24.0.6+ / 21.1.4+ changes for VA-API

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Nicolas Chauvet <kwizart@gmail.com> - 6.1.1-17
- Rebuilt for libplacebo/vmaf

* Wed Jun 19 2024 Dominik Mierzejewski <dominik@greysector.net> - 6.1.1-16
- Backport fix for CVE-2023-49528

* Thu Jun 13 2024 Sandro Mani <manisandro@gmail.com> - 6.1.1-15
- Rebuild for tesseract-5.4.1

* Wed May 29 2024 Robert-André Mauchin <zebob.m@gmail.com> - 6.1.1-14
- Rebuild for svt-av1 2.1.0

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 6.1.1-13
- Rebuild for updated VapourSynth.

* Tue Apr 23 2024 Kalev Lember <klember@redhat.com> - 6.1.1-12
- Stop using bundled openh264 headers in F40+ and build against noopenh264
- Backport a fix to build with Vulkan headers >= 1.3.280.0

* Wed Mar 13 2024 Sérgio Basto <sergio@serjux.com> - 6.1.1-11
- Rebuild for jpegxl (libjxl) 0.10.2

* Tue Mar 12 2024 Dominik Mierzejewski <dominik@greysector.net> - 6.1.1-10
- Enable drawtext filter (requires libharfbuzz)

* Wed Feb 14 2024 Sérgio Basto <sergio@serjux.com> - 6.1.1-9
- Rebuild for jpegxl (libjxl) 0.9.2 with soname bump

* Wed Feb 07 2024 Pete Walter <pwalter@fedoraproject.org> - 6.1.1-8
- Rebuild for libvpx 1.14.x

* Sun Jan 28 2024 Sandro Mani <manisandro@gmail.com> - 6.1.1-7
- Rebuild (tesseract)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.1.1-4
- Add missing files for some of the libraries to fix riscv64 builds

* Fri Jan 12 2024 Fabio Valentini <decathorpe@gmail.com> - 6.1.1-3
- Rebuild for dav1d 1.3.0

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 6.1.1-2
- Backport upstream patch to fix C compatibility issues

* Thu Jan 04 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.1.1-1
- Update to 6.1.1

* Thu Jan 04 2024 Neal Gompa <ngompa@fedoraproject.org> - 6.1-1
- Rebase to 6.1

* Wed Dec 06 2023 Kalev Lember <klember@redhat.com> - 6.0.1-2
- Prefer openh264 over noopenh264
- Backport upstream patch to drop openh264 runtime version checks

* Sat Nov 11 2023 Neal Gompa <ngompa@fedoraproject.org> - 6.0.1-1
- Update to 6.0.1
- Add ffmpeg chromium support patch (#2240127)
- Use git to apply patches

* Fri Nov 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 6.0-16
- Add patches to support enhanced RTMP and AV1 encoding through VA-API
- Force AAC decoding through fdk-aac-free

* Sun Oct 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 6.0-15
- Backport upstream patch to fix segfault when passing non-existent filter
  option (rfbz#6773)

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 6.0-14
- Rebuild (tesseract)

* Fri Sep 29 2023 Nicolas Chauvet <nchauvet@linagora.com> - 6.0-13
- Rebuilt for libplacebo

* Fri Aug 25 2023 Dominik Mierzejewski <dominik@greysector.net> - 6.0-12
- Backport upstream patch to fix assembly with binutils 2.41.

* Sat Aug 05 2023 Richard Shaw <hobbes1069@gmail.com> - 6.0-11
- Rebuild for codec2.

* Fri Jul 28 2023 Dominik Mierzejewski <dominik@greysector.net> - 6.0-10
- Rebuild for libplacebo

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Sandro Mani <manisandro@gmail.com> - 6.0-8
- Rebuild (tesseract)

* Sun Jun 18 2023 Sérgio Basto <sergio@serjux.com> - 6.0-7
- Mass rebuild for jpegxl-0.8.1

* Mon Jun 12 2023 Dominik Mierzejewski <dominik@greysector.net> - 6.0-6
- Rebuild for libdc1394

* Thu Apr 06 2023 Adam Williamson <awilliam@redhat.com> - 6.0-5
- Rebuild (tesseract) again

* Mon Apr 03 2023 Neal Gompa <ngompa@fedoraproject.org> - 6.0-4
- Include RISC-V support sources in the tarball

* Mon Apr 03 2023 Sandro Mani <manisandro@gmail.com> - 6.0-3
- Rebuild (tesseract)

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 6.0-2
- Backport upstream patches for libplacebo support

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 6.0-1
- Rebase to version 6.0
- Enable SVT-AV1 on all architectures
- Use oneVPL for QSV
- Switch to SPDX license identifiers

* Wed Feb 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.1.2-12
- Enable support for the RIST protocol through librist

* Wed Feb 15 2023 Tom Callaway <spot@fedoraproject.org> - 5.1.2-11
- bootstrap off

* Wed Feb 15 2023 Tom Callaway <spot@fedoraproject.org> - 5.1.2-10
- rebuild for libvpx (bootstrap)

* Mon Feb 13 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.1.2-9
- Enable lcms2, lv2, placebo, rabbitmq, xv

* Mon Feb 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.1.2-8
- Disable flite for RHEL 9 as flite is too old

* Fri Feb 03 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.1.2-7
- Properly enable caca, flite, gme, iec61883

* Mon Jan 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.1.2-6
- Enable more approved codecs

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.1.2-4
- Properly enable libzvbi_teletext decoder

* Fri Dec 23 2022 Sandro Mani <manisandro@gmail.com> - 5.1.2-3
- Rebuild (tesseract)

* Wed Nov 09 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.1.2-2
- Unconditionally enable Vulkan

* Wed Oct 12 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.1.2-1
- Update to version 5.1.2
- Refresh dlopen headers and patch for OpenH264 2.3.1

* Sun Sep 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.1.1-1
- Update to version 5.1.1
- Refresh dlopen headers for OpenH264 2.3.0
- Disable omxil and crystalhd for RHEL

* Wed Aug 24 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.1-1
- Rebase to version 5.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Richard Shaw <hobbes1069@gmail.com> - 5.0.1-15
- Rebuild for codec2 1.0.4.

* Fri Jul 08 2022 Sandro Mani <manisandro@gmail.com> - 5.0.1-14
- Rebuild (tesseract)

* Wed Jun 22 2022 Robert-André Mauchin <zebob.m@gmail.com> - 5.0.1-13
- Rebuilt for new aom, dav1d, rav1e and svt-av1

* Fri Jun 17 2022 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 5.0.1-12
- Rebuild for new srt

* Thu Jun 09 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-11
- Ensure libavdevice-devel is pulled in with devel metapackage

* Sun Jun 05 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-10
- Update for OpenH264 2.2.0

* Tue May 31 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-9
- Rebuild for ilbc-3.0.4

* Thu May 26 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 5.0.1-9
- Rebuild for ilbc-3.0.4 (bootstrap)

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 5.0.1-8
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 5.0.1-7
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Sun Apr 24 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-6
- Add VAAPI encoders for mjpeg, mpeg2, vp8, and vp9
- Ensure hwaccels for enabled codecs are turned on

* Tue Apr 19 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-5
- Drop unused enca build dependency

* Tue Apr 19 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-4
- Use shaderc for Vulkan support

* Mon Apr 18 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-3
- Fix codec2 support enablement

* Mon Apr 18 2022 Dominik Mierzejewski <dominik@greysector.net> - 5.0.1-2
- Properly enable decoding and encoding ilbc

* Tue Apr 12 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1 to fix crashes with muxing MP4 video (#2073980)

* Tue Apr 05 2022 Dominik Mierzejewski <dominik@greysector.net> - 5.0-11
- Enable OpenCL acceleration
- be explicit about enabled external features in configure
- enable gcrypt
- drop duplicate CFLAGS and use Fedora LDFLAGS

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 5.0-10
- Rebuild for tesseract 5.1.0

* Tue Mar 08 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-9
- Drop ffmpeg chromium support patch (#2061392)

* Fri Feb 18 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-8
- Add patch to return correct AVERROR with bad OpenH264 versions

* Fri Feb 18 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-7
- Update OpenH264 dlopen patch to split dlopen code into c and h files

* Thu Feb 17 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-6
- Update OpenH264 dlopen patch to use AVERROR return codes correctly

* Tue Feb 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-5
- Disable hardware decoders due to broken failure modes

* Tue Feb 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-4
- Add support for dlopening OpenH264
- Add tarball scripts as sources

* Sun Feb 13 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-3
- Enable more QSV and V4L2M2M codecs

* Sun Feb 13 2022 Neal Gompa <ngompa@fedoraproject.org> - 5.0-2
- Enable support for more hardware codecs

* Fri Feb 11 2022 Andreas Schneider <asn@redhat.com> - 5.0-1
- Initial import (fedora#2051008)
