%global commit f01f810714443d0f10c333d4d1d9c0383be41375
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20201007

Name:           xdgpp
Version:        0^%commitdate.%shortcommit
Release:        1%{?dist}
License:        MIT
Summary:        C++17 header-only implementation of the XDG Base Directory Specification
URL:            https://git.sr.ht/~danyspin97/xdgpp
Source:         %{url}/archive/%{commit}.tar.gz
Packager:       metcya <metcya@gmail.com>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%pkg_libs_files

%package devel
Requires:       %{name}%{?_isa} = %{evr}
%pkg_devel_files

%description
%summary.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%changelog
* Sat Dec 27 2025 metcya <metcya@gmail.com>
- Initial package 

