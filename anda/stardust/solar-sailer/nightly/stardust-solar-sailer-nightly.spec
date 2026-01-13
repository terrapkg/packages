%global commit 40ca9fc446756a5151275dcbac914cee399dbc4c
%global commit_date 20251218
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-solar-sailer-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Glide through space! This play space mover allows you to fly by dragging the space with momentum!
URL:            https://github.com/StardustXR/solar-sailer
Source0:        %url/archive/%commit.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT)
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold python3-devel

Provides:       solar-sailer-nightly stardust-solar-sailer-nightly
Conflicts:      stardust-xr-solar-sailer
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n solar-sailer-%commit
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/solar_sailer
%cargo_install
install -Dm644 res/solar_sailer/move_icon.glb %{buildroot}%{_datadir}/%{name}/solar_sailer/move_icon.glb
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/solar-sailer
%{_datadir}/%{name}/solar_sailer/move_icon.glb

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
