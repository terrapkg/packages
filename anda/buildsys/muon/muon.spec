Name:           muon
Version:        0.6.0
Release:        1%{?dist}
Summary:        A meson-compatible build system

# https://git.sr.ht/~lattis/muon/tree/master/item/LICENSES
License:        GPL-3.0-only AND Apache-2.0 AND Unlicense AND MIT AND Python-2.0
URL:            https://muon.build/
Source:         https://git.sr.ht/~lattis/muon/archive/%{version}.tar.gz
Patch0:         fix-dladdr-feature-macro.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  glibc-devel
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  scdoc
BuildRequires:  git-core
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libb2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  python3-pyyaml
BuildRequires:  mandoc
BuildRequires:  mdbook

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep
%autosetup -p1

%conf
%meson --wrap-mode=nofallback -Dtracy=disabled

%build
%meson_build

%install
%meson_install

%files
%license LICENSES/
%doc README.md
%{_bindir}/muon
%{_mandir}/man1/muon*
%{_mandir}/man5/meson*
%{_mandir}/man3/meson-reference.3.*

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com> - VERSION-RELEASE
- Update for 0.6.0 by removing the multilingual patch

* Mon Apr 20 2026 Owen Zimmerman <owen@fyralabs.com>
- Update spec, add tracy patch
