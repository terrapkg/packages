%global forgeurl https://gitlab.com/ubports/development/core/lomiri-app-launch
%global commit a057a37b56b96efddc7f42577407a3a08a0575cf
%forgemeta

Name:           lomiri-app-launch
Version:        0.1.9
Release:        1%{?dist}
Summary:        Provides the Lomiri App Launch user space daemon
License:        GPL-3.0
URL:            https://gitlab.com/ubports/development/core/lomiri-app-launch
Source0:        %{url}/-/archive/%commit/lomiri-app-launch-%commit.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(mirserver)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(dbus-1)

# Not in pkgconfig but required
BuildRequires: properties-cpp-devel
BuildRequires: libcurl-devel
BuildRequires: systemd-rpm-macros

%description
User space daemon for launching applications
Application launching system and associated utilities that is used to
launch applications in a standard and confined way.

%package devel
Summary:  Lomiri-app-launch development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-app-launch.

%prep
%autosetup -n lomiri-app-launch-%commit

%build
sed -i 's/-Werror//' ./CMakeLists.txt

# For some reason the macro of cmake fails on both clang and gcc
cmake -DLOMIRI_APP_LAUNCH_ARCH=%{_arch} -DENABLE_COVERAGE=OFF -DENABLE_TESTS=OFF -B redhat-linux-build -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_MIRCLIENT=off -DUSE_SYSTEMD=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/liblomiri-app-launch.so.*
%{_libdir}/girepository-1.0/LomiriAppLaunch-0.typelib
%{_userunitdir}/lal-application-end.target
%{_bindir}/lomiri-app-*
%{_bindir}/lomiri-helper-*
%{_libexecdir}/lomiri-app-launch/

%files devel
%{_libdir}/liblomiri-app-launch.so
%{_libdir}/pkgconfig/*.pc
%{_datarootdir}/gir-1.0/LomiriAppLaunch-0.gir
%dir %{_includedir}/liblomiri-app-launch-0
%{_includedir}/liblomiri-app-launch-0/*.h
%dir %{_includedir}/liblomiri-app-launch-0/lomiri-app-launch
%{_includedir}/liblomiri-app-launch-0/lomiri-app-launch/*.h

%changelog
%autochangelog
