# ? https://src.fedoraproject.org/rpms/retroarch/blob/rawhide/f/retroarch.spec

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}
# Please fix upstream this if you need it and no downstream Fedora patch
ExcludeArch: s390x

# Free/Freeworld/Non-Free version
%bcond_with freeworld
%bcond_without nonfree

%global appname retroarch
%global uuid    org.libretro.RetroArch

# Freeworld package
%if %{with freeworld}
%global p_suffix    -freeworld
%global sum_suffix  (Freeworld version)
%else
%global p_suffix    %{nil}
%global sum_suffix  %{nil}
%endif

%global short_url https://github.com/libretro

Name:           %{appname}%{?p_suffix}
Version:        1.22.0
%global major_ver %(echo %version | sed -E 's/\.\d+$//')
Release:        %autorelease
Summary:        Cross-platform, sophisticated frontend for the libretro API %{?sum_suffix}

# CC-BY:        Assets
# CC0:          AppData manifest
# MIT:          Libretro's core info
#               Joypad Autoconfig Files
#
# Apache License (v2.0)
# ------------------------------------
# deps/SPIRV-Cross/
# retroarch-assets/xmb/flatui/
# deps/glslang/glslang/
# gfx/include/vulkan/
#
# Creative Commons Attribution Public License (v4.0)
# -----------------------------------------------------------------
# retroarch-assets/rgui/wallpaper/
#
# Creative Commons Attribution-NonCommercial Public License (v3.0)
# -------------------------------------------------------------------------------
# retroarch-assets/sounds/
#
# Creative Commons Attribution-ShareAlike Public License (v3.0)
# ----------------------------------------------------------------------------
# retroarch-assets/rgui/wallpaper/
#
# Expat License
# ----------------------------
# libretro-common/glsym/
#
# GNU General Public License (v2)
# ----------------------------------------------
# memory/ngc/ssaram.c
#
# GNU Lesser General Public License
# ------------------------------------------------
# memory/neon/memcpy-neon.S
#
# SIL Open Font License
# ------------------------------------
# retroarch-assets/xmb/automatic/
# retroarch-assets/xmb/neoactive/
# retroarch-assets/xmb/retroactive/
#
# BSD 2-clause "Simplified" License
# ---------------------------------
# cores/
# gfx/
# libretro-common/
#
# BSD 2-clause "Simplified" License GPL (v2 or later)
# ---------------------------------------------------
# gfx/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# deps/discord-rpc/
# deps/glslang/
# deps/ibxm/
# gfx/
# libretro-common/
#
License:        GPL-3.0-or-later and GPL-2.0-only and CC-BY-3.0 and CC-BY-4.0 and CC0-1.0 and BSD-2-Clause and BSD-3-Clause and Apache-2.0 and MIT

URL:            https://www.libretro.com/
Packager:       madonuko <mado@fyralabs.com>
Source0:        %{short_url}/RetroArch/archive/v%{version}/%{appname}-%{version}.tar.gz

# Assets
Source1:        %{short_url}/%{appname}-assets/archive/v%{version}/%{appname}-assets-%{version}.tar.gz

# AppData manifest
# Upstreamed so should be easier now to maintain and automate updates for both
# Fedora and RPM Fusion repo.  There is still UUID inconsistency but upstream
# notified.  Keep old one for fallback.
# * https://github.com/libretro/RetroArch/pull/13113
#
# * https://github.com/flathub/org.libretro.RetroArch/blob/master/org.libretro.RetroArch.appdata.xml
Source2:        https://raw.githubusercontent.com/flathub/%{uuid}/19f5be928262256f42644dc0350cee1a5d9b3840/%{uuid}.appdata.xml

# Libretro's core info
Source3:        %{short_url}/libretro-core-info/archive/v%{version}/libretro-core-info-%{version}.tar.gz

# Joypad Autoconfig Files
Source4:        %{short_url}/%{appname}-joypad-autoconfig/archive/v%{version}/%{appname}-joypad-autoconfig-%{version}.tar.gz

# Database files (cheatcode, content data, cursors)
Source5:        %{short_url}/libretro-database/archive/v%{version}/libretro-database-%{version}.tar.gz

# Script for enabling network access which allows downloading more libretro
# cores
Source10:       %{name}-enable-network-access.sh

Source11:       README.fedora.md

Patch:          0001-use_system_flac.patch
Patch:          0003_use_system_zstd.patch

