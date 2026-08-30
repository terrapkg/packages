%global commit0 2e91369bae27841e0ffdcbe2e0fac2aaa7e779cf
%global date 20231008
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

%global desktop_id fr.handbrake.ghb

Name:           HandBrake
Version:        1.9.0
Release:        2%{?dist}
# RPMFusion's Handbrake builds link against an older version of x265, so we
# want to force upgrades to this package.
Epoch:          1
Summary:        An open-source multiplatform video transcoder
License:        GPLv2+
URL:            http://handbrake.fr/

%if 0%{?tag:1}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

# Adjust dependencies when using system libraries:
Patch0:         %{name}-deps.patch

BuildRequires:  AMF-devel
BuildRequires:  appstream
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel >= 2.4.11
BuildRequires:  fribidi-devel >= 0.19.4
BuildRequires:  gcc-c++
BuildRequires:  harfbuzz-devel >= 1.3.2
BuildRequires:  jansson-devel >= 2.10
BuildRequires:  libappstream-glib
BuildRequires:  libass-devel >= 0.13.4
BuildRequires:  libdav1d-devel >= 0.3.0
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  libsamplerate-devel >= 0.1.8
BuildRequires:  libtool
BuildRequires:  libva-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  nv-codec-headers >= 11
BuildRequires:  patch
BuildRequires:  pkgconfig(dovi)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(gio-2.0) >= 2.68
BuildRequires:  pkgconfig(glib-2.0) >= 2.68
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.68
BuildRequires:  pkgconfig(gthread-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(x264)
BuildRequires:  pkgconfig(x265)
BuildRequires:  python3
BuildRequires:  tar
BuildRequires:  wget
BuildRequires:  zlib-devel
BuildRequires:  zimg-devel >= 3.0.1

%ifarch x86_64
BuildRequires:  libvpl-devel
%endif

%description
%{name} is a general-purpose, free, open-source, cross-platform, multithreaded
video transcoder software application. It can process most common multimedia
files and any DVD or Bluray sources that do not contain any kind of copy
protection.

%package gui
Summary:        An open-source multiplatform video transcoder (GUI)
Provides:       handbrake-gui = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       handbrake = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-plugins-good%{_isa}
Requires:       hicolor-icon-theme
Requires:       libdvdcss%{_isa}

%description gui
%{name} is a general-purpose, free, open-source, cross-platform, multithreaded
video transcoder software application. It can process most common multimedia
files and any DVD or Bluray sources that do not contain any kind of copy
protection.

This package contains the main program with a graphical interface.

%package cli
Summary:        An open-source multiplatform video transcoder (CLI)
Provides:       handbrake-cli = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libdvdcss%{_isa}

%description cli
%{name} is a general-purpose, free, open-source, cross-platform, multithreaded
video transcoder software application. It can process most common multimedia
files and any DVD or Bluray sources that do not contain any kind of copy
protection.

This package contains the command line version of the program.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif
mkdir -p download build/contrib/include

# Use system libraries in place of bundled ones
for module in fdk-aac ffmpeg libdav1d libdovi libdvdnav libdvdread libbluray libvpl nvenc svt-av1 x265 zimg; do
    sed -i -e "/MODULES += contrib\/$module/d" make/include/main.defs
done

%build
echo "HASH=%{commit0}" > version.txt
echo "SHORTHASH=%{shortcommit0}" >> version.txt
echo "DATE=$(date "+%Y-%m-%d %T")" >> version.txt
%if 0%{?tag:1}
echo "TAG=%{tag}" >> version.txt
echo "TAG_HASH=%{commit0}" >> version.txt
%endif

# By default the project is built with optimizations for speed and no debug.
# Override configure settings by passing RPM_OPT_FLAGS and disabling preset
# debug options.
# These plus "--no-harden" at configure time set proper compiler flags:
cat > custom.defs << EOF
GCC.args.c_std =
GCC.args.cxx_std =
GCC.args.O.speed = %build_cflags -I%{_includedir}/vpl
GCC.args.g.none =
GCC.args.strip =
EOF

# Not an autotools configure script:
./configure \
    --build %{_build} \
    --disable-df-fetch \
    --disable-df-verify \
    --disable-update-checks \
    --enable-asm \
    --enable-fdk-aac \
    --enable-ffmpeg-aac \
    --enable-gst \
    --enable-libdovi \
    --enable-numa \
    --enable-nvdec \
    --enable-nvenc \
%ifarch x86_64
    --enable-qsv \
%endif
    --enable-vce \
    --enable-x265 \
    --force \
    --no-harden \
    --prefix=%{_prefix}

%make_build -C %{_build}

%install
%make_install -C %{_build}

%find_lang ghb

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{desktop_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{desktop_id}.metainfo.xml

%files -f ghb.lang gui
%license COPYING
%doc AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%{_bindir}/ghb
%{_metainfodir}/%{desktop_id}.metainfo.xml
%{_datadir}/applications/%{desktop_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{desktop_id}.svg

%files cli
%license COPYING
%doc AUTHORS.markdown NEWS.markdown README.markdown THANKS.markdown
%{_bindir}/HandBrakeCLI

%autochangelog
