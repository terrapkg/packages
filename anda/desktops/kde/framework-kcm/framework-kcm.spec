Name:           framework-kcm
Version:        0.1.0
Release:        1%{?dist}
Summary:        KDE settings pane for Framework Laptop hardware

License:        GPL-3.0-or-later
URL:            https://github.com/halfcyan/framework-kcm
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  kf6-rpm-macros

Requires:       framework-system
Requires:       plasma-systemsettings

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Framework KCM is a KDE System Settings pane for configuring Framework Laptop
hardware. It provides battery and hardware controls through framework_tool.

%prep
%autosetup -n framework-kcm-%{version}

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_framework.so
%{_appsdir}/kcm_framework.desktop

%changelog
* Mon Sep 28 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
