%global forgeurl https://gitlab.com/ubports/development/core/deviceinfo
%global commit 4423aab5a9f25ac1f6baf0623c7cf7a040d254ff
%forgemeta

Name:       deviceinfo
Version:    0.2.3
Release:    1%?dist
Summary:    Library to detect and configure devices
License:    GPLv3+
URL:        https://gitlab.com/ubports/development/core/deviceinfo
Source0:    %{url}/-/archive/%commit/deviceinfo-%commit.tar.gz
Source1:    https://salsa.debian.org/ubports-team/deviceinfo/-/raw/master/debian/device-info.1

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: gcc-c++

%description
Library to detect and configure devices for Lomiri.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n deviceinfo-%commit

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm644 '%{SOURCE1}' %{buildroot}%{_mandir}/man1/device-info.1

%files
%license LICENSE
%dir %{_sysconfdir}/deviceinfo
%config %{_sysconfdir}/deviceinfo/default.yaml
%dir %{_sysconfdir}/deviceinfo/devices
%config %{_sysconfdir}/deviceinfo/devices/*.yaml
%dir %{_sysconfdir}/deviceinfo/sensorfw
%config %{_sysconfdir}/deviceinfo/sensorfw/*.conf
%{_bindir}/device-info
%{_mandir}/man1/device-info.1.gz
%{_libdir}/libdeviceinfo.so.*

%files devel
%dir %{_includedir}/deviceinfo
%{_includedir}/deviceinfo/deviceinfo.h
/usr/include/deviceinfo/deviceinfo_c_api.h
%{_libdir}/libdeviceinfo.so
%{_libdir}/pkgconfig/deviceinfo.pc

%changelog
%autochangelog
