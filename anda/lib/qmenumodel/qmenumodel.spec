Name:       qmenumodel
Version:    0.9.1
Release:    %autorelease
Summary:    Qt5 renderer for Ayatana Indicators
License:    LGPL-3.0
URL:        https://github.com/AyatanaIndicators/qmenumodel
Source0:    https://releases.ayatana-indicators.org/source/qmenumodel/qmenumodel-%{version}.tar.gz
Patch0:     https://gitlab.com/ubports/development/core/packaging/qmenumodel/-/raw/9062c3a3da87d6fd887c41a67dec6f8d5f34baa8/debian/patches/1001-ayatanamenumodel-add-support-for-u-int-of-all-sizes.patch

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: qt5-doctools
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: dbus-test-runner

%description
Qt bindings for GMenuModel that allows connecting to a menu model exposed on
D-Bus and presents it as a list model. It can be used to expose indicator or
application menus for applications using the Qt framework.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n qmenumodel-%{version} -p1

%build
%cmake -DENABLE_TESTS=ON -DENABLE_COVERAGE=ON -DGENERATE_DOC=ON
%cmake_build

%install
%cmake_install

%files
%doc README
%license COPYING.LGPL
%{_libdir}/libqmenumodel.so.*
%dir %{_qt5_qmldir}/QMenuModel.1
%{_qt5_qmldir}/QMenuModel.1/libqmenumodel-qml.so
%{_qt5_qmldir}/QMenuModel.1/qmldir

%files devel
%dir %{_includedir}/qmenumodel
%{_includedir}/qmenumodel/*.h
%{_libdir}/libqmenumodel.so
%{_libdir}/pkgconfig/qmenumodel.pc

%changelog
%autochangelog
