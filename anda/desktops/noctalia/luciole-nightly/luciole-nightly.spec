%global appid dev.noctalia.luciole

%global ver 0

%global commit          f2aaa9fd726da60980bc9bf747f3737d36bb6272
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global buildrevision   %(c=%{commit}; echo ${c:0:9})
%global commitdate      20261128

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
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  stb_image_resize2-devel

Requires:       gvfs
Requires:       shared-mime-info
Requires:       gsettings-desktop-schemas
Requires:       dconf

Recommends:     adwaita-icon-theme
Recommends:     hicolor-icon-theme
Recommends:     glycin-loaders
Recommends:     glib-networking
Recommends:     (ffmpeg-free or ffmpeg)
Recommends:     ffmpegthumbnailer
Recommends:     poppler-utils
Recommends:     7zip
Recommends:     gvfs-smb
Recommends:     xdg-terminal-exec
Recommends:     xdg-desktop-portal

BuildSystem:    meson
BuildOption:    --buildtype=release
BuildOption:    -Dd_ndebug=true
BuildOption:    -Dtests=disabled
BuildOption:    -Dnative_optimizations=false
BuildOption:    -Dbuild_revision=%{buildrevision}

Conflicts:      luciole
# i imagine LionHeart will ship this as luciole-git (update: he did)
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
%doc README.md CONTRIBUTING.md PACKAGING.md docs/
%{_datadir}/luciole/assets/fonts/tabler-icons-license.txt
%{_bindir}/luciole
%{_datadir}/luciole/assets/fonts/noctalia-tabler.ttf
%{_datadir}/luciole/assets/fonts/tabler.json
%{_datadir}/dbus-1/services/dev.noctalia.luciole.FileManager1.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.luciole.service
%{_datadir}/xdg-desktop-portal/portals/luciole.portal
%{_appsdir}/dev.noctalia.luciole.desktop
%{_appsdir}/dev.noctalia.luciole-chooser.desktop
%{_scalableiconsdir}/dev.noctalia.luciole.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Fri Nov 27 2026 Cypress Reed <cypress@fyralabs.com>
- update reqs and files

* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
