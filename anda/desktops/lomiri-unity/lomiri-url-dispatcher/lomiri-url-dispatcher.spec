%global forgeurl https://gitlab.com/ubports/development/core/lomiri-url-dispatcher
%global commit 6b6f2277e2a63fe0893c1fddd1cc75da5da87eb7
%forgemeta

Name:           lomiri-url-dispatcher
Version:        0.1.3
Release:        2%{?dist}
Summary:        A small library for handling URLs over dbus

License:        LGPL-3.0
URL:            https://gitlab.com/ubports/development/core/lomiri-url-dispatcher
Source0:        %{url}/-/archive/%commit/lomiri-url-dispatcher-%commit.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libapparmor)
Requires:      lomiri-ui-toolkit
ExclusiveArch: x86_64 aarch64

%description
Lomiri-url-dispatcher is a small handler to take URLs and do what is
appropriate with them. That could be anything from launching a web browser to
just starting an application.  This is done over DBus because application
confinement doesn't allow for doing it from a confined application otherwise.
It's important the that applications can't know about each other, so this is a
fire and forget type operation.

%package devel
Summary:  Lomiri-url-dispatcher development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-url-dispatcher.

%prep
%autosetup -n lomiri-url-dispatcher-%commit
# Tests require static gtest library
sed -i '/add_subdirectory(tests)/d' ./CMakeLists.txt

%build
%cmake -Denable_mirclient=off

%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_libdir}/liblomiri-url-dispatcher.so.*
%{_bindir}/lomiri-url-*
%dir %{_libexecdir}/lomiri-app-launch/bad-url
%{_libexecdir}/lomiri-app-launch/bad-url/exec-tool
%dir %{_libexecdir}/lomiri-app-launch/url-overlay
%{_libexecdir}/lomiri-app-launch/url-overlay/exec-tool
%dir %{_libexecdir}/lomiri-url-dispatcher
%{_libexecdir}/lomiri-url-dispatcher/lomiri-*
%{_datadir}/applications/lomiri-url-dispatcher-gui.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%dir %{_datadir}/lomiri-url-dispatcher
%{_datadir}/lomiri-url-dispatcher/*.qml
%dir %{_datadir}/lomiri-url-dispatcher/gui
%{_datadir}/lomiri-url-dispatcher/gui/*.qml
%{_datadir}/lomiri-url-dispatcher/gui/*.svg
%{_userunitdir}/*.path
%{_userunitdir}/*.service

%files devel
%{_libdir}/liblomiri-url-dispatcher.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/liblomiri-url-dispatcher
%{_includedir}/liblomiri-url-dispatcher/*.h

%changelog
%autochangelog
