# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-protostar
Version:        0.50.0
Release:        2%?dist
Epoch:          1
Summary:        Prototype application launcher for Stardust XR
URL:            https://github.com/StardustXR/protostar
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause-Patent AND BSD-2-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND ISC AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       protostar stardust-protostar
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Prototype application launcher for StardustXR, providing an easy to use crate to write applications launchers.

%prep
%autosetup -n protostar-%version
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
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR protostar
