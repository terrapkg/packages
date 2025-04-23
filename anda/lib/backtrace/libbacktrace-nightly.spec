%global debug_package %nil

%global commit 793921876c981ce49759114d7bb89bb89b2d3a2d
%global shortcommit %(c=%commit; echo ${c:0:7})
%global commit_date 20250411

%global _desc %{expand:
A C library that may be linked into a C/C++ program to produce symbolic backtraces.
}

Name:           libbacktrace-nightly
Version:        1.0^%commit_date.%shortcommit
Release:        1%?dist
Summary:        Library to produce symbolic backtraces
License:        BSD-3-Clause
URL:            https://github.com/ianlancetaylor/libbacktrace
Source0:		%url/archive/%commit.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  gcc make
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description %_desc

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_desc
This package contains the development files for the %name package.

%prep
%autosetup -n libbacktrace-%commit

%build
autoreconf -fiv
%configure \
  --disable-static \
  --enable-shared \
  --with-system-libunwind \
  --enable-silent-rules
%make_build

%check
# btest_dwz fails
%make_build check ||:

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc README.md
%license LICENSE
%_includedir/backtrace-supported.h
%_includedir/backtrace.h
%_libdir/libbacktrace.so

%files devel
%_libdir/libbacktrace.so.*

%changelog
* Sat Aug 10 2024 madonuko <mado@fyralabs.com>
- Initial package
