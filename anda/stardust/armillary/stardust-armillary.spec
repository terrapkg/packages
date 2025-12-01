%global commit c278020dc78587e887f91377a882b50d0b009c50
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-armillary
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Model viewer for Stardust XR
URL:            https://github.com/StardustXR/armillary
Source0:        %url/archive/%commit/armillary-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       armillary stardust-armillary
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A model viewer for Stardust XR which works great for hand tracking, pointers, and controllers.

%prep
%autosetup -n armillary-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install

%files
%_bindir/armillary
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR armillary
