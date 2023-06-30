# https://pkgs.rpmfusion.org/cgit/free/HandBrake.git/tree/HandBrake.spec
%global commit0 04413a27e6d616cddd98c2c6468aca2bf91b87b5
%global commit_date %(date '+%Y%m%d')
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}
%global pkg HandBrake

# Build with "--without ffmpeg" or enable this to use bundled libAV
# instead of system FFMpeg libraries.
#global _without_ffmpeg 1

%ifarch i686 x86_64
%global _with_asm 1
%global _with_vpl 1
%endif

%global desktop_id fr.handbrake.ghb

Name:           terra-HandBrake
Version:        1.6.1
Release:        1%?dist
Summary:        An open-source multiplatform video transcoder
License:        GPL-2.0-or-later
URL:            https://handbrake.fr/

%if 0%{?tag:1}
#Source0:        https://github.com/%pkg/%pkg/releases/download/%version/%pkg-%version-source.tar.bz2
Source1:        https://github.com/%pkg/%pkg/releases/download/%version/%pkg-%version-source.tar.bz2.sig
# import from https://handbrake.fr/openpgp.php or https://github.com/HandBrake/HandBrake/wiki/OpenPGP
# gpg2 --export --export-options export-minimal 1629C061B3DDE7EB4AE34B81021DB8B44E4A8645 > gpg-keyring-1629C061B3DDE7EB4AE34B81021DB8B44E4A8645.gpg
Source2:        gpg-keyring-1629C061B3DDE7EB4AE34B81021DB8B44E4A8645.gpg
%else
#Source0:        https://github.com/%pkg/%pkg/archive/%commit0.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

