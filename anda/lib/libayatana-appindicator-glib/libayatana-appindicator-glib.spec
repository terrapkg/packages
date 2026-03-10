%undefine __brp_add_determinism

Name:       libayatana-appindicator-glib
Summary:    Ayatana Application Indicators Shared Library
Version:    2.0.1
Release:    1%?dist
License:    GPL-3.0
Packager:   veuxit <erroor234@gmail.com>
URL:        https://github.com/AyatanaIndicators/libayatana-appindicator-glib
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  glib2
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  gi-docgen
BuildRequires:  vala-devel
BuildRequires:  vala
BuildRequires:  intltool

%description
Ayatana Application Indicators Shared Library (GLib-2.0 reimplementation, 100% GTK-free, 100% dbusmenu-free)

%prep
%autosetup -n %{name}-%{version}

%build
%cmake 
%cmake_build

%install
%cmake_install

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/libayatana-appindicator-glib/
%{_libdir}/libayatana-appindicator-glib.so
%{_libdir}/pkgconfig/ayatana-appindicator-glib.pc
%{_datadir}/gir-1.0/AyatanaAppIndicatorGlib-2.0.gir
%{_datadir}/vala/vapi/ayatana-appindicator-glib.deps
%{_datadir}/vala/vapi/ayatana-appindicator-glib.vapi

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
Documentation for %{name}.

%files doc
%{_datadir}/doc/libayatana-appindicator-glib-dev/

%files
%license COPYING
%{_libdir}/libayatana-appindicator-glib.so.2*
%{_libdir}/girepository-1.0/AyatanaAppIndicatorGlib-2.0.typelib

%changelog
* Fri Feb 27 2026 veux <erroor234@gmail.com> - 2.0.1
- Initial package release