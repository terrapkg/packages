%global debug_package %{nil}
%global _default_patch_fuzz 2

Name:           opengamepadui
Version:        0.46.1
Release:        8%{?dist}
Summary:        Open source gamepad-native game launcher and overlay

License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/OpenGamepadUI
Packager:       Cappy Ishihara <cappy@fyralabs.com>

# Disable external game controllers for now
Patch0:         disable-manage-all.patch
# https://github.com/ShadowBlip/OpenGamepadUI/commit/a2c9ef8103d18c1e75d085492422f22db65b3541
Patch1:         https://github.com/ShadowBlip/OpenGamepadUI/commit/a2c9ef8103d18c1e75d085492422f22db65b3541.patch
# https://github.com/ShadowBlip/OpenGamepadUI/commit/ba2f231a3659b5c217c620582d424e0a56563895
Patch2:         https://github.com/ShadowBlip/OpenGamepadUI/commit/ba2f231a3659b5c217c620582d424e0a56563895.patch
# https://github.com/ShadowBlip/OpenGamepadUI/commit/2cf702ff40212174b45bb7579622b375bff9d132
Patch3:         https://github.com/ShadowBlip/OpenGamepadUI/commit/2cf702ff40212174b45bb7579622b375bff9d132.patch
# https://github.com/ShadowBlip/OpenGamepadUI/commit/397253fd09997c41b71ef3cc7829c7b74d5bf2a0
Patch4:         https://github.com/ShadowBlip/OpenGamepadUI/commit/397253fd09997c41b71ef3cc7829c7b74d5bf2a0.patch
# https://github.com/ShadowBlip/OpenGamepadUI/pull/531
Patch5:         https://patch-diff.githubusercontent.com/raw/ShadowBlip/OpenGamepadUI/pull/531.patch
# https://github.com/ShadowBlip/OpenGamepadUI/pull/525
Patch6:         https://patch-diff.githubusercontent.com/raw/ShadowBlip/OpenGamepadUI/pull/525.patch
# https://github.com/ShadowBlip/OpenGamepadUI/pull/548
Patch7:         https://patch-diff.githubusercontent.com/raw/ShadowBlip/OpenGamepadUI/pull/548.patch

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

# We clone the repo from Git here because the build script requires
# submodules to be present in the source directory.
rm -rf %{build_dir}
git clone %{url} %{build_dir} -b v%{version}
cd %{build_dir}
git checkout tags/v%{version}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1

%build
cd %{build_dir}
%make_build import
%make_build

%install
cd %{build_dir}
%make_install PREFIX=%{buildroot}%{_prefix} INSTALL_PREFIX=%{_prefix}

%files
%license %{build_dir}/LICENSE
%doc %{build_dir}/docs/
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
