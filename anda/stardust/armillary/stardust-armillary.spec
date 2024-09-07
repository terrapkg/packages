%global commit 8ad02b636690170adbd4279fe3fc8265088cbcc2
%global commit_date 20240726
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           stardust-armillary
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Model viewer for Stardust XR.
URL:            https://github.com/StardustXR/armillary
Source0:        https://github.com/StardustXR/armillary/archive/%commit/armillary-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold
Requires:       libgcc glibc

Provides:       armillary
Conflicts:      armillary

%description
A model viewer for Stardust XR which works great for hand tracking, pointers, and controllers.

%prep
%autosetup -n flatland-%commit
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%files
%_bindir/flatland
%license LICENSE
%doc README.md

%changelog
* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR armillary
