Name:       libayatana-common
Summary:    Common functions for Ayatana System Indicators
Version:    0.9.10
Release:    2%{?dist}
License:    GPL-3.0
URL:        https://github.com/AyatanaIndicators/libayatana-common
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(lomiri-url-dispatcher)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala-devel
BuildRequires:  vala
BuildRequires:  intltool

%description
The Ayatana Indicators project is the continuation of Application Indicators
and System Indicators, two technologies developed by Canonical Ltd. for the
Unity7 desktop and Lomiri desktop.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DENABLE_LOMIRI_FEATURES=ON \
       -DENABLE_TESTS=ON \
       -DENABLE_COVERAGE=OFF

%cmake_build

%install
%cmake_install
%find_lang ayatana-common

%files -f ayatana-common.lang
%license COPYING
%{_userunitdir}/ayatana-indicators.target
%{_libdir}/libayatana-common.so.*
%{_libdir}/girepository-1.0/AyatanaCommon-0.0.typelib
%{_datadir}/glib-2.0/schemas/org.ayatana.common.gschema.xml

%files devel
%{_libdir}/libayatana-common.so
%{_datadir}/gir-1.0/AyatanaCommon-0.0.gir
%{_libdir}/pkgconfig/libayatana-common.pc
%dir %{_includedir}/ayatana
%dir %{_includedir}/ayatana/common
%{_includedir}/ayatana/common/utils.h
%{_datadir}/vala/vapi/AyatanaCommon.vapi

%changelog
%autochangelog
