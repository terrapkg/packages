Name:           libwpe
Version:        1.16.3
Release:        1%{?dist}
Summary:        General-purpose library for the WPE-flavored port of WebKit
SourceLicense:  BSD-2-Clause
License:        %{sourcelicense} AND Apache-2.0 AND LGPL-2.0-or-later AND MIT-open-group AND HPND
URL:            https://github.com/WebPlatformForEmbedded/%{name}
Source0:        https://wpewebkit.org/releases/libwpe-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(xkbcommon)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{evr}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n libwpe-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libwpe-1.0.so.1.*
%{_libdir}/libwpe-1.0.so.1

%files devel
%{_includedir}/wpe-1.0/
%{_libdir}/libwpe-1.0.so
%{_libdir}/pkgconfig/wpe-1.0.pc

%changelog
* Fri Oct 16 2026 Cypress Reed <cypress@fyralabs.com>
- port to Terra from COPR philn/wpewebkit
