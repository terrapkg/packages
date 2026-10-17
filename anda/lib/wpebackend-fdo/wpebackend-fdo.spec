%undefine __cmake_in_source_build

Name:           wpebackend-fdo
Version:        1.16.1
Release:        1%{?dist}
Summary:        A WPE backend designed for Linux desktop systems

SourceLicense:  BSD-2-Clause
License:        %{sourcelicense} AND MIT
URL:            https://github.com/Igalia/wpebackend-fdp
Source0:        https://wpewebkit.org/releases/wpebackend-fdo-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0)

Packager: Cypress Reed <cypress@fyralabs.com>

%description
A WPE backend designed for Linux desktop systems.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{evr}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-1.0.so.1
%{_libdir}/libWPEBackend-fdo-1.0.so.1.*

%files devel
%{_includedir}/wpe-fdo-1.0
%{_libdir}/libWPEBackend-fdo-1.0.so
%{_libdir}/pkgconfig/wpebackend-fdo-1.0.pc

%changelog
* Fri Oct 16 2026 Cypress Reed <cypress@fyralabs.com>
- port to Terra from COPR philn/wpewebkit
