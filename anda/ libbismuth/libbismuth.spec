Summary:        libadwaita responsive widgets, without all the baggage.
Name:           libbismuth
Version:        1.0
Release:        1%{?dist}
License:        LGPL-2.1+
URL:            https://tauos.co
Source0:        https://github.com/tau-OS/libbismuth/archive/refs/heads/main.zip

BuildRequires:  sass
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala
# Needed for wrap
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
# BuildRequires:  pkgconfig(gobject-introspection-1.0)
# BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4) >= 4.4

Requires: gtk4 >= 4.4
Requires: glib2 >= 2.66.0
Requires: libgee >= 0.20
Requires: tau-helium >= %{version}

%description
Based on libadwaita responsive widgets, without all the baggage.

%package devel
Summary:        Development files for libbismuth
Requires:       libbismuth = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with libbismuth.

%prep
%autosetup -n libbismuth-main

%build
%meson -Dgtk_doc=true
%meson_build

%install
# Install licenses
mkdir -p licenses
%meson_install

rm -rf %{buildroot}%{_bindir}/blueprint-compiler
rm -rf %{buildroot}%{_datadir}/themes/*

%files
%license COPYING
%doc README.md
%{_libdir}/libbismuth-1.so*
%{_libdir}/girepository-1.0

%files devel
%{_includedir}/*
%{_datadir}/gir-1.0/*
%{_libdir}/pkgconfig/*
%{_datadir}/vala/*

%changelog
* Tue Jun 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1.0-6
- I think we finally fixed naming

* Sat Jun 4 2022 Jamie Murphy <jamie@fyralabs.com> - 1.0-1
- Initial Release
