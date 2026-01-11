# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-black-hole
Version:        0.50.0
Release:        1%?dist
Epoch:          1
Summary:        Spatial storage for Stardust XR
URL:            https://github.com/StardustXR/black-hole
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       black-hole stardust-black-hole
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n black-hole-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install
%cargo_license_summary_online
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
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Sat Sep 8 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR black-hole
