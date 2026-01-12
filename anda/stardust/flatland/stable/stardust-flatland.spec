# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-flatland
Version:        0.50.1
Release:        1%?dist
Epoch:          1
Summary:        Flatland for Stardust XR
URL:            https://github.com/StardustXR/flatland
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       flatland stardust-flatland
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n flatland-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies


%files
%_bindir/flatland
%_datadir/flatland/
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Flatland
