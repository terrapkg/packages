# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-armillary
Version:        0.50.0
Release:        1%?dist
Epoch:          1
Summary:        Model viewer for Stardust XR
URL:            https://github.com/StardustXR/armillary
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       armillary stardust-armillary
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A model viewer for Stardust XR which works great for hand tracking, pointers, and controllers.

%prep
%autosetup -n armillary-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/armillary
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR armillary
