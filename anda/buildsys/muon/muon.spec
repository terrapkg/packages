Name:           muon
Version:        0.5.0
Release:        1%?dist
Summary:        A meson-compatible build system

# https://git.sr.ht/~lattis/muon/tree/master/item/LICENSES
License:        GPL-3.0-only AND Apache-2.0 AND Unlicense AND MIT AND Python-2.0
URL:            https://muon.build/
Source:         https://git.sr.ht/~lattis/muon/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  scdoc
BuildRequires:  git-core
BuildRequires:  tracy

%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep
%autosetup

%conf
%meson -Ddocs=disabled

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/muon
%{_mandir}/man1/muon*
%{_mandir}/man5/meson*

%changelog
* Mon Apr 20 2026 Owen Zimmerman <owen@fyralabs.com>
- Update spec
