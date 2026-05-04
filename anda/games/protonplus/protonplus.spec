%define appid com.vysp3r.ProtonPlus

Name:           protonplus
Version:        0.5.20
Release:        1%{?dist}
Summary:        A modern compatibility tools manager
License:        GPL-3.0-or-later
URL:            https://github.com/Vysp3r/ProtonPlus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  desktop-file-utils

Provides:       ProtonPlus

%description
ProtonPlus is a modern compatibility tools manager for Linux.
It allows you to easily manage and update various compatibility
tools like Proton, Wine, DXVK, and VKD3D across different launchers.

%prep
%autosetup -n ProtonPlus-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%find_lang %{appid}

%files -f %{appid}.lang
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md
%license LICENSE.md
%{_bindir}/protonplus
%{_metainfodir}/%{appid}.metainfo.xml
%{_appsdir}/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_hicolordir}/*/apps/%{appid}.png

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
