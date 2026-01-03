# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-solar-sailer
Version:        0.50.0
Release:        1%?dist
Summary:        Glide through space! This play space mover allows you to fly by dragging the space with momentum!
URL:            https://github.com/StardustXR/solar-sailer
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        MIT
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold python3-devel

Provides:       solar-sailer stardust-solar-sailer
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary

%prep
%autosetup -n solar-sailer-%version
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
* Sat Jan 03 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
