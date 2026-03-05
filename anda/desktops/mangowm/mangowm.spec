%global mangowc_ver 0.12.5-1

Name:           mangowm
Version:        0.12.5
Release:        2%{?dist}
Summary:        A modern, lightweight, high-performance Wayland compositor built on dwl
License:        GPL-3.0-or-later AND MIT AND X11 AND CC0-1.0
Packager:       metcya <metcya@gmail.com>
URL:            https://github.com/mangowm/mango
Source:         %{url}/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(scenefx-0.4)

Conflicts:      mangowc < %{mangowc_ver}
Obsoletes:      mangowc < %{mangowc_ver}
Provides:       mangowc = %{mangowc_ver}

%description
MangoWM is a modern, lightweight, high-performance Wayland compositor built on
dwl — crafted for speed, flexibility, and a customizable desktop experience.

%prep
%autosetup -n mango-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%license LICENSE.wlroots
%license LICENSE.tinywl 
%license LICENSE.sway 
%license LICENSE.dwm 
%license LICENSE.dwl 
%{_bindir}/mango
%{_bindir}/mmsg
%{_sysconfdir}/mango/config.conf
%{_datadir}/wayland-sessions/mango.desktop
%{_datadir}/xdg-desktop-portal/mango-portals.conf

%changelog
* Wed Mar 04 2026 metcya <metcya@gmail.com> - 0.12.5-1
- Rename to mangowm

* Wed Nov 12 2025 metcya <metcya@gmail.com>
- Package mangowc
