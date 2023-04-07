%global forgeurl https://gitlab.com/ubports/development/core/libqtdbusmock
%global commit e875ddd9b79d87bffe6b10047e592b304bd62a47
%forgemeta

Name:       qtdbusmock
Version:    0.9.0
Release:    %autorelease
Summary:    Library for mocking DBus interactions using Qt
License:    LGPL-3.0
URL:        https://gitlab.com/ubports/development/core/libqtdbusmock
Source0:    %{url}/-/archive/%commit/libqtdbusmock-%commit.tar.gz

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
Requires:      qt5-qtdbustest

%description
A simple library for mocking DBus services with a Qt API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libqtdbusmock-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libqtdbusmock.so.*
%dir %{_datadir}/libqtdbusmock
%dir %{_datadir}/libqtdbusmock/templates
%{_datadir}/libqtdbusmock/templates/*.py

%files devel
%dir %{_includedir}/libqtdbusmock-1
%dir %{_includedir}/libqtdbusmock-1/libqtdbusmock
%{_includedir}/libqtdbusmock-1/libqtdbusmock/*.h
%{_libdir}/libqtdbusmock.so
%{_libdir}/pkgconfig/libqtdbusmock-1.pc

%changelog
%autochangelog
