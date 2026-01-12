# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-comet
Version:        0.50.0
Release:        1%?dist
Epoch:          1
Summary:        Annotate things in Stardust XR
URL:            https://github.com/StardustXR/comet
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       comet stardust-comet
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n comet-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/comet
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Sat Sep 7 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR comet
