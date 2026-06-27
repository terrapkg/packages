%global commit 35e58010f3662b21b6632bbe55988dc18070534c
%global commit_date 20211031
%global shortcommit %{sub %{commit} 1 7}

Name:           ShivaVG
Version:        0~%{commit_date}git.%shortcommit
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
Requires:       %{name} = %evr
Requires:       glew-devel
Requires:       mesa-libGL-devel
%pkg_devel_files
%_libdir/cmake/OpenVG/

%package static
Requires:       %{name} = %evr
%pkg_static_files

%prep
%autosetup -n ShivaVG-%{commit}
sed '/set(CMAKE_C_FLAGS/d' -i CMakeLists.txt

%build
%cmake -DBUILD_EXAMPLES=OFF -DDEBUG=ON -DPROJECT_VERSION=%commit -DCMAKE_C_FLAGS='%build_cflags'
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md

%changelog
* Wed Aug 27 2025 Ruka <pkgs@ruka.red> - 20211031.35e5801-1
- Set up auto-update mechanism using commit-based versioning
- Added license and documentation files

* Mon Aug 25 2025 Ruka <pkgs@ruka.red> - 0.1.35e5801-1
- Initial packaging for Terra PKG
