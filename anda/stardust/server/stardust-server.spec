%global commit 0c99dcb79ddeebf3449df6baa806cbba4111fd4f
%global commit_date 20251221
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-server
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/%commit/server-%commit.tar.gz
License:        GPL-2.0-only

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mold
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros

BuildRequires:  fontconfig-devel
BuildRequires:  glibc
BuildRequires:  openxr-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  wayland-devel

Provides:       stardust-server

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Usable Linux display server that reinvents human-computer interaction for all kinds of XR, from putting 2D/XR apps into various 3D shells for varying uses to SDF-based interaction.

%prep
%autosetup -n server-%commit
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/stardust-xr-server %{buildroot}%{_bindir}/stardust-xr-server
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/stardust-xr-server
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Tue Dec 02 2025 Owen Zimmerman <owen@fyralabs.com>
- Update spec to reflect upstream changes, add LICENSE.dependencies

* Sat Sep 14 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
