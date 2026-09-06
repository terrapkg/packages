%global debug_package   %{nil}

%global commit          f62201b3e3ce350c17f72f5e0a142ac8ab51313d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260905

Name:   	xdg-desktop-portal-umbriel-nightly
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
%systemd_user_post xdg-desktop-portal-umbriel.service

%preun
%systemd_user_preun xdg-desktop-portal-umbriel.service

%postun
%systemd_user_postun xdg-desktop-portal-umbriel.service

%files
%doc README.md
%license LICENSE
%{_userunitdir}/xdg-desktop-portal-umbriel.service
%{_libexecdir}/umbriel-share-picker
%{_libexecdir}/xdg-desktop-portal-umbriel
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.umbriel.service
%{_datadir}/xdg-desktop-portal/portals/umbriel.portal
%config %{_datadir}/xdg-desktop-portal/umbriel-portals.conf

%changelog
* Mon Aug 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
