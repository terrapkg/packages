Name:           opengamepadui
Version:        0.45.1
Release:        3%{?dist}
Summary:        Open source gamepad-native game launcher and overlay

License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/OpenGamepadUI
Packager:       Cappy Ishihara <cappy@fyralabs.com>

# https://patch-diff.githubusercontent.com/raw/ShadowBlip/OpenGamepadUI/pull/523
Patch0:         523.patch
Patch1:         disable-manage-all.patch

BuildRequires:  godot
BuildRequires:  scons
BuildRequires:  make
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  libXinerama-devel
BuildRequires:  libXi-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libevdev-devel
BuildRequires:  git
BuildRequires:  wget
BuildRequires:  unzip
BuildRequires:  dbus-devel
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  systemd-rpm-macros
BuildRequires:  patch

Requires:       godot-runner
Recommends:     inputplumber
Recommends:     powerstation

%description
Open Gamepad UI is a free and open source game launcher and overlay
written using the Godot Game Engine 4 designed with a gamepad native
experience in mind. Its goal is to provide an open and extendable
foundation to launch and play games. It also implements a gamepad
input system that can allow you to remap
gamepad input to mouse and keyboard inputs.

%prep
%git_clone %{url} tags/v%{version}
%patch 0 -p0
%patch 1 -p0

%build
%make_build import
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix} INSTALL_PREFIX=%{_prefix}

%files
%license /LICENSE
%doc /docs/
%{_bindir}/opengamepadui
%{_datadir}/opengamepadui/
%{_datadir}/applications/opengamepadui.desktop
%{_datadir}/icons/hicolor/scalable/apps/opengamepadui.svg
%{_datadir}/polkit-1/actions/*
%{_userunitdir}/*

%changelog
* Fri Jul 24 2026 HikariKnight <2557889+HikariKnight@users.noreply.github.com>
- Add patch to disable manage_all for inputplumber in overlay mode

* Sun Oct 20 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package
