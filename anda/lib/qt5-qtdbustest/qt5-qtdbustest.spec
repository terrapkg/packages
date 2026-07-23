Name:       qt5-qtdbustest
Version:    0.4.1
Release:    1%{?dist}
Summary:    Library for testing DBus interactions using Qt5
License:    LGPL-3.0-or-later
URL:        https://gitlab.com/ubports/development/core/libqtdbustest
Source0:    %{url}/-/archive/%{version}/libqtdbustest-%{version}.tar.gz?ref_type=tags

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: gcovr
BuildRequires: lcov
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)

%description
A simple library for testing Qt based DBus services and clients.
This package contains the shared libraries.

%package devel
%pkg_devel_files

%prep
%autosetup -n libqtdbustest-%{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_bindir}/qdbus-simple-test-runner
%{_libdir}/libqtdbustest.so.*
%{_libexecdir}/libqtdbustest/watchdog
%{_datadir}/libqtdbustest/*.conf

%changelog
* Thu Jul 23 2026 Owen Zimmerman <owen@fyralabs.com> - 0.4.1-1
- Bump, modernize spec, get rid of commit tracking and forgemeta
