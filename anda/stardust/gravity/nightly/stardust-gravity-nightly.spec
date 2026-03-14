%global commit 3283bf8b352cdcb04ef3e0edb5155c4ca8c5c97c
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-gravity-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Utility to launch apps and Stardust XR clients spatially
URL:            https://github.com/StardustXR/gravity
Source0:        %url/archive/%commit/gravity-%commit.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause-Patent AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       gravity-nightly stardust-gravity-nightly
Conflicts:      stardust-xr-gravity
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n gravity-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/gravity
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
