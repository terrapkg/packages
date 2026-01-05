Name:           somewm
Version:        0.5.0
Release:        1%?dist
Summary:        Wayland compositor that brings AwesomeWM's Lua API to Wayland
License:        GPL-3.0
URL:            https://github.com/trip-zip/somewm
Source:         %{url}/archive/%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(wlroots)
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

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc README.md CHANGELOG.md
%license LICENSE licenses/
%{_bindir}/%{name}
%{_bindir}/%{name}-client
%{_sysconfdir}/xdg/%{name}/rc.lua
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_mandir}/man1/somewm.1.*

%changelog
* Sun Jan 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
