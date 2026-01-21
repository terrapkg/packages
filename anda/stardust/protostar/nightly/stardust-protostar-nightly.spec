%global commit 7609cbfc07121b3b68d91bf2124b9c0afa57363d
%global commit_date 20251218
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-protostar-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Prototype application launcher for Stardust XR
URL:            https://github.com/StardustXR/protostar
Source0:        %url/archive/%commit/protostar-%commit.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause-Patent AND BSD-2-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND ISC AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       protostar-nightly stardust-protostar-nightly
Conflicts:      stardust-xr-protostar
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Prototype application launcher for StardustXR, providing an easy to use crate to write applications launchers.

%prep
%autosetup -n protostar-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
(cd app_grid && %cargo_install) &
(cd hexagon_launcher && %cargo_install) &
(cd single && %cargo_install) &
(cd sirius && %cargo_install) &

wait

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/

%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/hexagon_launcher
%_bindir/single
%_bindir/sirius
%_datadir/protostar/

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
