%global commit 8ad02b636690170adbd4279fe3fc8265088cbcc2
%global commit_date 20240726
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-armillary
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Model viewer for Stardust XR.
URL:            https://github.com/StardustXR/armillary
Source0:        %url/archive/%commit/armillary-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold
Requires:       libgcc glibc

Provides:       armillary
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A model viewer for Stardust XR which works great for hand tracking, pointers, and controllers.

%prep
%autosetup -n armillary-%commit
%cargo_prep_online

%build

%install
%cargo_install

%files
%_bindir/armillary
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR armillary
