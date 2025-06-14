Name:			logiops
Version:		0.3.5
Release:		1%?dist
Summary:		An unofficial userspace driver for HID++ Logitech devices
License:		GPL-3.0-only
URL:			https://github.com/PixlOne/logiops
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	cmake libevdev-devel systemd-devel libconfig-devel gcc-c++ glib2-devel
Provides:		logid = %evr

%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep
%git_clone %url v%version

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

echo "enable logid.service" | install -Dm644 /dev/stdin %buildroot%_presetdir/96-%name.preset

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%doc README.md
%license LICENSE
%_bindir/logid
%_datadir/dbus-1/system.d/pizza.pixl.LogiOps.conf
%_presetdir/96-%name.preset
%dnl %_sysconfdir/logid.cfg
%_unitdir/logid.service