%{?_without_ffmpeg:Source10:       https://libav.org/releases/libav-12.tar.gz}

# Pass strip tool override to gtk/configure
Patch0:         %pkg-nostrip.patch
# Don't link with libva unnecessarily
Patch1:         %pkg-no-libva.patch
# Don't link with fdk_aac unnecessarily
Patch2:         %pkg-no-fdk_aac.patch
# Fix build on non-x86 (without nasm)
Patch3:         %pkg-no-nasm.patch
# Patch from Gentoo
Patch4:         %pkg-x265-link.patch

BuildRequires:  a52dec-devel >= 0.7.4
BuildRequires:  cmake
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
%if 0%{?tag:1}
BuildRequires:  gnupg2
%endif
BuildRequires:  libappstream-glib
%{!?_without_ffmpeg:BuildRequires:  ffmpeg-free-devel >= 3.5}
# Should be >= 2.6:
BuildRequires:  freetype-devel >= 2.4.11
# Should be >= 0.19.7:
BuildRequires:  fribidi-devel >= 0.19.4
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  intltool
BuildRequires:  jansson-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  lame-devel >= 3.98
BuildRequires:  libappindicator-gtk3-devel
# Should be >= 0.13.2:
BuildRequires:  libass-devel >= 0.13.1
BuildRequires:  libbluray-devel >= 0.9.3
BuildRequires:  libdav1d-devel
BuildRequires:  libdrm-devel
BuildRequires:  libdvdnav-devel >= 5.0.1
BuildRequires:  libdvdread-devel >= 5.0.0
BuildRequires:  libgudev-devel
%if 0%{?_with_vpl:1}
BuildRequires:  intel-mediasdk-devel
BuildRequires:  oneVPL-devel
BuildRequires:  libva-devel
%endif
BuildRequires:  libmpeg2-devel >= 0.5.1
BuildRequires:  libnotify-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
# Should be >= 1.5:
BuildRequires:  libvpx-devel >= 1.3
BuildRequires:  make
BuildRequires:  meson
%if 0%{?_with_asm:1}
BuildRequires:  nasm
%endif
BuildRequires:  numactl-devel
BuildRequires:  nv-codec-headers
BuildRequires:  opus-devel
BuildRequires:  python3
BuildRequires:  speex-devel
BuildRequires:  svt-av1-devel
BuildRequires:  x264-devel >= 0.148
BuildRequires:  x265-devel >= 1.9
BuildRequires:  xz-devel
BuildRequires:  zimg-devel
BuildRequires:  git
BuildRequires:  vulkan-loader

Requires:       hicolor-icon-theme
# needed for reading encrypted DVDs
%{?fedora:Recommends:     libdvdcss%_isa}
Obsoletes:      HandBrake-cli < %version-%release
Provides:       HandBrake-cli = %version-%release
Provides:       handbrake =  %version-%release

%description
%pkg is a general-purpose, free, open-source, cross-platform, multithreaded
video transcoder software application. It can process most common multimedia
files and any DVD or Bluray sources that do not contain any kind of copy
protection.

This package contains the command line version of the program.

%package gui
Summary:        An open-source multiplatform video transcoder (GUI)
Provides:       handbrake-gui = %version-%release
Requires:       hicolor-icon-theme
# needed for reading encrypted DVDs
%{?fedora:Recommends:     libdvdcss%_isa}
# needed for live preview
%{?fedora:Recommends:     gstreamer1-plugins-good%_isa}

%description gui
%pkg is a general-purpose, free, open-source, cross-platform, multithreaded
video transcoder software application. It can process most common multimedia
files and any DVD or Bluray sources that do not contain any kind of copy
protection.

This package contains the main program with a graphical interface.

%prep
%if 0%{?tag:1}
#gpgv2 --keyring %{S:2} %{S:1} %{S:0}
%endif
#setup -q %%{!?tag:-n HandBrake-%commit0}%%{?tag:-n HandBrake-%version}
git clone https://github.com/%pkg/%pkg
cd %pkg
git checkout %{!?tag:%commit0}%{?tag:%version}
%patch -P0 -p1
%if 0%!?_with_vpl
%patch -P1 -p1
%endif
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# Use system libraries in place of bundled ones
for module in a52dec fdk-aac %{!?_without_ffmpeg:ffmpeg} libdav1d libdvdnav libdvdread libbluray %{?_with_vpl:libmfx libvpl} nvenc libvpx svt-av1 x265; do
    sed -i -e "/MODULES += contrib\/$module/d" make/include/main.defs
done

# Fix desktop file
sed -i -e 's/%desktop_id.svg/%desktop_id/g' gtk/src/%desktop_id.desktop

%build
cd %pkg
echo "HASH=%commit0" > version.txt
echo "SHORTHASH=%shortcommit0" >> version.txt
echo "DATE=$(date "+%Y-%m-%d %T" -d %date)" >> version.txt
%if 0%{?tag:1}
echo "TAG=%version" >> version.txt
echo "TAG_HASH=%commit0" >> version.txt
%endif

# By default the project is built with optimizations for speed and no debug.
# Override configure settings by passing RPM_OPT_FLAGS and disabling preset
# debug options.
echo "GCC.args.O.speed = %optflags -I%_includedir/vpl -I%_includedir/ffmpeg -ldl -lx265 %{?_with_vpl:-lvpl}" > custom.defs
echo "GCC.args.g.none = " >> custom.defs

# Not an autotools configure script.
./configure \
    --build build \
    --prefix=%_prefix \
    --debug=std \
    --strip=%_bindir/echo \
    --verbose \
    --disable-df-fetch \
    --disable-df-verify \
    --disable-gtk-update-checks \
    %{?_with_asm:--enable-asm} \
    --enable-x265 \
    --disable-numa \
    --enable-fdk-aac \
    %{?_with_vpl:--enable-qsv}

%make_build -C build V=1

%install
cd %pkg
%make_install -C build

# Desktop file, icons and AppStream metadata from FlatPak build (more complete)
rm -f %buildroot%_datadir/applications/ghb.desktop \
    %buildroot%_datadir/icons/hicolor/scalable/apps/hb-icon.svg

install -Dpm644 gtk/src/%desktop_id.desktop \
    %buildroot%_datadir/applications/%desktop_id.desktop
install -Dpm644 gtk/src/%desktop_id.svg \
    %buildroot%_datadir/icons/hicolor/scalable/apps/%desktop_id.svg

%find_lang ghb

%check
desktop-file-validate %buildroot%_datadir/applications/%desktop_id.desktop
appstream-util validate-relax --nonet %buildroot%_metainfodir/%desktop_id.metainfo.xml

%files -f ghb.lang gui
%license COPYING
%doc AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%_bindir/ghb
%_metainfodir/%desktop_id.metainfo.xml
%_datadir/applications/%desktop_id.desktop
%_datadir/icons/hicolor/scalable/apps/%desktop_id.svg

%files
%license COPYING
%doc AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%_bindir/HandBrakeCLI

%changelog
%autochangelog
