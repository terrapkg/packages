%global commit af38adafe7491498c48905b77518f8a6e9541f67
%global commit_date 20251202
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-atmosphere-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Environment, homespace, and setup client for Stardust XR
URL:            https://github.com/StardustXR/atmosphere
Source0:        %url/archive/%commit/atmosphere-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       atmosphere-nightly stardust-atmosphere-nightly
Conflicts:      stardust-xr-atmosphere
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n atmosphere-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/stardust-xr-atmosphere
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
