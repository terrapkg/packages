%global commit 0c8bfb91e8ca32a4895f858067334ed265517309
%global commit_date 20240822
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-atmosphere
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Environment, homespace, and setup client for Stardust XR.
URL:            https://github.com/StardustXR/atmosphere
Source0:        %url/archive/%commit/atmosphere-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       atmosphere
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n atmosphere-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install

%files
%_bindir/atmosphere
%license LICENSE
%doc README.md

%changelog
* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR atmosphere
