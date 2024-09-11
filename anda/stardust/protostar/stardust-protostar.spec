%global commit 39499a061af74c3a2d5e1e46e4ad21aca5727219
%global commit_date 20240719
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-protostar
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Tools you can easily snap together to get non-spatial input into stardust.
URL:            https://github.com/StardustXR/protostar
Source0:        %url/archive/%commit/protostar-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       protostar
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Tools you can easily snap together to get non-spatial input into stardust.

%prep
%autosetup -n protostar-%commit
%cargo_prep_online

%build

%install
cd protostar
%cargo_install

%files
%_bindir/protostar
%license LICENSE
%doc README.md

%changelog
* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR protostar
