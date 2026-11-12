%global commit 9e3c1e4446251098d5d5a08b42ebdb595df64323
%global commit_date 20261031
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-black-hole-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Spatial storage for Stardust XR
URL:            https://github.com/StardustXR/black-hole
Source0:        %url/archive/%commit/black-hole-%commit.tar.gz
SourceLicense:  MIT
License:        %{SourceLicense} AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT)
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros

Provides:       black-hole-nightly stardust-black-hole-nightly
Conflicts:      stardust-xr-black-hole
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n black-hole-%commit
%cargo_prep_online

%build

%install
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/black-hole
%_datadir/black_hole/

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
