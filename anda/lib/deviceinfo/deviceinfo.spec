%global forgeurl https://gitlab.com/ubports/development/core/deviceinfo
%global commit fe939f071aafa47f631caec55a4e8420b3eb4a12
%forgemeta

Name:       deviceinfo
Version:    0.1.1
Release:    %autorelease
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
%{_sysconfdir}/deviceinfo/default.yaml
%dir %{_sysconfdir}/deviceinfo/devices
%{_sysconfdir}/deviceinfo/devices/*.yaml
%dir %{_sysconfdir}/deviceinfo/sensorfw
%{_sysconfdir}/deviceinfo/sensorfw/*.conf
%{_bindir}/device-info
%{_mandir}/man1/device-info.1.gz
%{_libdir}/libdeviceinfo.so.*

%files devel
%dir %{_includedir}/deviceinfo
%{_includedir}/deviceinfo/deviceinfo.h
%{_libdir}/libdeviceinfo.so
%{_libdir}/pkgconfig/deviceinfo.pc

%changelog
%autochangelog
