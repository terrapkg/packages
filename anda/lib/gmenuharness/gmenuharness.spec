%global forgeurl https://gitlab.com/ubports/development/core/gmenuharness
%global commit 04e27ce98ca2d2b132b9bd0279a80bcb1ccbcc8c
%forgemeta

Name:       gmenuharness
Version:    0.1.4
Release:    %autorelease
Summary:    GMenu harness library
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/gmenuharness
Source0:    %{url}/-/archive/%commit/gmenuharness-%commit.tar.gz

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libqtdbustest-1)

%description
GMenu harness library for lomiri.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gmenuharness-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/libgmenuharness.so.*

%files devel
%dir %{_includedir}/gmenuharness-0.1
%dir %{_includedir}/gmenuharness-0.1/lomiri
%dir %{_includedir}/gmenuharness-0.1/lomiri/gmenuharness
%{_includedir}/gmenuharness-0.1/lomiri/gmenuharness/*.h
%{_libdir}/libgmenuharness.so
%{_libdir}/pkgconfig/libgmenuharness.pc

%changelog
%autochangelog
