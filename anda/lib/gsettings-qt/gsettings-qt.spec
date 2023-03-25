%global forgeurl https://gitlab.com/ubports/development/core/gsettings-qt
%global commit d5e002d7e0bce46c315bcc99a44a8bd51f49f488
%forgemeta

Name:       gsettings-qt
Version:    0.2
Release:    %autorelease
Summary:    QML Bindings for GSettings
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/gsettings-qt
Source0:    %{url}/-/archive/%commit/gsettings-qt-%commit.tar.gz

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtdeclarative-devel

%description
gsettings-qt provides Qt binding to GSettings, a high-level API
for application settings. This library can be used to access GSettings from Qt
applications.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gsettings-qt-%commit

%build
%qmake_qt5

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
# Files underneath are part of coreutils and cpptest packages
rm -rf %{buildroot}/usr/tests

%files
%license COPYING
%{_libdir}/libgsettings-qt.so.1
%{_libdir}/libgsettings-qt.so.1.0
%{_libdir}/libgsettings-qt.so.1.0.0
%dir %{_libdir}/qt5/qml/GSettings.1.0
%{_libdir}/qt5/qml/GSettings.1.0/libGSettingsQmlPlugin.so
%{_libdir}/qt5/qml/GSettings.1.0/plugins.qmltypes
%{_libdir}/qt5/qml/GSettings.1.0/qmldir

%files devel
%dir %{_includedir}/qt5/QGSettings
%{_includedir}/qt5/QGSettings/QGSettings
%{_includedir}/qt5/QGSettings/qgsettings.h
%{_libdir}/libgsettings-qt.so
%{_libdir}/pkgconfig/gsettings-qt.pc

%changelog
%autochangelog
