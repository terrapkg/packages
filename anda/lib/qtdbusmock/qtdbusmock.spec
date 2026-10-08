%global forgeurl https://gitlab.com/ubports/development/core/libqtdbusmock

Name:       qtdbusmock
Version:    0.10.0

%forgemeta
Release:    1%{?dist}
Summary:    Library for mocking DBus interactions using Qt
License:    LGPL-3.0-or-later
URL:        https://gitlab.com/ubports/development/core/libqtdbusmock
Source0:    %{url}/-/archive/%{version}/libqtdbusmock-%{version}.tar.gz

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
%autosetup -n libqtdbusmock-%{version}

%conf
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
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
