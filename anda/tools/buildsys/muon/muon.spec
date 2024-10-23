Name:           muon
Version:        0.3.1
Release:        1%?dist
Summary:        A meson-compatible build system

# muon is licensed under the GPL version 3 (see LICENSE). Tests under tests/project were copied from the meson project tests and are licensed under Apache 2.0.
License:        GPL-3.0 AND Apache-2.0
URL:            https://muon.build/
Source:         https://git.sr.ht/~lattis/muon/archive/%version.tar.gz

# we need meson for the macros
BuildRequires:  meson ninja-build
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  scdoc
BuildRequires:  american-fuzzy-lop

%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep
%autosetup

%build
./bootstrap.sh build-stage1
build-stage1/muon setup build-stage2
ninja -C build-stage2

%global __meson build-stage2/muon
%meson -Dtracy=disabled -Dmeson_tests_repo=disabled
%meson_build

%install
%meson_install

%files
%_bindir/muon
%{_mandir}/man1/muon*
%{_mandir}/man5/meson*
