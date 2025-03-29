Name:           opengamepadui
Version:        0.39.0
Release:        1%?dist
Summary:        Open source gamepad-native game launcher and overlay

License:        GPLv3
URL:            https://github.com/ShadowBlip/OpenGamepadUI
Packager:       Cappy Ishihara <cappy@fyralabs.com>

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

Requires:       godot-runner
Recommends:     inputplumber
Recommends:     powerstation

%global build_dir %{name}-%{version}

%description
Open Gamepad UI is a free and open source game launcher and overlay written using the Godot Game Engine 4 designed with a gamepad native experience in mind. Its goal is to provide an open and extendable foundation to launch and play games. It also implements a gamepad input system that can allow you to
remap gamepad input to mouse and keyboard inputs.

%prep

# We clone the repo from Git here because the build script requires
# submodules to be present in the source directory.
rm -rf %{build_dir}
git clone %{url} %{build_dir} -b v%{version}
cd %{build_dir}
git checkout tags/v%{version}

%build
cd %{build_dir}
make import
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
* Sun Oct 20 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package
