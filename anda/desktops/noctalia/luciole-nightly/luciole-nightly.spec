%global appid dev.noctalia.luciole

%global ver 0

%global commit          734959fe40b3d21a640714af5da1b5f2261e9dbb
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20261116

Name:   	luciole-nightly
Version:	%{ver}^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A native file manager with list, grid, and Miller column support for Wayland

License:	MIT
URL:		https://github.com/noctalia-dev/luciole
Source0:	https://github.com/noctalia-dev/luciole/archive/%{commit}/luciole-%{commit}.tar.gz
Source1:    %{appid}.metainfo.xml

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  stb_image_resize2-devel

Requires:       shared-mime-info
Requires:       gsettings-desktop-schemas
Requires:       dconf
Requires:       adwaita-icon-theme
Requires:       gvfs
Requires:       gvfs-smb
Requires:       glib-networking
Requires:       (ffmpeg-free or ffmpeg)
Requires:       ffmpegthumbnailer
Requires:       poppler-utils
Requires:       7zip
Requires:       xdg-terminal-exec

BuildSystem:    meson
BuildOption:    --buildtype=release
BuildOption:    -Dtests=disabled
BuildOption:    -Dnative_optimizations=false

Conflicts:      luciole
# i imagine LionHeart will ship this as luciole-git
Conflicts:      luciole-git

Packager: Cypress Reed <cypress@fyralabs.com>

%description
Luciole is a native Wayland file manager with list,
grid and optional Miller column views, tabs, split view and a side preview.

%install -a
%terra_appstream -o %{S:1}
rm %{buildroot}%{_defaultlicensedir}/luciole/LICENSE

%pkg_completion -Bfz luciole

%files
%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/luciole
%{_datadir}/luciole/assets/fonts/noctalia-tabler.ttf
%{_datadir}/luciole/assets/fonts/tabler.json
%{_datadir}/luciole/assets/fonts/tabler-icons-license.txt
%{_datadir}/luciole/templates/colors.toml
%{_datadir}/dbus-1/services/dev.noctalia.luciole.FileManager1.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.luciole.service
%{_datadir}/xdg-desktop-portal/portals/luciole.portal
%{_appsdir}/dev.noctalia.luciole.desktop
%{_scalableiconsdir}/dev.noctalia.luciole.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
