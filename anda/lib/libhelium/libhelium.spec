%global ver 1.8.14-2
%global sanitized_ver %(echo %{ver} | sed -E 's/-/~/g')
Summary:        The Application Framework for tauOS apps
Name:           libhelium
Version:        %{sanitized_ver}
Release:        1%?dist
License:        GPL-3.0
URL:            https://github.com/tau-OS/libhelium
Source0:        https://github.com/tau-OS/libhelium/archive/refs/tags/%{ver}.tar.gz

BuildRequires:  sass
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala
# Needed for wrap
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4) >= 4.4

Requires: gtk4 >= 4.4
Requires: glib2 >= 2.66.0
Requires: libgee >= 0.20
Requires: tau-helium >= 1.1.25
Requires: tau-hydrogen

%description
The Application Framework for tauOS apps

%package devel
Summary:        Development files for libhelium
Requires:       libhelium = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with libhelium.

%prep
%autosetup -n libhelium-%{ver}

%build
%meson \
    -Ddemo=false \
    -Dvaladoc=false \
    --wrap-mode=default
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
%{_libdir}/libhelium-1.so.*
%{_libdir}/girepository-1.0
%{_datadir}/glib-2.0/schemas/com.fyralabs.desktop.appearance.gschema.xml

%files devel
%{_libdir}/libhelium-1.so
%{_includedir}/*
%{_datadir}/gir-1.0/*
%{_libdir}/pkgconfig/*
%{_datadir}/vala/*

%changelog
* Tue Dec 06 2022 root - 1.2.0-1
- new version

* Tue Dec 06 2022 root - 1.1.7-1
- new version

* Sat Nov 19 2022 root - 1.1.6-1
- new version

* Fri Nov 11 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.5-1
- new version

* Sun Oct 23 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.0-1
- 1.1.0 release

* Tue Jun 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1.0-6
- I think we finally fixed naming

* Sat Jun 4 2022 Jamie Murphy <jamie@fyralabs.com> - 1.0-1
- Initial Release
