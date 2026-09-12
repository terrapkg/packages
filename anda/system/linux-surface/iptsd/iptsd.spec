%global toolchain clang

Name: iptsd
Version: 3.1.0
Release: 1%{?dist}
Summary: Userspace daemon for Intel Precise Touch & Stylus
License: GPL-2.0-or-later

URL: https://github.com/linux-surface/iptsd
Source: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: meson
BuildRequires: clang

# Some of our dependencies can only be resolved with cmake
BuildRequires: cmake

# Daemon
BuildRequires: cmake(CLI11)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(inih)
BuildRequires: cmake(Microsoft.GSL)
BuildRequires: pkgconfig(spdlog)

# Debug Tools
BuildRequires: pkgconfig(cairomm-1.0)
BuildRequires: pkgconfig(sdl2)

BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: systemd-rpm-macros

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
iptsd is a userspace daemon that processes touch events from the IPTS
kernel driver, and sends them back to the kernel using uinput devices.

%prep
%autosetup -C

%conf
# Give us all the O's
%global optflags %(echo %{optflags} | sed 's|-O2||g' | sed 's|-mtune=generic||g')
%meson --buildtype=release --debug

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/iptsd.conf
%dir %{_datadir}/iptsd
%dir %{_sysconfdir}/iptsd.d
%{_bindir}/iptsd
%{_bindir}/iptsd-check-device
%{_bindir}/iptsd-calibrate
%{_bindir}/iptsd-dump
%{_bindir}/iptsd-find-hidraw
%{_bindir}/iptsd-find-service
%{_bindir}/iptsd-foreach
%{_bindir}/iptsd-perf
%{_bindir}/iptsd-plot
%{_bindir}/iptsd-show
%{_bindir}/iptsd-systemd
%{_unitdir}/iptsd@.service
%{_udevrulesdir}/50-iptsd.rules
%{_datadir}/iptsd/*

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com> - 3.1.0-1
- Initial commit, port to Terra from linux-surface
