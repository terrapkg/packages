Summary:        libadwaita responsive widgets, without all the baggage.
Name:           libbismuth
Version:        1.0.2
Release:        1%{?dist}
License:        LGPL-2.1+
URL:            https://github.com/tau-OS/libbismuth
Source0:        https://github.com/tau-OS/libbismuth/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala
# Needed for wrap
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.4

Requires: gtk4 >= 4.4
Requires: glib2 >= 2.66.0

%description
The Application Framework for tauOS apps

%package devel
Summary:        Development files for libbismuth
Requires:       libbismuth = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with libbismuth.

%prep
%autosetup -n libbismuth-%{version}

%build
%meson
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
* Sun Oct 23 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.0.0
- Initial release
