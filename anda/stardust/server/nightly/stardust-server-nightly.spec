%global commit ccbd4e07d859d5373f57b88af0ff755b7838bfe0
%global commit_date 20260125
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-server-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/%commit/server-%commit.tar.gz
License:        GPL-2.0-only AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-2-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 GPL-2.0-only AND ISC AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MIT-0 AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (MIT OR Apache-2.0) AND (Zlib OR Apache-2.0 OR MIT)

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

Provides:       stardust-server-nightly
Conflicts:      stardust-xr-server

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
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/stardust-xr-server
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