# Support for newer glslang versions without SPIRV and HLSL libraries
# https://github.com/libretro/RetroArch/pull/17563
Patch:          https://github.com/libretro/RetroArch/pull/17563.patch#/0002-Support-for-newer-glslang-versions-without-SPIRV-and-HLSL-libraries.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 7
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  systemd-devel

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  stb_image-static
BuildRequires:  stb_rect_pack-static
BuildRequires:  stb_truetype-static

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6Concurrent) >= 6.2
BuildRequires:  pkgconfig(Qt6Core) >= 6.2
BuildRequires:  pkgconfig(Qt6Gui) >= 6.2
BuildRequires:  pkgconfig(Qt6Network) >= 6.2
BuildRequires:  pkgconfig(Qt6Widgets) >= 6.2
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)

%if %{with freeworld}
# Available in Freeworld repo
BuildRequires:  ffmpeg-devel
# Since F36 ffmpeg-free available in official repos
%else
%if 0%{?fedora} >= 37
BuildRequires:  ffmpeg-free-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavdevice-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  libswscale-free-devel
%endif
%endif
%if %{with nonfree}
# Available in Non-Free repo
BuildRequires:  Cg
BuildRequires:  libCg
BuildRequires:  xv
%endif

Requires:       perl(Net::DBus)
Requires:       perl(X11::Protocol)

Recommends:     %{name}-assets              >= %{?epoch:%{epoch}:}%{major_ver}
Recommends:     %{name}-database            >= %{?epoch:%{epoch}:}%{major_ver}
Recommends:     %{name}-filters%{?_isa}     >= %{?epoch:%{epoch}:}%{major_ver}
Recommends:     gamemode
Recommends:     libretro-beetle-ngp
Recommends:     libretro-beetle-pce-fast
Recommends:     libretro-beetle-vb
Recommends:     libretro-beetle-wswan
Recommends:     libretro-bsnes-mercury
Recommends:     libretro-desmume2015
Recommends:     libretro-gambatte
Recommends:     libretro-gw
Recommends:     libretro-handy
Recommends:     libretro-mgba
Recommends:     libretro-nestopia
Recommends:     libretro-pcsx-rearmed
Recommends:     libretro-prosystem
Recommends:     libretro-stella2014
%if %{with freeworld}
# Non-Free cores
# * Dummy for future
%endif

# Provides:       bundled(7zip) = 19.00
Provides:       bundled(discord-rpc)
Provides:       bundled(dr)
Provides:       bundled(ibxm)

# https://github.com/libretro/RetroArch/issues/8153
Provides:       bundled(lua) = 5.3.6

Provides:       bundled(rcheevos) = 12.1
Provides:       bundled(SPIRV-Cross)
# Unbundling this in the manner of the other stb libraries does not work.
Provides:       bundled(stb_vorbis)

%global _description %{expand:
RetroArch is the reference frontend for the libretro API. Popular examples of
implementations for this API includes video game system emulators and game
engines as well as more generalized 3D programs. These programs are instantiated
as dynamic libraries. We refer to these as "libretro cores".

libretro is an API that exposes generic audio/video/input callbacks. A frontend
for libretro (such as RetroArch) handles video output, audio output, input and
application lifecycle. A libretro core written in portable C or C++ can run
seamlessly on many platforms with very little to no porting effort.

While RetroArch is the reference frontend for libretro, several other projects
have used the libretro interface to include support for emulators and/or game
engines. libretro is completely open and free for anyone to use.

For how to download and install more libretro cores please read included
README.fedora.md file.}

%description %{_description}


# Assets package
%package        assets
Summary:        Assets needed for RetroArch - e.g. menu drivers, etc.
BuildArch:      noarch

Requires:       %{name} >= %{?epoch:%{epoch}:}%{major_ver}

# RetroArch relies heavily on built-in fonts. There's no proper way to use system
# fonts without dirty patching each theme.
Provides:       bundled(inter-ui-fonts)
Provides:       bundled(metrophobic-fonts)
Provides:       bundled(sf-atarian-system-fonts)
Provides:       bundled(titilium-web-fonts)

%description    assets
The retroarch-assets repository is the home of the user interface elements used
to generate the various User Experience (UX) environments. The UX environments
are referred to as "menu drivers" and you can switch between environments on
most platforms at any time.


# Filters package
%package        filters
Summary:        Audio and video filters for %{name}

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    filters
Audio and video filters for %{name}.


# Database package
%package        database
Summary:        Database files (cheatcode, content data, cursors) for %{name}
BuildArch:      noarch

Requires:       %{name} >= %{?epoch:%{epoch}:}%{major_ver}

%description    database
Repository containing cheatcode files, content data files, etc.


# Devel package
%package        devel
Summary:        Development files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
libretro.h is a simple API that allows for the creation of games and emulators.


%prep
%autosetup -n RetroArch-%{version} -S git
%setup -n RetroArch-%{version} -q -D -T -a1
%setup -n RetroArch-%{version} -q -D -T -a3
%setup -n RetroArch-%{version} -q -D -T -a4
%setup -n RetroArch-%{version} -q -D -T -a5

