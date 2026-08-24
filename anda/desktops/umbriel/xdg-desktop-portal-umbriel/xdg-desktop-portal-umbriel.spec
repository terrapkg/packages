%global debug_package   %{nil}

%global commit          515c9f70f13ba4b4b9e19930b3e899c4ac8a50a4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260824

Name:   	xdg-desktop-portal-umbriel
Version:	0^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:    An xdg-desktop-portal backend for the Umbriel compositor

License:	MIT
URL:		https://github.com/noctalia-dev/xdg-desktop-portal-umbriel
Source0:	https://github.com/noctalia-dev/xdg-desktop-portal-umbriel/archive/%{commit}/xdg-desktop-portal-umbriel-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  systemd-rpm-macros

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n xdg-desktop-portal-umbriel-%{commit}

# Manually insert commit hash
sed -i "s/'unknown'/'%{shortcommit}'/g" meson.build

%conf
%meson

%build
%meson_build

%install
%meson_install

%post
%systemd_post xdg-desktop-portal-umbriel.service

%preun
%systemd_preun xdg-desktop-portal-umbriel.service

%postun
%systemd_postun xdg-desktop-portal-umbriel.service

%files
%doc README.md
%license LICENSE
%{_userunitdir}/xdg-desktop-portal-umbriel.service
%{_libexecdir}/umbriel-share-picker
%{_libexecdir}/xdg-desktop-portal-umbriel
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.umbriel.service
%{_datadir}/xdg-desktop-portal/portals/umbriel.portal
%{_datadir}/xdg-desktop-portal/umbriel-portals.conf

%changelog
* Mon Aug 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
