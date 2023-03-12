Name:       qt5-qtdbustest
Version:    0.2+bzr42
Release:    %autorelease
Summary:    Library for testing DBus interactions using Qt5
License:    LGPLv3
URL:        https://launchpad.net/libqtdbustest
Source0:    http://deb.debian.org/debian/pool/main/libq/libqtdbustest/libqtdbustest_0.2+bzr42+repack1.orig.tar.xz
Source1:    https://salsa.debian.org/debian-ayatana-team/libqtdbustest/-/archive/master/libqtdbustest-master.tar.gz

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
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libqtdbustest-%{version}
# Apply fixes
tar -xf '%{SOURCE1}'
for i in $(cat libqtdbustest-master/debian/patches/series); do patch -p1 < libqtdbustest-master/debian/patches/$i; done

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/qdbus-simple-test-runner
%{_libdir}/libqtdbustest.so.*
%dir %{_libexecdir}/libqtdbustest
%{_libexecdir}/libqtdbustest/watchdog
%dir %{_datadir}/libqtdbustest
%{_datadir}/libqtdbustest/*.conf

%files devel
%license COPYING
%dir %{_includedir}/libqtdbustest-1
%dir %{_includedir}/libqtdbustest-1/libqtdbustest
%{_includedir}/libqtdbustest-1/libqtdbustest/*.h
%{_libdir}/libqtdbustest.so
%{_libdir}/pkgconfig/libqtdbustest-1.pc

%changelog
%autochangelog
