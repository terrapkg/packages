%global commit 35e58010f3662b21b6632bbe55988dc18070534c
%global commit_date 20211031
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           ShivaVG
Version:        %commit_date.%shortcommit
Release:        1%{?dist}
Summary:        An open-source LGPL ANSI C implementation of the Khronos Group OpenVG specification

License:        LGPL-2.1-or-later
URL:            https://github.com/vpxyz/ShivaVG
Source0:        %{url}/archive/%{commit}/ShivaVG-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glew-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  freeglut-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig

%description
ShivaVG is an open-source LGPL ANSI C implementation of the Khronos Group OpenVG specification.
OpenVG is an royalty-free, cross-platform API that provides a low-level hardware acceleration
interface for vector graphics and imaging applications.

%package devel
Summary:        Development files for ShivaVG
Requires:       %{name}-%{version}-%{release}
Requires:       glew-devel
Requires:       mesa-libGL-devel

%description devel
Development files for ShivaVG, including header files and static library needed
to develop applications using the OpenVG API.

%package static
Summary:        Static library for ShivaVG
Requires:       %{name}-%{version}-%{release}

%description static
Static library for ShivaVG, needed when statically linking applications.

%prep
%autosetup -n ShivaVG-%{commit}

%build
mkdir build
cd build
%cmake .. -DSHARED_LIBRARY_NAME=OpenVG -DSTATIC_LIBRARY_NAME=OpenVGStatic -DBUILD_EXAMPLES=OFF
cd redhat-linux-build
%make_build

%install
cd build/redhat-linux-build
%make_install

%files
%{_libdir}/libOpenVG.so
%license COPYING
%doc README.md

%files devel
%{_includedir}/VG/
%{_libdir}/libOpenVGStatic.a
%{_libdir}/pkgconfig/openvg.pc
%{_libdir}/cmake/OpenVG/

%files static
%{_libdir}/libOpenVGStatic.a

%changelog
* Wed Aug 27 2025 Ruka <pkgs@ruka.red> - 20211031.35e5801-1
- Set up auto-update mechanism using commit-based versioning
- Added license and documentation files

* Mon Aug 25 2025 Ruka <pkgs@ruka.red> - 0.1.35e5801-1
- Initial packaging for Terra PKG
