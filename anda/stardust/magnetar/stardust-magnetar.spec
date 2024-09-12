%global commit 48064b84b71d27ceea00b5d2f19dcbf21d75f554
%global commit_date 20240831
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-magnetar
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Workspaces client for Stardust.
URL:            https://github.com/StardustXR/magnetar
Source0:        %url/archive/%commit/magnetar-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       magnetar
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n magnetar-%commit
%cargo_prep_online

%build

%install
%cargo_install


%files
%_bindir/magnetar
%license LICENSE
%doc README.md

%changelog
* Wed Sep 11 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR magnetar

