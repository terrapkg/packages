%global forgeurl https://gitlab.com/ubports/development/core/lomiri-indicator-network
%global commit a4522caf548d7e7f63f98f9e5c98314ee8d4c8fb
%forgemeta

Name:       lomiri-indicator-network
Version:    1.0.2
Release:    1%{?dist}
Summary:    The Network indicator for Ubuntu Touch
License:    GPL-3.0 AND LGPL-3.0
URL:        https://gitlab.com/ubports/development/core/lomiri-indicator-network
Source0:    %{url}/-/archive/%commit/lomiri-indicator-network-%commit.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: qt-devel
BuildRequires: doxygen
BuildRequires: qt5-doctools
BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(ofono)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(libgmenuharness)
BuildRequires: pkgconfig(ofono)
BuildRequires: pkgconfig(qofono-qt5)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(systemd)
Requires:      gmenuharness

%description
The "Network" indicator for Ubuntu Touch and Lomiri.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%autosetup -n lomiri-indicator-network-%commit

%build
%cmake -DENABLE_COVERAGE=OFF -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING COPYING.LGPL
%config /usr/etc/xdg/autostart/lomiri-indicator-network.desktop
%{_userunitdir}/*.service
%{_libdir}/liblomiri-connectivity-qt1.so.*
%dir %{_qt5_qmldir}/Lomiri/Connectivity
%{_qt5_qmldir}/Lomiri/Connectivity/libconnectivity-qml.so
%{_qt5_qmldir}/Lomiri/Connectivity/qmldir
%dir %{_qt5_qmldir}/Ubuntu/Connectivity
%{_qt5_qmldir}/Ubuntu/Connectivity/libconnectivity-qml-ubuntu-compat.so
%{_qt5_qmldir}/Ubuntu/Connectivity/qmldir
%dir %{_libexecdir}/lomiri-indicator-network
%{_libexecdir}/lomiri-indicator-network/lomiri-indicator-network-*
%{_datadir}/dbus-1/services/com.lomiri.connectivity1.service
%{_datadir}/glib-2.0/schemas/com.lomiri.indicator.network.gschema.xml
%{_datadir}/unity/indicators/com.lomiri.indicator.network

%files devel
%dir %{_includedir}/connectivity-api
%dir %{_includedir}/connectivity-api/qt1
%dir %{_includedir}/connectivity-api/qt1/connectivityqt
%{_includedir}/connectivity-api/qt1/connectivityqt/*.h
%dir %{_includedir}/connectivity-api/qt1/lomiri
%dir %{_includedir}/connectivity-api/qt1/lomiri/connectivity
%{_includedir}/connectivity-api/qt1/lomiri/connectivity/networking-status.h
%{_libdir}/liblomiri-connectivity-qt1.so
%{_libdir}/pkgconfig/lomiri-connectivity-qt1.pc

%files doc
%{_docdir}/lomiri-indicator-network

%changelog
%autochangelog
