%global commit 15f77807a5f617341bd36f69174ea00f5550d131
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-protostar
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Prototype application launcher for Stardust XR
URL:            https://github.com/StardustXR/protostar
Source0:        %url/archive/%commit/protostar-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       protostar stardust-protostar
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

%files
%doc README.md
%license LICENSE
%_bindir/app_grid
%_bindir/hexagon_launcher
%_bindir/single
%_bindir/sirius
%_datadir/protostar/

%changelog
* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR protostar
