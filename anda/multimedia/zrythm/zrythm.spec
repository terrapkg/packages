%global v v1.0.0

Name:           zrythm
Version:        %(echo %v | sed 's@-@~@g' | sed 's@^v@@')
Release:        2%?dist
Summary:        Highly automated and intuitive digital audio workstation
License:        AGPL-3.0-or-later
Packager:       madonuko <mado@fyralabs.com>
URL:            https://www.zrythm.org/
Source0:        https://gitlab.zrythm.org/zrythm/zrythm/-/archive/%v/zrythm-%v.tar.gz

# https://github.com/OpenMandrivaAssociation/zrythm/blob/master/zrythm.spec

BuildRequires: automake
BuildRequires: libappstream-glib
BuildRequires: mold
BuildRequires: git
BuildRequires: gettext
BuildRequires: python
BuildRequires: sed
BuildRequires: sassc
BuildRequires: libbacktrace-nightly-devel
BuildRequires: boost-devel
BuildRequires: (ffmpeg-free-devel or ffmpeg-devel)
BuildRequires: ladspa-devel
BuildRequires: graphviz-devel
BuildRequires: pkgconfig(carla-host-plugin) >= 2.6.0
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(audec)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libchromaprint)
BuildRequires: pkgconfig(libcurl)
#BuildRequires: pkgconfig(libfl)
BuildRequires: libfl-devel
# ^ maybe?
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libsass)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(reproc)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(rtaudio) >= 5.1.0
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libxdot)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(pypandoc)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lsp-dsp-lib)
BuildRequires: pkgconfig(vamp)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(zix-0)
BuildRequires: pkgconfig(yyjson)
BuildRequires: pkgconfig(epoxy)
BuildRequires: libstdc++
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-static
BuildRequires: libxml2
BuildRequires: jq-devel
BuildRequires: help2man
BuildRequires: texi2html
BuildRequires: xdg-utils
BuildRequires: meson
BuildRequires: guile22
BuildRequires: flex
Requires:      ladspa
Requires:      lilv
Requires:      lv2
Requires:      fftw
Requires:      liblsp-dsp

%description
Zrythm is a digital audio workstation designed to be
featureful and easy to use.
It offers streamlined editing workflows with flexible
tools, limitless automation capabilities, powerful
mixing features, chord assistance and support for
various plugin and file formats.

%pkg_completion -Bf

%prep
%autosetup -n %name-%v


%build
CFLAGS=$(echo "$CFLAGS -fuse-ld=mold -Wno-incompatible-pointer-types" | sed -E "s@\b-Werror\b@@")
CXXFLAGS=$(echo "$CFLAGS -fuse-ld=mold" | sed -E "s@\b-Werror\b@@")

%meson \
       -Drtmidi=enabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Dlsp_dsp=disabled \
       -Dgraphviz=enabled \
       --buildtype=release
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc README.md
%license COPYING
%_bindir/zrythm
%_bindir/zrythm_valgrind
%_bindir/zrythm_launch
%_bindir/zrythm_gdb
%_libdir/zrythm/carla/
%_libdir/zrythm/lv2
%_datadir/applications/org.zrythm.Zrythm.desktop
%_datadir/fonts/%name
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/scalable/apps/org.zrythm.Zrythm.svg
%_datadir/%name/
%_datadir/mime/packages/org.zrythm.Zrythm-mime.xml
%_datadir/metainfo/org.zrythm.Zrythm.appdata.xml
%_mandir/man1/zrythm.1.*
