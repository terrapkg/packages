%global forgeurl https://gitlab.com/ubports/development/core/lib-cpp/process-cpp
%global commit ee6d99a3278343f5fdcec7ed3dad38763e257310
%forgemeta

Name:          process-cpp
Version:       3.0.2
Release:       %autorelease
Summary:       A simple convenience library for handling processes in C++

License:       LGPL-3.0-or-later
URL:           https://gitlab.com/ubports/development/core/lib-cpp/process-cpp
Source0:       %{url}/-/archive/%commit/process-cpp-%commit.tar.gz
Patch0:        https://sources.debian.org/data/main/p/process-cpp/3.0.1-9/debian/patches/2001-Don-t-run-tests.patch
Patch1:        https://sources.debian.org/data/main/p/process-cpp/3.0.1-9/debian/patches/1002-Reproducible-documentation.patch
Patch3:        https://sources.debian.org/data/main/p/process-cpp/3.0.1-9/debian/patches/1004-spelling-fixes.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(properties-cpp)
#BuildRequires: pkgconfig(Backtrace)
BuildRequires: doxygen


%description
A simple convenience library for handling processes in C++11.

%package devel
Summary:  process-cpp development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for process-cpp.

%package doc
Summary:   process-cpp documentation files
BuildArch: noarch

%description doc
This package contains documentation files for process-cpp.

%prep
%autosetup -n process-cpp-%commit -p1

%build
sed -i '/find_package(PkgConfig REQUIRED)/a set(THREADS_PREFER_PTHREAD_FLAG ON)' CMakeLists.txt
%cmake -DPROCESS_CPP_WERROR=OFF

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_libdir}/libprocess-cpp.so.*

%files devel
%{_libdir}/libprocess-cpp.so
%{_libdir}/pkgconfig/process-cpp.pc
%dir %{_includedir}/core/testing
%{_includedir}/core/testing/*.h
%dir %{_includedir}/core/posix
%{_includedir}/core/posix/*.h
%dir %{_includedir}/core/posix/linux
%dir %{_includedir}/core/posix/linux/proc
%dir %{_includedir}/core/posix/linux/proc/process
%{_includedir}/core/posix/linux/proc/process/*.h

%files doc
%dir %{_docdir}/process-cpp
%dir %{_docdir}/process-cpp/html
%{_docdir}/process-cpp/html/*.html
%{_docdir}/process-cpp/html/*.map
%{_docdir}/process-cpp/html/*.css
%{_docdir}/process-cpp/html/*.png
%{_docdir}/process-cpp/html/*.js
%{_docdir}/process-cpp/html/*.md5
%{_docdir}/process-cpp/html/*.svg

%changelog
%autochangelog
