%global appid io.github.rfrench3.controllable

Name:           qt6-controllable
Version:        0.2.0
Release:        1%{?dist}
Summary:        QML module for controller support

License:        GPL-2.0-or-later
URL:            https://github.com/rfrench3/controllable
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Packager:       Robert French <frenchrobertm@outlook.com>

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(SDL3)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  cmake(KF6I18n)

Requires:       kf6-ki18n

Provides:       qt6-controllable = %{evr}

%description
A QML module that provides support for controllers.

%prep
%autosetup -n controllable-%{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{orgname}.*.xml || :

%files
%license LICENSE.txt
%doc README.md
%{_kf6_metainfodir}/%{appid}.*.xml
%{_kf6_libdir}/libqt6-controllable.so
%{_kf6_qmldir}/io/github/rfrench3/controllable/*



%changelog
* Tue May 12 2026 Robert French
- Initial tests for rpm package
* Sun Apr 26 2026 Robert French
- First day of splitting this module off of bazzite updater
