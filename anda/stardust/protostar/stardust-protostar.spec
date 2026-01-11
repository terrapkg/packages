# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-protostar
Version:        0.50.0
Release:        1%?dist
Epoch:          1
Summary:        Prototype application launcher for Stardust XR
URL:            https://github.com/StardustXR/protostar
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
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

%cargo_license_summary_online
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