# Unbundling
pushd deps
rm -rf                      \
        7zip                \
        bearssl-0.6         \
        glslang             \
        libfat              \
        libFLAC             \
        libiosuhax          \
        libvita2d           \
        libz                \
        peglib              \
        pthreads            \
        wayland-protocols   \
        zstd                \
        %{nil}
popd
for lib in image rect_pack truetype
do
  ln -svf /usr/include/stb/stb_${lib}.h deps/stb/stb_${lib}.h
done

# * Not part of the 'mbedtls' upstream source
find deps/mbedtls/ ! -name 'cacert.h' -type f -exec rm -f {} +

# Use system assets, libretro cores, libretro's core info and audio/video,
# filters, database files (cheatcode, content data, cursors)
sed -e 's|# libretro_directory =|libretro_directory = %{_libdir}/libretro/|g' \
    -i retroarch.cfg
%if %{with freeworld}
sed -e 's|# assets_directory =|assets_directory = %{_datadir}/libretro/assets-freeworld/|g'                 \
    -e 's|# video_filter_dir =|video_filter_dir = %{_libdir}/retroarch/filters/video-freeworld/|g'          \
    -e 's|# audio_filter_dir =|audio_filter_dir = %{_libdir}/retroarch/filters/audio-freeworld/|g'          \
    -e 's|# libretro_info_path =|libretro_info_path = %{_datadir}/libretro/info-freeworld/|g'               \
    -e 's|# joypad_autoconfig_dir =|joypad_autoconfig_dir = %{_datadir}/libretro/autoconfig-freeworld/|g'   \
    -e 's|# content_database_path =|content_database_path = %{_datadir}/libretro/database-freeworld/rdb/|g' \
    -e 's|# cheat_database_path =|cheat_database_path = %{_datadir}/libretro/database-freeworld/cht/|g'     \
    -e 's|# cursor_directory =|cursor_directory = %{_datadir}/libretro/database-freeworld/cursors/|g'       \
%else
sed -e 's|# assets_directory =|assets_directory = %{_datadir}/libretro/assets/|g'                   \
    -e 's|# video_filter_dir =|video_filter_dir = %{_libdir}/retroarch/filters/video/|g'            \
    -e 's|# audio_filter_dir =|audio_filter_dir = %{_libdir}/retroarch/filters/audio/|g'            \
    -e 's|# libretro_info_path =|libretro_info_path = %{_datadir}/libretro/info/|g'                 \
    -e 's|# joypad_autoconfig_dir =|joypad_autoconfig_dir = %{_datadir}/libretro/autoconfig/|g'     \
    -e 's|# content_database_path =|content_database_path = %{_datadir}/libretro/database/rdb/|g'   \
    -e 's|# cheat_database_path =|cheat_database_path = %{_datadir}/libretro/database/cht/|g'       \
    -e 's|# cursor_directory =|cursor_directory = %{_datadir}/libretro/database/cursors/|g'         \
%endif
    -i retroarch.cfg

# Disable online update feature due security reasons
sed -e 's|# menu_show_online_updater = true|menu_show_online_updater = false|g' \
    -e 's|# menu_show_core_updater = true|menu_show_core_updater = false|g'     \
    -i retroarch.cfg

# Freeworld config file
%if %{with freeworld}
sed -e 's|retroarch.cfg|%{name}.cfg|g'  \
    -i retroarch.c                      \
       configuration.c                  \
       %{nil}
%endif


%conf
# --disable-7zip              \
# --disable-builtinbearssl    \
# --disable-builtinflac       \
# --disable-builtinglslang    \
# --disable-builtinmbedtls    \
# --disable-builtinzlib       \
# --disable-oss               \
./configure                     \
    --prefix=%{_prefix}         \
    --disable-update_assets     \
    --enable-dbus               \
    --enable-libdecor           \
    --enable-spirv_cross        \
    --enable-vulkan             \
    --enable-wayland            \
    %{nil}


%build
%make_build

# Audio filters
%make_build -C libretro-common/audio/dsp_filters

# Video filters
%make_build -C gfx/video_filters


%install
%make_install
rm  %{buildroot}%{_docdir}/%{appname}/COPYING \
    %{buildroot}%{_docdir}/%{appname}/README.md

# Assets
%make_install -C %{appname}-assets-%{version}
%if %{with freeworld}
mv  %{buildroot}%{_datadir}/libretro/assets/ \
    %{buildroot}%{_datadir}/libretro/assets-freeworld/
%endif

# * Move assets license file in proper location
mkdir -p    %{buildroot}%{_licensedir}/%{name}-assets/
mv          %{buildroot}%{_datadir}/libretro/assets%{?p_suffix}/COPYING \
            %{buildroot}%{_licensedir}/%{name}-assets/COPYING

