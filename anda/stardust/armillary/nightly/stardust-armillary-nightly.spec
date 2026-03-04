%global commit c278020dc78587e887f91377a882b50d0b009c50
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-armillary-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Model viewer for Stardust XR
URL:            https://github.com/StardustXR/armillary
Source0:        %url/archive/%commit/armillary-%commit.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND BSD-3-Clause AND LGPL-2.1-or-later AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       armillary-nightly stardust-armillary-nightly
Conflicts:      stardust-xr-armillary
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A model viewer for Stardust XR which works great for hand tracking, pointers, and controllers.

%prep
%autosetup -n armillary-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/armillary
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
