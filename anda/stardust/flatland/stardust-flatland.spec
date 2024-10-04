%global commit 0914dd3df54a5e6258dfc0a02d65af1c0fc0fc90
%global commit_date 20240920
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-flatland
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Flatland for Stardust XR.
URL:            https://github.com/StardustXR/flatland
Source0:        %url/archive/%commit/flatland-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       flatland
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n flatland-%commit
%cargo_prep_online

%build
STARDUST_RES_PREFIXES=/usr/share

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
STARDUST_RES_PREFIXES=%_datadir
%cargo_install

%files
%_bindir/flatland
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Flatland
