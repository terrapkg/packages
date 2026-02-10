%global ver 0.0.10

Name:          holyc
Version:       %{ver}~beta
Release:       1%{?dist}
Summary:       HolyC compiler and transpiler
License:       BSD-2-Clause
URL:           https://holyc-lang.com
Source0:       https://github.com/Jamesbarford/holyc-lang/archive/refs/tags/beta-v%{ver}.tar.gz
BuildRequires: cmake
BuildRequires: cmake-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
Packager:      Gilver E. <roachy@fyralabs.com>

%description
HolyC is a fun recreational programming language designed by Terry A. Davis.
Originally implemented in TempleOS as a general purpose programming language and scripting language for all manner of tasks.

%prep
%autosetup -n %{name}-lang-beta-v%{ver}/src

%build
%cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DHCC_LINK_SQLITE3="1"
%cmake_build

%install
%cmake_install

%files
%license ../COPYING
%doc ../README.md
%{_bindir}/hcc
%{_includedir}/tos.HH

%changelog
* Tue Feb 10 2026 Gilver E. <roachy@fyralabs.com> - 0.0.10~beta-1
- Initial package
