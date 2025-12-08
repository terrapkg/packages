%global commit 10cf122d5c1ab9125562563eafe9e56dec10b674
%global commit_date 20251207
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-flatland
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Flatland for Stardust XR
URL:            https://github.com/StardustXR/flatland
Source0:        %url/archive/%commit/flatland-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       flatland stardust-flatland
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
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies


%files
%_bindir/flatland
%_datadir/flatland/
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Flatland
