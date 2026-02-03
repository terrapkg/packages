# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

%global commit db22a4528ff4ca77253c0dbc80fb96908c8c48f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260202
%global ver 0.41.0

Name:           mpv-nightly
Version:        %ver^%commit_date.%shortcommit
Release:        1%?dist

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        Movie player playing most video formats and DVDs
URL:            https://mpv.io/
Source0:        https://github.com/mpv-player/mpv/archive/%commit/mpv-%commit.tar.gz
Conflicts:		mpv

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  meson
BuildRequires:  python3-docutils

BuildRequires:  perl(Encode)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec) >= 59.27.100
BuildRequires:  pkgconfig(libavdevice) >= 58.13.100
BuildRequires:  pkgconfig(libavfilter) >= 7.110.100
BuildRequires:  pkgconfig(libavformat) >= 59.24.100
BuildRequires:  pkgconfig(libavutil) >= 57.24.100
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.19
BuildRequires:  pkgconfig(libplacebo) >= 6.338.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample) >= 3.9.100
BuildRequires:  pkgconfig(libswscale) >= 5.9.100
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(lua-5.1)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uchardet) >= 0.0.5
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(zlib)
%if %{with x11}
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
%endif

%ifarch x86_64
BuildRequires:  libOpenCL.so.1
%endif

Requires:       hicolor-icon-theme
Provides:       mplayer-backend
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

Mpv has an OpenGL, Vulkan, and D3D11 based video output that is capable of many
features loved by videophiles, such as video scaling with popular high quality
algorithms, color management, frame timing, interpolation, HDR, and more.

While mpv strives for minimalism and provides no real GUI, it has a small
controller on top of the video for basic control.

Mpv can leverage most hardware decoding APIs on all platforms. Hardware
decoding can be enabled at runtime on demand.

Powerful scripting capabilities can make the player do almost anything. There
is a large selection of user scripts on the wiki.

A straightforward C API was designed from the ground up to make mpv usable as
a library and facilitate easy integration into other applications.

%package libs
Summary: Dynamic library for Mpv frontends

%description libs
This package contains the dynamic library libmpv, which provides access to Mpv.

%package devel
Summary: Development package for libmpv
Provides: mpv-libs-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: mpv-nightly-libs-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: mpv-libs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: mpv-nightly-libs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires: mpv-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: mpv-nightly-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development header files and libraries for Mpv.

%pkg_completion -Bfz mpv

%prep
%autosetup -p1 -n mpv-%commit
sed -e "s|/usr/local/etc|%{_sysconfdir}/mpv|" -i etc/mpv.conf

%build
%meson --auto-features=auto \
    -Dalsa=enabled \
    -Dbuild-date=false \
    -Dcaca=enabled \
    -Dcdda=enabled \
    -Dcplayer=true \
    -Dcplugins=enabled \
    -Dcuda-hwaccel=enabled \
    -Dcuda-interop=enabled \
    -Ddmabuf-wayland=enabled \
    -Ddrm=enabled \
    -Ddvbin=enabled \
    -Ddvdnav=enabled \
    -Degl-drm=enabled \
    -Degl-wayland=enabled \
%if %{with x11}
    -Degl-x11=enabled \
    -Dgl-x11=enabled \
    -Dvaapi-x11=enabled \
    -Dvdpau-gl-x11=enabled \
    -Dvdpau=enabled \
    -Dx11=enabled \
    -Dxv=enabled \
%endif
    -Degl=enabled \
    -Dgbm=enabled \
    -Dgl=enabled \
    -Dhtml-build=enabled \
    -Diconv=enabled \
    -Djack=enabled \
    -Djavascript=enabled \
    -Djpeg=enabled \
    -Dlcms2=enabled \
    -Dlibarchive=enabled \
    -Dlibavdevice=enabled \
    -Dlibbluray=enabled \
    -Dlibmpv=true \
    -Dlua=enabled \
    -Dmanpage-build=enabled \
    -Dopenal=enabled \
    -Dopensles=disabled \
    -Doss-audio=disabled \
    -Dpipewire=enabled \
    -Dplain-gl=enabled \
    -Dpulse=enabled \
    -Drubberband=enabled \
    -Dsdl2-audio=enabled \
    -Dsdl2-gamepad=enabled \
    -Dsdl2-video=enabled \
    -Dshaderc=disabled \
    -Dsndio=disabled \
    -Dspirv-cross=disabled \
    -Duchardet=enabled \
    -Dvaapi-drm=enabled \
    -Dvaapi-wayland=enabled \
    -Dvaapi=enabled \
    -Dvapoursynth=enabled \
    -Dvector=enabled \
    -Dvulkan=enabled \
    -Dwayland=enabled \
    -Dwerror=false \
    -Dzimg=enabled \
    -Dzlib=enabled
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/mpv.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/mpv.desktop

%files
%docdir %{_docdir}/mpv/
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_docdir}/mpv/
%{_bindir}/mpv
%{_datadir}/applications/mpv.desktop
%{_datadir}/icons/hicolor/*/apps/mpv*.*
%{_mandir}/man1/mpv.*
%{_metainfodir}/mpv.metainfo.xml

%files libs
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_libdir}/libmpv.so.2{,.*}

%files devel
%{_includedir}/mpv/
%{_libdir}/libmpv.so
%{_libdir}/pkgconfig/mpv.pc
