Name:           somewm
Version:        1.4.1
Release:        1%{?dist}
Summary:        Wayland compositor that brings AwesomeWM's Lua API to Wayland
License:        GPL-3.0-or-later
URL:            https://github.com/trip-zip/somewm
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  lua-lgi-compat
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  libxkbcommon-devel
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  dbus-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python3-devel
BuildRequires:  ninja-build

%description
somewm is a Wayland compositor that brings AwesomeWM's Lua API to Wayland, built on wlroots.
The goal is 100% compatibility with AwesomeWM's Lua configuration.

%prep
%autosetup

%package devel
%pkg_devel_files

%conf
%meson -Dwerror=false

%build
%meson_build

%install
%meson_install

%post
%systemd_post somewm.service

%preun
%systemd_preun somewm.service

%postun
%systemd_postun_with_restart somewm.service

%files
%doc README.md CHANGELOG.md
%license LICENSE licenses/
%{_bindir}/%{name}
%{_bindir}/%{name}-client
%{_bindir}/somewm-session
%{_sysconfdir}/xdg/%{name}/rc.lua
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/portals/somewm.portal
%{_mandir}/man1/somewm.1.*
%{_userunitdir}/somewm-shutdown.target
%{_userunitdir}/somewm.service

%changelog
* Sun May 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Update spec for 1.4.1

* Sun Jan 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
