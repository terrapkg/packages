Name:           kooha
Version:        2.3.2
Release:        1%?dist
Summary:        Elegantly record your screen
URL:            https://github.com/SeaDve/Kooha
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
Patch0:         libadwaita-version-change.patch
SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} OR (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT)

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  desktop-file-utils

Packager:       Its-J <jonah@fyralabs.com>

%description
Capture your screen in an intuitive and straightforward way without distractions.

%prep
%autosetup -C -p1

%conf
%meson

%build
%meson_build

%install
%meson_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%license LICENSE.dependencies
%{_bindir}/kooha
%{_metainfodir}/io.github.seadve.Kooha.metainfo.xml
%{_appsdir}/io.github.seadve.Kooha.desktop
%{_datadir}/dbus-1/services/io.github.seadve.Kooha.service
%{_datadir}/glib-2.0/schemas/io.github.seadve.Kooha.gschema.xml
%{_datadir}/kooha/resources.gresource
%{_scalableiconsdir}/io.github.seadve.Kooha.svg
%{_hicolordir}/symbolic/apps/io.github.seadve.Kooha-symbolic.svg

%changelog
* Sat Aug 01 2026 Its-J <jonah@fyralabs.com> - 2.3.2-1
- Initial Package
