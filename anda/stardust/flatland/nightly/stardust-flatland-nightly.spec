%global commit b2031190cd241292289bfd4f6dd33d1950761e9a
%global commit_date 20260203
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-flatland-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Flatland for Stardust XR
URL:            https://github.com/StardustXR/flatland
Source0:        %url/archive/%commit/flatland-%commit.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only AND ISC AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       flatland-nightly stardust-flatland-nightly
Conflicts:      stardust-xr-flatland
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n flatland-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/
%{cargo_license_online} > LICENSE.dependencies


%files
%_bindir/flatland
%_datadir/flatland/
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
