%global commit 96787ed3139717ea6061f6e259e9fed3e483274a
%global commit_date 20240821
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-gravity
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Utility to launch apps and Stardust XR clients spatially.
URL:            https://github.com/StardustXR/gravity
Source0:        %url/archive/%commit/gravity-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold  

Provides:       gravity
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n gravity-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install


%files
%_bindir/gravity
%license LICENSE
%doc README.md

%changelog
* Wed Sep 11 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR gravity
