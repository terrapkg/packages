# codecs which cannot be shipped in Fedora proper
%bcond freeworld 1
%bcond x264 %{with freeworld}
%bcond x265 %{with freeworld}

# not compatible with asdcplib-2.12
%bcond asdcp %[!(0%{?fedora} >= 38 || 0%{?rhel} >= 10)]
# not compatible with opencv 3.4 or 4.0
# https://code.videolan.org/videolan/vlc/-/issues/22016
%bcond opencv 0
# not compatible with libplacebo-6
# https://code.videolan.org/videolan/vlc/-/merge_requests/3950
%bcond placebo %[!(0%{?fedora} >= 39 || 0%{?rhel} >= 10)]
# disabled due to various issues
%bcond projectm 0

# some dependencies are not yet in EPEL 10
%bcond daala %{undefined el10}
%bcond lirc 1
%bcond schro %[!(0%{?rhel} >= 10)]
%bcond sdl %[!(0%{?rhel} >= 10)]

%ifnarch s390x
# retired from F43, was never in EPEL 9+
%bcond crystalhd 0
%bcond ieee1394 1
%endif

%ifarch x86_64
%bcond vpl 1
%endif

Name:       vlc
Epoch:      2
Version:    3.0.21
Release:    1%{?dist}
Summary:    The cross-platform open-source multimedia framework, player and server
License:    GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause
URL:        https://www.videolan.org
Source0:    https://get.videolan.org/vlc/%{version}/vlc-%{version}.tar.xz
Source1:    macros.vlc

## upstream patches
# opus_header: fix channel mapping family 1 parsing (rhbz#2307919)
Patch0:     https://code.videolan.org/videolan/vlc/-/merge_requests/5590.patch
# add support for ffmpeg 7.0 (without VAAPI)
Patch1:     https://code.videolan.org/videolan/vlc/-/merge_requests/5574.patch
# mux: avformat: fix avio callbacks signature with ffmpeg 6.1
Patch2:     https://code.videolan.org/videolan/vlc/-/merge_requests/6168.patch
# ffmpeg: backport more channel checks
Patch3:     https://code.videolan.org/videolan/vlc/-/merge_requests/6273.patch
# avcodec: vaapi: support VAAPI with latest FFmpeg
Patch4:     https://code.videolan.org/videolan/vlc/-/merge_requests/6606.patch
# nfs: fix libnfs API v2 support (rhbz#2341791)
Patch5:     https://code.videolan.org/videolan/vlc/-/merge_requests/6527.patch

## upstreamable patches

## downstream patches
# https://fedoraproject.org/wiki/Changes/CryptoPolicy
Patch:      0001-Use-SYSTEM-wide-ciphers-for-gnutls.patch
# Fix building with fdk-aac-2.0; backport for 3.0 from flathub
Patch:      fdk-aac2.patch
# port from intel-mediasdk to oneVPL
Patch:      oneVPL.patch
# fix appstreamcli validate to show in Software (rhbz#2258611)
Patch:      appdata.patch
# port from libidn to libidn2
Patch:      libidn2.patch
# fix deprecated lua math functions (rhbz#2280091)
Patch:      lua-math.patch
# update to freerdp2 api; backport from master
Patch:      freerdp2.patch
# fix build with live555-2024.11.28
Patch:      live555.patch

%{load:%{S:1}}
%global __provides_exclude_from ^%{vlc_plugindir}/.*$

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  a52dec-devel
BuildRequires:  aalib-devel
BuildRequires:  faad2-devel
BuildRequires:  hostname
BuildRequires:  kernel-headers
%if %{with crystalhd}
BuildRequires:  libcrystalhd-devel
%endif
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libpng-devel
%if %{with lirc}
BuildRequires:  lirc-devel
%endif
BuildRequires:  live555-devel
BuildRequires:  lua-devel
BuildRequires:  pkgconfig(alsa) >= 1.0.24
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(aribb24)
BuildRequires:  pkgconfig(aribb25)
%if %{with asdcp}
BuildRequires:  pkgconfig(asdcplib)
%endif
BuildRequires:  pkgconfig(avahi-client) >= 0.6
#BuildRequires: pkgconfig(breakpad-client)
BuildRequires:  pkgconfig(caca) >= 0.99.beta14
%if %{with daala}
BuildRequires:  pkgconfig(daaladec)
BuildRequires:  pkgconfig(daalaenc)
%endif
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dvdnav) > 4.9.0
BuildRequires:  pkgconfig(dvdread) > 4.9.0
BuildRequires:  pkgconfig(egl)
#BuildRequires: pkgconfig(evas)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(flac)
#BuildRequires: pkgconfig(fluidlite)
BuildRequires:  pkgconfig(fluidsynth) >= 1.1.2
BuildRequires:  pkgconfig(fontconfig) >= 2.11
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gnutls) >= 3.3.6
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jack) >= 1.9.7
BuildRequires:  pkgconfig(kate) >= 0.3.0
BuildRequires:  pkgconfig(libarchive) >= 3.1.0
BuildRequires:  pkgconfig(libass) >= 0.9.8
BuildRequires:  pkgconfig(libavcodec) >= 57.37.100
BuildRequires:  pkgconfig(libavformat) >= 53.21.0
BuildRequires:  pkgconfig(libavutil) >= 52.0.0
BuildRequires:  pkgconfig(libbluray) >= 0.6.2
BuildRequires:  pkgconfig(libcddb) >= 0.9.5
BuildRequires:  pkgconfig(libchromaprint)
%if %{with ieee1394}
BuildRequires:  pkgconfig(libdc1394-2) >= 2.1.0
%endif
BuildRequires:  pkgconfig(libdca) >= 0.0.5
#BuildRequires: pkgconfig(libdsm) >= 0.2.0
BuildRequires:  pkgconfig(libdvbpsi)
BuildRequires:  pkgconfig(libebml) >= 1.3.6
BuildRequires:  pkgconfig(libgme)
#BuildRequires: pkgconfig(libgoom2)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libmatroska)
BuildRequires:  pkgconfig(libmodplug) >= 0.8.9.0
BuildRequires:  pkgconfig(libmpeg2) >= 0.3.2
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp) >= 1.0.0
BuildRequires:  pkgconfig(libnfs) >= 1.10.0
BuildRequires:  pkgconfig(libnotify) pkgconfig(gtk+-3.0)
%if %{with placebo}
BuildRequires:  pkgconfig(libplacebo) < 6
%endif
BuildRequires:  pkgconfig(libpostproc)
%if %{with projectm}
BuildRequires:  pkgconfig(libprojectM)
%endif
BuildRequires:  pkgconfig(libpulse) >= 1.0
%if %{with ieee1394}
BuildRequires:  pkgconfig(libraw1394) >= 2.0.1 pkgconfig(libavc1394) >= 0.5.3
%endif
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.9.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
#BuildRequires: pkgconfig(libsidplay2)
#BuildRequires: pkgconfig(libsmb2) >= 3.0.0
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 142
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libva) >= 0.38
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvncclient) >= 0.9.9
#BuildRequires: pkgconfig(libvsxu)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5
BuildRequires:  pkgconfig(microdns) >= 0.1.2
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ogg) >= 1.0
%if %{with opencv}
BuildRequires:  pkgconfig(opencv)
%endif
BuildRequires:  pkgconfig(opus) >= 1.0.3
BuildRequires:  pkgconfig(protobuf-lite) >= 2.5
BuildRequires:  pkgconfig(Qt5Core) >= 5.5
BuildRequires:  pkgconfig(Qt5Gui) >= 5.5
BuildRequires:  pkgconfig(Qt5Svg) >= 5.5
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.5
BuildRequires:  pkgconfig(samplerate)
%if %{with schro}
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
%endif
%if %{with sdl}
BuildRequires:  pkgconfig(SDL_image) >= 1.2.10
%endif
#BuildRequires: pkgconfig(shine) >= 3.0.0
BuildRequires:  pkgconfig(shout) >= 2.1
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(soxr) >= 0.1.2
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(spatialaudio)
BuildRequires:  pkgconfig(speex) >= 1.0.5
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(tiger) >= 0.3.1
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau) >= 0.6
BuildRequires:  pkgconfig(vorbis) >= 1.1
BuildRequires:  pkgconfig(vorbisenc) >= 1.1
%if %{with vpl}
BuildRequires:  pkgconfig(vpl)
%endif
BuildRequires:  pkgconfig(vpx) >= 1.5.0
BuildRequires:  pkgconfig(wayland-client) >= 1.5.91
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
#BuildRequires: pkgconfig(x262)
%if %{with x264}
BuildRequires:  pkgconfig(x264) >= 0.153
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:  pkgconfig(xcb-randr) >= 1.3
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xv) >= 1.1.90.1
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires:       kde-filesystem
%else
Requires:       kf5-filesystem
%endif
Requires:       %{name}-gui-qt%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     %{name}-gui-skins2%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     %{name}-plugin-ffmpeg%{?_isa} = %{epoch}:%{version}-%{release}
# For xdg-screensaver (libxdg_screensaver_plugin)
Recommends:     xdg-utils
Recommends:     xset
Provides:       %{name}-xorg%{?_isa} = %{epoch}:%{version}-%{release}


