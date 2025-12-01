%global commit 86e962eada5f9e5722c746f4eaab8e5aa087bbf4
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-comet
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Annotate things in Stardust XR
URL:            https://github.com/StardustXR/comet
Source0:        %url/archive/%commit/comet-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       comet stardust-comet
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n comet-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install

%files
%_bindir/comet
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR comet
