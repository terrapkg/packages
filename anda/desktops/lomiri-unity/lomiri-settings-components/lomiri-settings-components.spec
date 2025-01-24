%global forgeurl https://gitlab.com/ubports/development/core/lomiri-settings-components
%global commit 8be505f0a54e9803adcaa20fefe334b3c3b7d4e7
%forgemeta

Name:       lomiri-settings-components
Version:    1.1.2
Release:    1%?dist
Summary:    The system settings components for Lomiri
License:    GPLv3 AND LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-settings-components
Source0:    %{url}/-/archive/%commit/lomiri-settings-components-%commit.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(QtGui)
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: cmake(QmlPlugins)
Recommends:    lomiri-system-settings

%description
The system settings qml components for lomiri-system-settings.

%prep
%autosetup -n %{name}-%commit

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.GPL COPYING.LGPL
%dir %{_qt5_qmldir}/Lomiri/Settings
%{_qt5_qmldir}/Lomiri/Settings/Components/
%{_qt5_qmldir}/Lomiri/Settings/Fingerprint/
%{_qt5_qmldir}/Lomiri/Settings/Menus/
%{_qt5_qmldir}/Lomiri/Settings/Vpn/

%changelog
%autochangelog