%description
VLC media player is a highly portable multimedia player and multimedia framework
capable of reading most audio and video formats as well as DVDs, Audio CDs VCDs,
and various streaming protocols.
It can also be used as a media converter or a server to stream in uni-cast or
multi-cast in IPv4 or IPv6 on networks.

%package libs
Summary:    VLC media player runtime libraries
Recommends: libproxy-bin%{?_isa}
Conflicts:  %{name}-core < %{epoch}:%{version}-%{release}
%description libs
VLC media player runtime libraries

%package cli
Summary:    VLC media player command line interface
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: %{name}-plugin-lua%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:  %{name}-core < %{epoch}:%{version}-%{release}
Provides:   %{name}-core = %{epoch}:%{version}-%{release}
Provides:   %{name}-nox = %{epoch}:%{version}-%{release}
%description cli
VLC media player command line interfaces

%package gui-ncurses
Summary:    VLC media player TUI
Requires:   %{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
%description gui-ncurses
VLC media player ncurses-based terminal interface

%package gui-qt
Summary:    VLC media player Qt GUI
Requires:   %{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-video-out%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-lua%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   (%{name}-plugin-pipewire%{?_isa} if pipewire)
Requires:   (%{name}-plugin-pulseaudio%{?_isa} = %{epoch}:%{version}-%{release} if (pipewire-pulseaudio or pulseaudio))
Requires:   (qt5-qtwayland%{?_isa} if libwayland-client%{?_isa})
Recommends: %{name}-plugins-extra%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: %{name}-plugin-ffmpeg%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: %{name}-plugin-visualization%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: (%{name}-plugin-gnome%{?_isa} = %{epoch}:%{version}-%{release} if gnome-keyring)
Recommends: (%{name}-plugin-kde%{?_isa} = %{epoch}:%{version}-%{release} if (kf6-kwallet or kf5-wallet))
Recommends: (%{name}-plugin-notify%{?_isa} = %{epoch}:%{version}-%{release} if gtk3)
%description gui-qt
VLC media player Qt graphical interface

%package gui-skins2
Summary:    VLC media player Skins2 GUI
Requires:   %{name}-cli%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-gui-qt%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   gnu-free-sans-fonts

%description gui-skins2
VLC media player skinnable graphical interface

%package plugins-all
Summary:    VLC media player - all plugins
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-extra%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-video-out%{?_isa} = %{epoch}:%{version}-%{release}
%if %{with crystalhd}
Requires:   %{name}-plugin-crystalhd%{?_isa} = %{epoch}:%{version}-%{release}
%endif
Requires:   %{name}-plugin-ffmpeg%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-fluidsynth%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   (%{name}-plugin-gnome%{?_isa} = %{epoch}:%{version}-%{release} if gnome-keyring)
Requires:   %{name}-plugin-gstreamer%{?_isa} = %{epoch}:%{version}-%{release}
%if %{with ieee1394}
Requires:   %{name}-plugin-ieee1394%{?_isa} = %{epoch}:%{version}-%{release}
%endif
Requires:   (%{name}-plugin-jack%{?_isa} = %{epoch}:%{version}-%{release} if (jack-audio-connection-kit or pipewire-jack-audio-connection-kit))
Requires:   (%{name}-plugin-kde%{?_isa} = %{epoch}:%{version}-%{release} if (kf6-kwallet or kf5-wallet))
Requires:   %{name}-plugin-lua%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   (%{name}-plugin-notify%{?_isa} = %{epoch}:%{version}-%{release} if gtk3)
%if %{with opencv}
Requires:   %{name}-plugin-opencv%{?_isa} = %{epoch}:%{version}-%{release}
%endif
Requires:   (%{name}-plugin-pulseaudio%{?_isa} = %{epoch}:%{version}-%{release} if (pipewire-pulseaudio or pulseaudio))
Requires:   %{name}-plugin-rdp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-samba%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-svg%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-visualization%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugin-vnc%{?_isa} = %{epoch}:%{version}-%{release}
# separate plugins
Requires:   %{name}-plugin-bittorrent%{?_isa}
Requires:   %{name}-plugin-pause-click%{?_isa}
Requires:   (%{name}-plugin-pipewire%{?_isa} if pipewire)

%description plugins-all
Installs all available plugins for VLC media player

%package plugins-base
Summary:    VLC media player core
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 10
Requires:   google-noto-sans-mono-fonts
Requires:   google-noto-serif-fonts
%else
Requires:   google-noto-sans-mono-vf-fonts
Requires:   google-noto-serif-vf-fonts
%endif
Recommends: libv4l%{?_isa}
Conflicts:  %{name}-core < %{epoch}:%{version}-%{release}
%if %{without crystalhd}
Obsoletes:  %{name}-plugin-crystalhd < %{epoch}:%{version}-%{release}
%endif
%if %{without ieee1394}
Obsoletes:  %{name}-plugin-ieee1394 < %{epoch}:%{version}-%{release}
%endif
%if %{without opencv}
Obsoletes:  %{name}-plugin-opencv < %{epoch}:%{version}-%{release}
%endif
# Handle Freeworld transition
%if %{with freeworld}
Provides:   %{name}-plugins-freeworld = %{epoch}:%{version}-%{release}
Obsoletes:  %{name}-plugins-freeworld < %{epoch}:%{version}-%{release}
%endif

%description plugins-base
VLC media player core components

%package plugins-extra
Summary:    VLC media player extra plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Conflicts:  %{name}-plugins-base < %{epoch}:%{version}-%{release}

%description plugins-extra
VLC media player additional components

# libcrystalhd requires crystalhd-firmware, is for specific hardware
%if %{with crystalhd}
%package plugin-crystalhd
Summary:    VLC media player Crystal HD plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:  %{name}-extras < %{epoch}:%{version}-%{release}
Provides:   %{name}-extras = %{epoch}:%{version}-%{release}

%description plugin-crystalhd
Crystal HD plugin for VLC media player.
%endif

# libavcodec/libavformat etc. have many dependencies
%package plugin-ffmpeg
Summary:    VLC media player FFmpeg plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-video-out%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-ffmpeg
FFmpeg support plugins for VLC media player.

# for MIDI playback, requires a soundfont (usually quite large)
%package plugin-fluidsynth
Summary:    VLC media player MIDI playback plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: fluid-soundfont-gm

%description plugin-fluidsynth
MIDI playback support plugin for VLC media player.

# requires libsecret, for gnome-keyring secrets storage on GNOME
%package plugin-gnome
Summary:    VLC media player Gnome Keyring plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-gnome
Gnome Keyring integration for VLC media player.

# alternative codecs for specific formats, requires many of its own plugins
%package plugin-gstreamer
Summary:    VLC media player GStreamer codec plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   gstreamer1-plugins-good%{?_isa}
Requires:   gstreamer1-plugins-bad-free%{?_isa}
Recommends: gstreamer1-plugin-libav%{?_isa}
Recommends: gstreamer1-plugin-openh264%{?_isa}

%description plugin-gstreamer
GStreamer decoder plugins for VLC media player.

# requires libdc1394/libavc1394/libraw1394, is for specific hardware
%if %{with ieee1394}
%package plugin-ieee1394
Summary:    VLC media player IEEE 1394 plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-ieee1394
IEEE 1394 (FireWire) plugins for VLC media player.
%endif

# depends on j-a-c-k or pipewire-j-a-c-k, for low-latency audio
%package plugin-jack
Summary:    VLC media player JACK plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

Suggests:   pipewire-jack-audio-connection-kit
%description plugin-jack
PulseAudio plugins for VLC media player.

# for KWallet secrets storage on KDE Plasma
%package plugin-kde
Summary:    VLC media player KWallet plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-kde
KDE KWallet integration for VLC media player.

# requires lua, used by CLI and GUI
%package plugin-lua
Summary:    VLC media player lua scripting plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%{?lua_version:Requires: lua(abi) = %{lua_version}}
%description plugin-lua
Lua scripting support for VLC media player.

# requires gtk3 to render the notification icon
%package plugin-notify
Summary:    VLC media player notification plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-notify
Desktop notification plugin for VLC media player.

# opencv has many dependencies
%if %{with opencv}
%package plugin-opencv
Summary:    VLC media player OpenCV plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-opencv
OpenCV plugins for VLC media player.
%endif

# uses libpulse to connect to pipewire-pulseaudio
# vlc-plugin-pipewire plugin is an alternative
%package plugin-pulseaudio
Summary:    VLC media player PulseAudio plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-pulseaudio
PulseAudio plugins for VLC media player.

# requires freerdp2, for RDP remote desktop support
%package plugin-rdp
Summary:    VLC media player RDP plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-rdp
RDP access plugin for VLC media player.

# requires libsmbclient, for SMB protocol support
%package plugin-samba
Summary:    VLC media player SMB plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-samba
Samba access plugin for VLC media player.

# requires librsvg2, for SVG decoding and screen overlay
%package plugin-svg
Summary:    VLC media player SVG plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-svg
SVG plugins for VLC media player.

# requires libv4l, libva, OpenGL, X11/xcb, etc.
%package plugins-video-out
Summary:    VLC media player vout plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugins-video-out
Video output plugins for VLC media player.

%package plugin-visualization
Summary:    VLC media player visualization plugins
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-visualization
Visualization plugins for VLC media player.

%package plugin-vnc
Summary:    VLC media player VNC plugin
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:   %{name}-plugins-base%{?_isa} = %{epoch}:%{version}-%{release}

%description plugin-vnc
VNC access plugin for VLC media player.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications and plugins that use %{name}.


%prep
%autosetup -p1

rm -f aclocal.m4 m4/lib*.m4 m4/lt*.m4
./bootstrap

# switch "Allow automatic icon change" to opt-in
sed -i -e 's|\("qt-icon-change",\) true|\1 false|' modules/gui/qt/qt.cpp

# sync appstream app-id with Flathub
# fill in release date from appstream.patch
# https: https://code.videolan.org/videolan/vlc/-/merge_requests/1555 (4.0)
sed -e 's|org\.videolan\.vlc|org.videolan.VLC|' \
    -e 's|@DATE@|%(date +%F -r %{S:0})|' \
    -e 's|http:|https:|g' \
    -i share/vlc.appdata.xml.in.in

# Fix an issue with our CI technically being run as root since VLC cannot be run as root. We should still run the other tests, so the workaround is to make the script not fail.
echo "%{_bindir}/true" > test/run_vlc.sh

touch src/revision.txt


%build
export LIVE555_PREFIX=%{_prefix}
%configure                                            \
    --disable-silent-rules                            \
    --disable-dependency-tracking                     \
    --with-binary-version=%{version}                  \
    --disable-static                                  \
    --with-pic                                        \
    --disable-rpath                                   \
    --enable-dbus                                     \
    --disable-optimizations                           \
    --enable-lua                                      \
    --enable-archive                                  \
    --enable-live555                                  \
    --enable-dc1394%{!?with_ieee1394:=no}             \
    --enable-dv1394%{!?with_ieee1394:=no}             \
    --enable-linsys                                   \
    --enable-dvdread                                  \
    --enable-dvdnav                                   \
    --enable-bluray                                   \
    --enable-opencv%{!?with_opencv:=no}               \
    --enable-smbclient                                \
    --disable-dsm                                     \
    --enable-sftp                                     \
    --enable-nfs                                      \
    --disable-smb2                                    \
    --enable-v4l2                                     \
    --disable-decklink                                \
    --enable-vcd                                      \
    --enable-libcddb                                  \
    --enable-screen                                   \
    --enable-vnc                                      \
    --enable-freerdp                                  \
    --enable-realrtsp                                 \
    --enable-asdcp%{!?with_asdcp:=no}                 \
    --enable-dvbpsi                                   \
    --enable-gme                                      \
    --disable-sid                                     \
    --enable-ogg                                      \
    --enable-shout                                    \
    --enable-matroska                                 \
    --enable-mod                                      \
    --enable-mpc                                      \
    --disable-shine                                   \
    --disable-omxil                                   \
    --enable-crystalhd%{!?with_crystalhd:=no}         \
    --enable-mad                                      \
    --enable-mpg123                                   \
    --enable-gst-decode                               \
    --enable-avcodec                                  \
    --enable-libva                                    \
    --enable-avformat                                 \
    --enable-swscale                                  \
    --enable-postproc                                 \
    --enable-faad                                     \
    --enable-aom                                      \
    --enable-dav1d                                    \
    --enable-vpx                                      \
    --enable-twolame                                  \
    --enable-fdkaac                                   \
    --enable-a52                                      \
    --enable-dca                                      \
    --enable-flac                                     \
    --enable-libmpeg2                                 \
    --enable-vorbis                                   \
    --enable-tremor                                   \
    --enable-speex                                    \
    --enable-opus                                     \
    --enable-spatialaudio                             \
    --enable-theora                                   \
    --enable-oggspots                                 \
    --enable-daala%{!?with_daala:=no}                 \
    --enable-schroedinger%{!?with_schro:=no}          \
    --enable-png                                      \
    --enable-jpeg                                     \
    --disable-bpg                                     \
    --disable-x262                                    \
    --enable-x265%{!?with_x265:=no}                   \
    --enable-x264%{!?with_x264:=no}                   \
    --enable-x26410b%{!?with_x264:=no}                \
    --enable-vpl%{!?with_vpl:=no}                     \
    --enable-fluidsynth                               \
    --disable-fluidlite                               \
    --enable-zvbi                                     \
    --disable-telx                                    \
    --enable-libass                                   \
    --enable-aribsub                                  \
    --enable-aribb25                                  \
    --enable-kate                                     \
    --enable-tiger                                    \
    --enable-css                                      \
    --enable-gles2                                    \
    --enable-xcb                                      \
    --enable-xvideo                                   \
    --enable-vdpau                                    \
    --enable-wayland                                  \
    --enable-sdl-image%{!?with_sdl:=no}               \
    --enable-freetype                                 \
    --enable-fribidi                                  \
    --enable-harfbuzz                                 \
    --enable-fontconfig                               \
    --with-default-font-family=NotoSerif              \
    --with-default-monospace-font-family=NotoSansMono \
    --enable-svg                                      \
    --enable-svgdec                                   \
    --enable-aa                                       \
    --enable-caca                                     \
    --disable-mmal                                    \
    --disable-evas                                    \
    --enable-pulse                                    \
    --enable-alsa                                     \
    --enable-jack                                     \
    --enable-samplerate                               \
    --enable-soxr                                     \
    --enable-chromaprint                              \
    --enable-chromecast                               \
    --enable-qt                                       \
    --enable-skins2                                   \
    --disable-libtar                                  \
    --enable-lirc%{!?with_lirc:=no}                   \
    --enable-srt                                      \
    --disable-goom                                    \
    --enable-projectm%{!?with_projectm:=no}           \
    --disable-vsxu                                    \
    --enable-avahi                                    \
    --enable-udev                                     \
    --enable-mtp                                      \
    --enable-upnp                                     \
    --enable-microdns                                 \
    --enable-libxml2                                  \
    --enable-libgcrypt                                \
    --enable-gnutls                                   \
    --enable-taglib                                   \
    --enable-secret                                   \
    --enable-kwallet                                  \
    --disable-update-check                            \
    --enable-notify                                   \
    --enable-libplacebo%{!?with_placebo:=no}          \
    --with-kde-solid=%{_datadir}/solid/actions        \
    %{nil}

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
# avoid redefinition warnings
sed -i -e '/^#define _FORTIFY_SOURCE/d' config.h

%make_build

%install
%make_install CPPROG="cp -p"

# RPM macros for other vlc-plugin-* packages
install -Dm644 %{S:1} -t %{buildroot}%{_rpmmacrodir}

# Ghost the plugins cache
touch %{buildroot}%{vlc_plugindir}/plugins.dat

# Use installed fonts for skins2; gnu-free is part of flatpak runtime
rm -f %{buildroot}%{_datadir}/vlc/skins2/fonts/FreeSans{,Bold}.ttf
ln -s %{_usr}/share/fonts/gnu-free/FreeSans{,Bold}.ttf %{buildroot}%{_datadir}/vlc/skins2/fonts/

# Remove libtool libraries (for RHEL 9 and older)
find %{buildroot}%{_libdir} -name '*.la' -delete

# unpackaged static library
rm -f %{buildroot}%{_libdir}/vlc/libcompat.*

# GNOME 2 script, not compatible with GNOME 3+
rm -f %{buildroot}%{_datadir}/vlc/utils/gnome-vlc-default.sh

# The default PNG icons are used for desktop menu, notifications, and SNI;
# all other icons are compiled in as resources
find %{buildroot}%{_hicolordir} -type f ! -name 'vlc.png' -delete
rm -f %{buildroot}%{_datadir}/vlc/vlc.ico

# docs will be installed in %%files
rm -rf %{buildroot}%{_docdir}/vlc

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_appsdir}/vlc.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/vlc.appdata.xml

# chroma_copy_test fails on s390x (big endian?)
%ifnarch s390x
%{__make} check
%endif

%transfiletriggerin libs -- %{vlc_plugindir}
%{_libdir}/vlc/vlc-cache-gen %{vlc_plugindir} &>/dev/null || :

%transfiletriggerpostun libs -- %{vlc_plugindir}
%{_libdir}/vlc/vlc-cache-gen %{vlc_plugindir} &>/dev/null || :

%files
%doc AUTHORS NEWS README THANKS
%license COPYING COPYING.LIB
%{_appsdir}/%{name}.desktop
%{_hicolordir}/*/apps/%{name}.png
%{_datadir}/solid/actions/%{name}-*.desktop
%{_datadir}/vlc/utils/
%{_metainfodir}/%{name}.appdata.xml

%files libs -f %{name}.lang
%license COPYING.LIB
# client library, used by e.g. kaffeine, phonon-backend-vlc, etc.
%{_libdir}/libvlc.so.5{,.*}
# plugin API, used by vlc-plugin(s)-*
%{_libdir}/libvlccore.so.9{,.*}
%dir %{_libdir}/vlc/
%{_libdir}/vlc/vlc-cache-gen
%dir %{vlc_plugindir}
%ghost %{vlc_plugindir}/plugins.dat

%files cli
%{_bindir}/vlc
%{_bindir}/cvlc
%{_bindir}/rvlc
%{_bindir}/vlc-wrapper
%{_mandir}/man1/vlc*.1*

%files gui-ncurses
%{_bindir}/nvlc
%{vlc_plugindir}/gui/libncurses_plugin.so

%files gui-qt
%{_bindir}/qvlc
%{vlc_plugindir}/gui/libqt_plugin.so

%files gui-skins2
%{_bindir}/svlc
%{vlc_plugindir}/gui/libskins2_plugin.so
%{_datadir}/vlc/skins2/

%files plugins-all

%files plugins-base
%license COPYING COPYING.LIB
%dir %{vlc_plugindir}/access/
%dir %{vlc_plugindir}/access_output/
%dir %{vlc_plugindir}/audio_filter/
%dir %{vlc_plugindir}/audio_mixer/
%dir %{vlc_plugindir}/audio_output/
%dir %{vlc_plugindir}/codec/
%dir %{vlc_plugindir}/control/
%dir %{vlc_plugindir}/demux/
%dir %{vlc_plugindir}/gui/
%dir %{vlc_plugindir}/keystore/
%dir %{vlc_plugindir}/logger/
%dir %{vlc_plugindir}/meta_engine/
%dir %{vlc_plugindir}/misc/
%dir %{vlc_plugindir}/mux/
%dir %{vlc_plugindir}/notify/
%dir %{vlc_plugindir}/packetizer/
%dir %{vlc_plugindir}/services_discovery/
%dir %{vlc_plugindir}/spu/
%dir %{vlc_plugindir}/stream_extractor/
%dir %{vlc_plugindir}/stream_filter/
%dir %{vlc_plugindir}/stream_out/
%dir %{vlc_plugindir}/text_renderer/
%dir %{vlc_plugindir}/vaapi/
%dir %{vlc_plugindir}/vdpau/
%dir %{vlc_plugindir}/video_chroma/
%dir %{vlc_plugindir}/video_filter/
%dir %{vlc_plugindir}/video_output/
%dir %{vlc_plugindir}/video_splitter/
%dir %{vlc_plugindir}/visualization/
%dir %{_datadir}/vlc/
%{vlc_plugindir}/access/libaccess_alsa_plugin.so
%{vlc_plugindir}/access/libaccess_concat_plugin.so
%{vlc_plugindir}/access/libaccess_imem_plugin.so
%{vlc_plugindir}/access/libaccess_mms_plugin.so
%{vlc_plugindir}/access/libaccess_realrtsp_plugin.so
%{vlc_plugindir}/access/libattachment_plugin.so
%{vlc_plugindir}/access/libdtv_plugin.so
%{vlc_plugindir}/access/libfilesystem_plugin.so
%{vlc_plugindir}/access/libftp_plugin.so
%{vlc_plugindir}/access/libhttp_plugin.so
%{vlc_plugindir}/access/libhttps_plugin.so
%{vlc_plugindir}/access/libidummy_plugin.so
%{vlc_plugindir}/access/libimem_plugin.so
%{vlc_plugindir}/access/librist_plugin.so
%{vlc_plugindir}/access/librtp_plugin.so
%{vlc_plugindir}/access/libsatip_plugin.so
%{vlc_plugindir}/access/libsdp_plugin.so
%{vlc_plugindir}/access/libshm_plugin.so
%{vlc_plugindir}/access/libtcp_plugin.so
%{vlc_plugindir}/access/libtimecode_plugin.so
%{vlc_plugindir}/access/libudp_plugin.so
%{vlc_plugindir}/access/libvcd_plugin.so
%{vlc_plugindir}/access/libvdr_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_dummy_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_file_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_http_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_livehttp_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_rist_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_shout_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_udp_plugin.so
%{vlc_plugindir}/audio_filter/libaudio_format_plugin.so
%{vlc_plugindir}/audio_filter/libaudiobargraph_a_plugin.so
%{vlc_plugindir}/audio_filter/libchorus_flanger_plugin.so
%{vlc_plugindir}/audio_filter/libcompressor_plugin.so
%{vlc_plugindir}/audio_filter/libdolby_surround_decoder_plugin.so
%{vlc_plugindir}/audio_filter/libequalizer_plugin.so
%{vlc_plugindir}/audio_filter/libgain_plugin.so
%{vlc_plugindir}/audio_filter/libheadphone_channel_mixer_plugin.so
%{vlc_plugindir}/audio_filter/libkaraoke_plugin.so
%{vlc_plugindir}/audio_filter/libmono_plugin.so
%{vlc_plugindir}/audio_filter/libnormvol_plugin.so
%{vlc_plugindir}/audio_filter/libparam_eq_plugin.so
%{vlc_plugindir}/audio_filter/libremap_plugin.so
%{vlc_plugindir}/audio_filter/libscaletempo_pitch_plugin.so
%{vlc_plugindir}/audio_filter/libscaletempo_plugin.so
%{vlc_plugindir}/audio_filter/libsimple_channel_mixer_plugin.so
%{vlc_plugindir}/audio_filter/libspatializer_plugin.so
%{vlc_plugindir}/audio_filter/libstereo_widen_plugin.so
%{vlc_plugindir}/audio_filter/libtospdif_plugin.so
%{vlc_plugindir}/audio_filter/libtrivial_channel_mixer_plugin.so
%{vlc_plugindir}/audio_filter/libugly_resampler_plugin.so
%{vlc_plugindir}/audio_mixer/libfloat_mixer_plugin.so
%{vlc_plugindir}/audio_mixer/libinteger_mixer_plugin.so
%{vlc_plugindir}/audio_output/libadummy_plugin.so
%{vlc_plugindir}/audio_output/libafile_plugin.so
%{vlc_plugindir}/audio_output/libalsa_plugin.so
%{vlc_plugindir}/audio_output/libamem_plugin.so
%{vlc_plugindir}/codec/liba52_plugin.so
%{vlc_plugindir}/codec/libadpcm_plugin.so
%{vlc_plugindir}/codec/libaes3_plugin.so
%{vlc_plugindir}/codec/libaraw_plugin.so
%{vlc_plugindir}/codec/libcc_plugin.so
%{vlc_plugindir}/codec/libcdg_plugin.so
%{vlc_plugindir}/codec/libcvdsub_plugin.so
%{vlc_plugindir}/codec/libdav1d_plugin.so
%{vlc_plugindir}/codec/libddummy_plugin.so
%{vlc_plugindir}/codec/libdvbsub_plugin.so
%{vlc_plugindir}/codec/libedummy_plugin.so
%{vlc_plugindir}/codec/libfaad_plugin.so
%{vlc_plugindir}/codec/libfdkaac_plugin.so
%{vlc_plugindir}/codec/libflac_plugin.so
%{vlc_plugindir}/codec/libg711_plugin.so
%{vlc_plugindir}/codec/libjpeg_plugin.so
%{vlc_plugindir}/codec/liblpcm_plugin.so
%{vlc_plugindir}/codec/libmpg123_plugin.so
%{vlc_plugindir}/codec/liboggspots_plugin.so
%{vlc_plugindir}/codec/libopus_plugin.so
%{vlc_plugindir}/codec/libpng_plugin.so
%{vlc_plugindir}/codec/librawvideo_plugin.so
%{vlc_plugindir}/codec/librtpvideo_plugin.so
%{vlc_plugindir}/codec/libscte18_plugin.so
%{vlc_plugindir}/codec/libscte27_plugin.so
%{vlc_plugindir}/codec/libspdif_plugin.so
%{vlc_plugindir}/codec/libspeex_plugin.so
%{vlc_plugindir}/codec/libspudec_plugin.so
%{vlc_plugindir}/codec/libstl_plugin.so
%{vlc_plugindir}/codec/libsubsdec_plugin.so
%{vlc_plugindir}/codec/libsubstx3g_plugin.so
%{vlc_plugindir}/codec/libsubsusf_plugin.so
%{vlc_plugindir}/codec/libsvcdsub_plugin.so
%{vlc_plugindir}/codec/libt140_plugin.so
%{vlc_plugindir}/codec/libtextst_plugin.so
%{vlc_plugindir}/codec/libtheora_plugin.so
%{vlc_plugindir}/codec/libttml_plugin.so
%{vlc_plugindir}/codec/libtwolame_plugin.so
%{vlc_plugindir}/codec/libuleaddvaudio_plugin.so
%{vlc_plugindir}/codec/libvorbis_plugin.so
%{vlc_plugindir}/codec/libvpx_plugin.so
%{vlc_plugindir}/codec/libwebvtt_plugin.so
%if %{with x264}
%{vlc_plugindir}/codec/libx26410b_plugin.so
%{vlc_plugindir}/codec/libx264_plugin.so
%endif
%if %{with x265}
%{vlc_plugindir}/codec/libx265_plugin.so
%endif
%{vlc_plugindir}/codec/libxwd_plugin.so
%{vlc_plugindir}/control/libdbus_plugin.so
%{vlc_plugindir}/control/libdummy_plugin.so
%{vlc_plugindir}/control/libgestures_plugin.so
%{vlc_plugindir}/control/libhotkeys_plugin.so
%{vlc_plugindir}/control/libmotion_plugin.so
%{vlc_plugindir}/control/libnetsync_plugin.so
%{vlc_plugindir}/control/liboldrc_plugin.so
%{vlc_plugindir}/demux/libadaptive_plugin.so
%{vlc_plugindir}/demux/libaiff_plugin.so
%{vlc_plugindir}/demux/libasf_plugin.so
%{vlc_plugindir}/demux/libau_plugin.so
%{vlc_plugindir}/demux/libavi_plugin.so
%{vlc_plugindir}/demux/libcaf_plugin.so
%{vlc_plugindir}/demux/libdemux_cdg_plugin.so
%{vlc_plugindir}/demux/libdemux_chromecast_plugin.so
%{vlc_plugindir}/demux/libdemux_stl_plugin.so
%{vlc_plugindir}/demux/libdemuxdump_plugin.so
%{vlc_plugindir}/demux/libdiracsys_plugin.so
%{vlc_plugindir}/demux/libdirectory_demux_plugin.so
%{vlc_plugindir}/demux/libes_plugin.so
%{vlc_plugindir}/demux/libflacsys_plugin.so
%{vlc_plugindir}/demux/libh26x_plugin.so
%{vlc_plugindir}/demux/libimage_plugin.so
%{vlc_plugindir}/demux/libmjpeg_plugin.so
%{vlc_plugindir}/demux/libmp4_plugin.so
%{vlc_plugindir}/demux/libmpgv_plugin.so
%{vlc_plugindir}/demux/libnoseek_plugin.so
%{vlc_plugindir}/demux/libnsc_plugin.so
%{vlc_plugindir}/demux/libnsv_plugin.so
%{vlc_plugindir}/demux/libnuv_plugin.so
%{vlc_plugindir}/demux/libogg_plugin.so
%{vlc_plugindir}/demux/libplaylist_plugin.so
%{vlc_plugindir}/demux/libps_plugin.so
%{vlc_plugindir}/demux/libpva_plugin.so
%{vlc_plugindir}/demux/librawaud_plugin.so
%{vlc_plugindir}/demux/librawdv_plugin.so
%{vlc_plugindir}/demux/librawvid_plugin.so
%{vlc_plugindir}/demux/libreal_plugin.so
%{vlc_plugindir}/demux/libsmf_plugin.so
%{vlc_plugindir}/demux/libsubtitle_plugin.so
%{vlc_plugindir}/demux/libtta_plugin.so
%{vlc_plugindir}/demux/libty_plugin.so
%{vlc_plugindir}/demux/libvc1_plugin.so
%{vlc_plugindir}/demux/libvobsub_plugin.so
%{vlc_plugindir}/demux/libvoc_plugin.so
%{vlc_plugindir}/demux/libwav_plugin.so
%{vlc_plugindir}/demux/libxa_plugin.so
%{vlc_plugindir}/keystore/libfile_keystore_plugin.so
%{vlc_plugindir}/keystore/libmemory_keystore_plugin.so
%{vlc_plugindir}/logger/libconsole_logger_plugin.so
%{vlc_plugindir}/logger/libfile_logger_plugin.so
%{vlc_plugindir}/logger/libsd_journal_plugin.so
%{vlc_plugindir}/logger/libsyslog_plugin.so
%{vlc_plugindir}/meta_engine/libfolder_plugin.so
%{vlc_plugindir}/meta_engine/libtaglib_plugin.so
%{vlc_plugindir}/misc/libaddonsfsstorage_plugin.so
%{vlc_plugindir}/misc/libaddonsvorepository_plugin.so
%{vlc_plugindir}/misc/libaudioscrobbler_plugin.so
%{vlc_plugindir}/misc/libdbus_screensaver_plugin.so
%{vlc_plugindir}/misc/libexport_plugin.so
%{vlc_plugindir}/misc/libfingerprinter_plugin.so
%{vlc_plugindir}/misc/libgnutls_plugin.so
%{vlc_plugindir}/misc/liblogger_plugin.so
%{vlc_plugindir}/misc/libstats_plugin.so
%{vlc_plugindir}/misc/libvod_rtsp_plugin.so
%{vlc_plugindir}/misc/libxdg_screensaver_plugin.so
%{vlc_plugindir}/misc/libxml_plugin.so
%{vlc_plugindir}/mux/libmux_asf_plugin.so
%{vlc_plugindir}/mux/libmux_avi_plugin.so
%{vlc_plugindir}/mux/libmux_dummy_plugin.so
%{vlc_plugindir}/mux/libmux_mp4_plugin.so
%{vlc_plugindir}/mux/libmux_mpjpeg_plugin.so
%{vlc_plugindir}/mux/libmux_ogg_plugin.so
%{vlc_plugindir}/mux/libmux_ps_plugin.so
%{vlc_plugindir}/mux/libmux_wav_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_a52_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_av1_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_copy_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_dirac_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_dts_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_flac_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_h264_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_hevc_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_mlp_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_mpeg4audio_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_mpeg4video_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_mpegaudio_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_mpegvideo_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_vc1_plugin.so
%{vlc_plugindir}/services_discovery/libmediadirs_plugin.so
%{vlc_plugindir}/services_discovery/libpodcast_plugin.so
%{vlc_plugindir}/services_discovery/libsap_plugin.so
%{vlc_plugindir}/spu/libaudiobargraph_v_plugin.so
%{vlc_plugindir}/spu/libdynamicoverlay_plugin.so
%{vlc_plugindir}/spu/liblogo_plugin.so
%{vlc_plugindir}/spu/libmarq_plugin.so
%{vlc_plugindir}/spu/libmosaic_plugin.so
%{vlc_plugindir}/spu/libremoteosd_plugin.so
%{vlc_plugindir}/spu/librss_plugin.so
%{vlc_plugindir}/spu/libsubsdelay_plugin.so
%{vlc_plugindir}/stream_filter/libadf_plugin.so
%{vlc_plugindir}/stream_filter/libcache_block_plugin.so
%{vlc_plugindir}/stream_filter/libcache_read_plugin.so
%{vlc_plugindir}/stream_filter/libdecomp_plugin.so
%{vlc_plugindir}/stream_filter/libhds_plugin.so
%{vlc_plugindir}/stream_filter/libinflate_plugin.so
%{vlc_plugindir}/stream_filter/libprefetch_plugin.so
%{vlc_plugindir}/stream_filter/librecord_plugin.so
%{vlc_plugindir}/stream_filter/libskiptags_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_autodel_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_bridge_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_cycle_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_delay_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_description_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_display_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_dummy_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_duplicate_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_es_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_gather_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_mosaic_bridge_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_record_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_rtp_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_setid_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_smem_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_standard_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_stats_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_transcode_plugin.so
%{vlc_plugindir}/text_renderer/libtdummy_plugin.so
%exclude %{vlc_plugindir}/video_chroma/libswscale_plugin.so
%{vlc_plugindir}/video_chroma/*.so
%exclude %{vlc_plugindir}/video_filter/libpostproc_plugin.so
%{vlc_plugindir}/video_filter/*.so
%{vlc_plugindir}/video_output/libfb_plugin.so
%{vlc_plugindir}/video_output/libvdummy_plugin.so
%{vlc_plugindir}/video_output/libvmem_plugin.so
%{vlc_plugindir}/video_output/libyuv_plugin.so

%files plugins-extra
%{vlc_plugindir}/access/libaccess_mtp_plugin.so
%{vlc_plugindir}/access/libaccess_srt_plugin.so
%{vlc_plugindir}/access/libcdda_plugin.so
%if %{with asdcp}
%{vlc_plugindir}/access/libdcp_plugin.so
%endif
%{vlc_plugindir}/access/libdvb_plugin.so
%{vlc_plugindir}/access/libdvdnav_plugin.so
%{vlc_plugindir}/access/libdvdread_plugin.so
%{vlc_plugindir}/access/liblibbluray_plugin.so
%{vlc_plugindir}/access/liblive555_plugin.so
%{vlc_plugindir}/access/libnfs_plugin.so
%{vlc_plugindir}/access/libsftp_plugin.so
%{vlc_plugindir}/access/liblinsys_hdsdi_plugin.so
%{vlc_plugindir}/access/liblinsys_sdi_plugin.so
%{vlc_plugindir}/access/libv4l2_plugin.so
%{vlc_plugindir}/access/libxcb_screen_plugin.so
%{vlc_plugindir}/access_output/libaccess_output_srt_plugin.so
%{vlc_plugindir}/audio_filter/libmad_plugin.so
%{vlc_plugindir}/audio_filter/libsamplerate_plugin.so
%{vlc_plugindir}/audio_filter/libsoxr_plugin.so
%{vlc_plugindir}/audio_filter/libspatialaudio_plugin.so
%{vlc_plugindir}/audio_filter/libspeex_resampler_plugin.so
%{vlc_plugindir}/codec/libaom_plugin.so
%{vlc_plugindir}/codec/libaribsub_plugin.so
%if %{with daala}
%{vlc_plugindir}/codec/libdaala_plugin.so
%endif
%{vlc_plugindir}/codec/libdca_plugin.so
%{vlc_plugindir}/codec/libkate_plugin.so
%{vlc_plugindir}/codec/liblibass_plugin.so
%{vlc_plugindir}/codec/liblibmpeg2_plugin.so
%if %{with vpl}
%{vlc_plugindir}/codec/libqsv_plugin.so
%endif
%if %{with schro}
%{vlc_plugindir}/codec/libschroedinger_plugin.so
%endif
%if %{with sdl}
%{vlc_plugindir}/codec/libsdl_image_plugin.so
%endif
%{vlc_plugindir}/codec/libzvbi_plugin.so
%if %{with lirc}
%{vlc_plugindir}/control/liblirc_plugin.so
%endif
%{vlc_plugindir}/demux/libgme_plugin.so
%{vlc_plugindir}/demux/libmpc_plugin.so
%{vlc_plugindir}/demux/libmkv_plugin.so
%{vlc_plugindir}/demux/libmod_plugin.so
%{vlc_plugindir}/demux/libts_plugin.so
%{vlc_plugindir}/mux/libmux_ts_plugin.so
%{vlc_plugindir}/services_discovery/libavahi_plugin.so
%{vlc_plugindir}/services_discovery/libmicrodns_plugin.so
%{vlc_plugindir}/services_discovery/libmtp_plugin.so
%{vlc_plugindir}/services_discovery/libupnp_plugin.so
%{vlc_plugindir}/services_discovery/libudev_plugin.so
%{vlc_plugindir}/stream_extractor/libarchive_plugin.so
%{vlc_plugindir}/stream_filter/libaribcam_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_chromecast_plugin.so
%{vlc_plugindir}/text_renderer/libfreetype_plugin.so
%{vlc_plugindir}/video_output/libaa_plugin.so
%{vlc_plugindir}/video_output/libcaca_plugin.so

%if %{with crystalhd}
%files plugin-crystalhd
%{vlc_plugindir}/codec/libcrystalhd_plugin.so
%endif

%files plugin-ffmpeg
%{vlc_plugindir}/access/libavio_plugin.so
%{vlc_plugindir}/codec/libavcodec_plugin.so
%{vlc_plugindir}/codec/libvaapi_drm_plugin.so
%{vlc_plugindir}/codec/libvaapi_plugin.so
%{vlc_plugindir}/demux/libavformat_plugin.so
%{vlc_plugindir}/packetizer/libpacketizer_avparser_plugin.so
%{vlc_plugindir}/stream_out/libstream_out_chromaprint_plugin.so
%{vlc_plugindir}/vdpau/libvdpau_avcodec_plugin.so
%{vlc_plugindir}/video_chroma/libswscale_plugin.so
%{vlc_plugindir}/video_filter/libpostproc_plugin.so

%files plugin-fluidsynth
%{vlc_plugindir}/codec/libfluidsynth_plugin.so

%files plugin-gnome
%{vlc_plugindir}/keystore/libsecret_plugin.so

%files plugin-gstreamer
%{vlc_plugindir}/codec/libgstdecode_plugin.so

%if %{with ieee1394}
%files plugin-ieee1394
%{vlc_plugindir}/access/libdc1394_plugin.so
%{vlc_plugindir}/access/libdv1394_plugin.so
%endif

%files plugin-jack
%{vlc_plugindir}/access/libaccess_jack_plugin.so
%{vlc_plugindir}/audio_output/libjack_plugin.so

%files plugin-kde
%{vlc_plugindir}/keystore/libkwallet_plugin.so

%files plugin-lua
%{_libdir}/vlc/lua/
%{vlc_plugindir}/lua/
%{_datadir}/vlc/lua/

%files plugin-notify
%{vlc_plugindir}/notify/libnotify_plugin.so

%if %{with opencv}
%files plugin-opencv
%{vlc_plugindir}/video_filter/libopencv_example_plugin.so
%{vlc_plugindir}/video_filter/libopencv_wrapper_plugin.so
%endif

%files plugin-pulseaudio
%{_libdir}/vlc/libvlc_pulse.so*
%{vlc_plugindir}/access/libpulsesrc_plugin.so
%{vlc_plugindir}/audio_output/libpulse_plugin.so
%{vlc_plugindir}/services_discovery/libpulselist_plugin.so

%files plugin-rdp
%{vlc_plugindir}/access/librdp_plugin.so

%files plugin-samba
%{vlc_plugindir}/access/libsmb_plugin.so

%files plugin-svg
%{vlc_plugindir}/codec/libsvgdec_plugin.so
%{vlc_plugindir}/text_renderer/libsvg_plugin.so

%files plugins-video-out
%{_libdir}/vlc/libvlc_vdpau.so*
%{_libdir}/vlc/libvlc_xcb_events.so*
%{vlc_plugindir}/control/libxcb_hotkeys_plugin.so
%{vlc_plugindir}/services_discovery/libxcb_apps_plugin.so
%{vlc_plugindir}/vaapi/*.so
%exclude %{vlc_plugindir}/vdpau/libvdpau_avcodec_plugin.so
%{vlc_plugindir}/vdpau/*.so
%{vlc_plugindir}/video_output/libegl_wl_plugin.so
%{vlc_plugindir}/video_output/libegl_x11_plugin.so
%{vlc_plugindir}/video_output/libflaschen_plugin.so
%{vlc_plugindir}/video_output/libgl_plugin.so
%{vlc_plugindir}/video_output/libglconv_vaapi_drm_plugin.so
%{vlc_plugindir}/video_output/libglconv_vaapi_wl_plugin.so
%{vlc_plugindir}/video_output/libglconv_vaapi_x11_plugin.so
%{vlc_plugindir}/video_output/libglconv_vdpau_plugin.so
%{vlc_plugindir}/video_output/libgles2_plugin.so
%{vlc_plugindir}/video_output/libglx_plugin.so
%{vlc_plugindir}/video_output/libwl_shell_plugin.so
%{vlc_plugindir}/video_output/libwl_shm_plugin.so
%{vlc_plugindir}/video_output/libxcb_window_plugin.so
%{vlc_plugindir}/video_output/libxcb_x11_plugin.so
%{vlc_plugindir}/video_output/libxcb_xv_plugin.so
%{vlc_plugindir}/video_output/libxdg_shell_plugin.so
%{vlc_plugindir}/video_splitter/*.so

%files plugin-visualization
%{vlc_plugindir}/visualization/*.so

%files plugin-vnc
%{vlc_plugindir}/access/libvnc_plugin.so

%files devel
%dir %{_includedir}/vlc
%{_includedir}/vlc/*.h
%{_includedir}/vlc/plugins/
%{_libdir}/libvlc.so
%{_libdir}/libvlccore.so
%{_libdir}/pkgconfig/libvlc.pc
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_rpmmacrodir}/macros.vlc

%changelog
* Fri Dec 19 2025 - 2:3.0.21-1
- Initial package
