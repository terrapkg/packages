%global commit 01c666f472457ef6230c9d2fd5a289d0a64ce5c2
%global commit_date 20241230
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$ 

Name:           stardust-xr-black-hole
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Spatial storage for Stardust XR.
URL:            https://github.com/StardustXR/black-hole
Source0:        %url/archive/%commit/black-hole-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       black-hole stardust-black-hole
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n black-hole-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/

%files
%doc README.md
%license LICENSE
%_bindir/black-hole
%_datadir/black_hole/

%changelog
* Sat Sep 8 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR black-hole
