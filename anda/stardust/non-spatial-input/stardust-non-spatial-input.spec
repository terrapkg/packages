%global commit 5ac7f04f6876097aa8c3cf9af033d609a8a49944
%global commit_date 20240824
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           stardust-non-spatial-input
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Tools you can easily snap together to get non-spatial input into stardust.
URL:            https://github.com/StardustXR/non-spatial-input
Source0:        https://github.com/StardustXR/non-spatial-input/archive/%commit/non-spatial-input-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel
Requires:       libgcc glibc 

Provides:       non-spatial-input
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Tools you can easily snap together to get non-spatial input into stardust.

%prep
%autosetup -n non-spatial-input-%commit
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%files
%_bindir/non-spatial-input
%license LICENSE
%doc README.md

%changelog
* Mon Sep 9 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR non-spatial-input