# * Remove sounds
#   CC-BY-NC-3.0 license is not permitted in Fedora
rm -rf %{buildroot}%{_datadir}/libretro/assets/sounds/

# Audio filters
%make_install -C libretro-common/audio/dsp_filters              \
    PREFIX=%{_prefix}                                           \
    INSTALLDIR=%{_libdir}/retroarch/filters%{?p_suffix}/audio

# Video filters
%make_install -C gfx/video_filters                              \
    PREFIX=%{_prefix}                                           \
    INSTALLDIR=%{_libdir}/retroarch/filters%{?p_suffix}/video

# Libretro's core info
%make_install -C libretro-core-info-%{version} \
    INSTALLDIR=%{_datadir}/libretro/info%{?p_suffix}

# AppData proper manifest
rm -f %{buildroot}%{_metainfodir}/*.xml
install -m 0644 -Dp %{SOURCE2} %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml

# Joypad Autoconfig Files
%make_install -C %{appname}-joypad-autoconfig-%{version} \
    DOC_DIR=%{_datadir}/libretro/autoconfig/doc
%if %{with freeworld}
mv  %{buildroot}%{_datadir}/libretro/autoconfig/ \
    %{buildroot}%{_datadir}/libretro/autoconfig-freeworld/
%endif

# Database files (cheatcode, content data, cursors)
%make_install -C libretro-database-%{version} \
    INSTALLDIR=%{_datadir}/libretro/database%{?p_suffix}

# Devel package
mkdir -p %{buildroot}%{_includedir}/libretro-common/
cp -ar libretro-common/include/* %{buildroot}%{_includedir}/libretro-common/

%if %{with freeworld}
# Rename binary, desktop file, appdata manifest, manpage and config file
mv  %{buildroot}%{_bindir}/%{appname} \
    %{buildroot}%{_bindir}/%{appname}-freeworld
mv  %{buildroot}%{_bindir}/%{appname}-cg2glsl \
    %{buildroot}%{_bindir}/%{appname}-cg2glsl-freeworld
mv  %{buildroot}%{_datadir}/applications/%{uuid}.desktop \
    %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
mv  %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml \
    %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
mv  %{buildroot}%{_sysconfdir}/%{appname}.cfg \
    %{buildroot}%{_sysconfdir}/%{name}.cfg
mv  %{buildroot}%{_mandir}/man6/%{appname}.6 \
    %{buildroot}%{_mandir}/man6/%{appname}-freeworld.6
mv  %{buildroot}%{_mandir}/man6/%{appname}-cg2glsl.6 \
    %{buildroot}%{_mandir}/man6/%{appname}-cg2glsl-freeworld.6
sed -i 's|Exec=retroarch|Exec=retroarch-freeworld|' \
    %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
sed -i 's|org.libretro.RetroArch.desktop|org.libretro.RetroArch-freeworld.desktop|' \
    %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
%endif

install -Dpm0755 %{SOURCE10} -t %{buildroot}%{_bindir}
install -Dpm0644 %{SOURCE11} -t %{buildroot}%{_docdir}/%{name}

# Fix Desktop file name
mv  %{buildroot}%{_datadir}/applications/com.libretro.RetroArch.desktop \
    %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml


%files
%license COPYING
%doc README.md README.fedora.md README-exynos.md README-OMAP.md README-mali_fbdev_r4p0.md CHANGES.md CONTRIBUTING.md
%{_bindir}/%{appname}
%{_bindir}/%{appname}-cg2glsl
%{_bindir}/%{appname}-enable-network-access.sh
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/libretro/autoconfig%{?p_suffix}/
%{_datadir}/libretro/info%{?p_suffix}/
%{_datadir}/pixmaps/*.svg
%{_mandir}/man6/*.6*
%{_metainfodir}/%{uuid}.appdata.xml
%dir %{_datadir}/libretro/

# Things may changed in future and it's safe to replace system config since old
# one will be saved in home dir
%config %{_sysconfdir}/%{name}.cfg


%files assets
# Incorrect-fsf-address
# * https://github.com/libretro/retroarch-assets/issues/335
%{_licensedir}/%{name}-assets/

%{_datadir}/libretro/assets%{?p_suffix}/
%dir %{_datadir}/libretro/


%files filters
%{_libdir}/%{appname}/filters%{?p_suffix}/
%dir %{_libdir}/%{appname}/


%files database
%{_datadir}/libretro/database%{?p_suffix}/cht/
%{_datadir}/libretro/database%{?p_suffix}/cursors/
%{_datadir}/libretro/database%{?p_suffix}/rdb/


%files devel
%{_includedir}/libretro-common/

%changelog
* Wed Aug 19 2026 madonuko <mado@fyralabs.com> - 1.22.0-1
- Port from Fedora
