Name:           framework-kcm
Version:        0.1.1
Release:        1%{?dist}
Summary:        KDE System Settings module for Framework laptops

License:        GPL-3.0-or-later
URL:            https://github.com/flamingspaz/framework-kcm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.22
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconf-pkg-config
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  hidapi-devel
BuildRequires:  libusb1-devel
BuildRequires:  systemd-devel
BuildRequires:  libudev-devel
BuildRequires:  systemd-rpm-macros

Requires:       plasma-systemsettings
Requires:       kf6-kcmutils
Requires:       kf6-kirigami
Requires:       qt6-qtdeclarative
Requires:       polkit
Requires:       systemd

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Framework KCM is a KDE System Settings module for Framework laptops. It
provides battery, fan, touchpad, LED, firmware and USB-C port controls, with
a companion system service for hardware access.

%prep
%autosetup -n framework-kcm-%{version}

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install
%find_lang kcm_framework

%post
%systemd_post framework-kcmd.service

%preun
%systemd_preun framework-kcmd.service

%postun
%systemd_postun_with_restart framework-kcmd.service

%files -f kcm_framework.lang
%license LICENSE
%doc README.md
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_framework.so
%{_appsdir}/kcm_framework.desktop
%{_datadir}/dbus-1/system.d/io.github.frameworkkcm.Daemon1.conf
%{_datadir}/dbus-1/system-services/io.github.frameworkkcm.Daemon1.service
%{_unitdir}/framework-kcmd.service
%{_libexecdir}/framework-kcmd
%{_datadir}/polkit-1/actions/io.github.frameworkkcm.policy
%{_scalableiconsdir}/framework-kcm.svg

%changelog
* Fri Oct 02 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
