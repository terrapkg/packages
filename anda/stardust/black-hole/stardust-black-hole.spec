%global commit 0b847b6ddc383bfcc1e133a2238a37ce8202fe95
%global commit_date 20240824
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$ 

Name:           stardust-black-hole
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Spatial storage for stardust xr.
URL:            https://github.com/StardustXR/black-hole
Source0:        %url/archive/%commit/black-hole-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       black-hole
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n black-hole-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install

%files
%_bindir/black-hole
%license LICENSE
%doc README.md

%changelog
* Sat Sep 8 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR black-hole
