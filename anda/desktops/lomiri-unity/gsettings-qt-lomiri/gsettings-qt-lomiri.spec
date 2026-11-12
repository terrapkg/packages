Name:       gsettings-qt-lomiri
Version:    1.1.1
Release:    1%{?dist}
Summary:    QML Bindings for GSettings
License:    LGPL-3.0-or-later
URL:        https://gitlab.com/ubports/development/core/gsettings-qt
Source0:    %{url}/-/archive/v%{version}/gsettings-qt-v%{version}.tar.gz?ref_type=tags

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: cmake(QmlPlugins)
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt-devel libxkbcommon-x11 libxcb libX11-xcb

%description
gsettings-qt provides Qt binding to GSettings, a high-level API
for application settings. This library can be used to access GSettings from Qt
applications.

%package devel
Requires: %{name}%{?_isa} = %{evr}

%pkg_devel_files

%prep
%autosetup -n gsettings-qt-v%{version}

%conf
export QT_QPA_PLATFORM=offscreen
%cmake

%build
%cmake_build

%install
%cmake_install INSTALL_ROOT=%{buildroot}
# Files underneath are part of coreutils and cpptest packages
rm -rf %{buildroot}/usr/tests

%files
%license COPYING
%{_libdir}/libgsettings-qt.so.*
%dir %{_libdir}/qt5/qml/GSettings.1.0
%{_libdir}/qt5/qml/GSettings.1.0/libGSettingsQmlPlugin.so
%{_libdir}/qt5/qml/GSettings.1.0/plugins.qmltypes
%{_libdir}/qt5/qml/GSettings.1.0/qmldir

%changelog
%autochangelog
