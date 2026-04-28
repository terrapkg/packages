%global ver 0.0.10

Name:          holyc
Version:       %{ver}~beta
Release:       3%{?dist}
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
# Currently needed to fetch the commit hash for hcc --version
%git_clone https://github.com/Jamesbarford/holyc-lang.git beta-v%{ver}
%setup -T -D -n holyc-lang/src
# Make packaged versions of HolyC report the correct Git hash
sed -i 's|git rev-parse main|git rev-parse HEAD|g' CMakeLists.txt
# Make the binary correctly report its installed location as /usr/bin instead of /usr
sed -i 's|binary: %%s/hcc|binary: %%s/bin/hcc|g' cli.c

%build
%cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DHCC_LINK_SQLITE3="1"
%cmake_build

%install
%cmake_install

%check
%{buildroot}%{_bindir}/hcc --version

%files
%license ../COPYING
%doc ../README.md
%{_bindir}/hcc
%{_includedir}/tos.HH

%changelog
* Tue Feb 10 2026 Gilver E. <roachy@fyralabs.com> - 0.0.10~beta-1
- Initial package
