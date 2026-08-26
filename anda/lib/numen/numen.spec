Name:           numen
Version:        0.4.1
Release:        1%{?dist}
Summary:        Zero dependency calculator library

License:        BSD-3-Clause
URL:            https://github.com/vicinaehq/numen
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake-rpm-macros

BuildSystem:    cmake
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

Packager:       Olivia <git@olivia.sh>

%description
Zero dependency calculator library with first class support for units and
timezone conversions.

%package devel
%pkg_devel_files 

%files
%license LICENSE
%doc README.md
%{_libdir}/libnumen.so.*

%changelog
* Wed Aug 26 2026 Olivia <git@olivia.sh>
- Initial package
