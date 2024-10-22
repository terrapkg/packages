Name:           muon
Version:        0.3.1
Release:        1%?dist
Summary:        A meson-compatible build system

# muon is licensed under the GPL version 3 (see LICENSE). Tests under tests/project were copied from the meson project tests and are licensed under Apache 2.0.
License:        GPL-3.0 AND Apache-2.0
URL:            https://muon.build/
Source:         https://git.sr.ht/~lattis/muon/archive/%{version}.tar.gz

BuildRequires:  meson
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
%define __meson build-stage2/muon
%meson
%meson_build

%install
%define __meson build-stage2/muon
%meson_install

%files
/usr/bin/muon
%{_mandir}/man1/muon*
%{_mandir}/man5/meson*

%changelog
%autochangelog
