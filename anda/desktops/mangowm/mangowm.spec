Name:           mangowm
Version:        0.12.5
Release:        2%?dist
Summary:        Practical and Powerful wayland compositor (dwm but wayland)
License:        GPL-3.0
Packager:       metcya <metcya@gmail.com>
URL:            https://mangowm.github.io
Source:         https://github.com/mangowm/mango/archive/%{version}.tar.gz

Provides:       mangowc = %evr
Obsoletes:      mangowc < 0.12.5-2

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

%description
MangoWM is a lightweight, high-performance Wayland compositor built on dwl, designed for speed, flexibility, and a modern, customizable desktop experience.

%prep
%autosetup

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

%changelog
* Wed Nov 12 2025 metcya <metcya@gmail.com>
- Package mangowc
