# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-non-spatial-input
Version:        0.50.0
Release:        2%?dist
Epoch:          1
Summary:        Tools you can easily snap together to get non-spatial input into Stardust XR
URL:            https://github.com/StardustXR/non-spatial-input
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND BSD-3-Clause AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold libudev-devel g++ libinput-devel libxkbcommon-x11-devel

Provides:       non-spatial-input stardust-non-spatial-input
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n non-spatial-input-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
(cd azimuth && %cargo_install) &
(cd eclipse && %cargo_install) &
(cd manifold && %cargo_install) &
(cd simular && %cargo_install) &

wait

%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/azimuth
%_bindir/eclipse
%_bindir/manifold
%_bindir/simular
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to version based

* Mon Sep 9 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR non-spatial-input
