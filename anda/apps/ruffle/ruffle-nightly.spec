%global ver 2024-07-29
%global goodver %(echo %ver | sed 's/-//g')
%global __brp_mangle_shebangs %{nil}
%bcond_without mold

%global _description %{expand:
Ruffle is an Adobe Flash Player emulator written in the Rust programming
language. Ruffle targets both the desktop and the web using WebAssembly.}

Name:           ruffle-nightly
Version:        %goodver
Release:        1%?dist
Summary:        A Flash Player emulator written in Rust
License:        Apache-2.0 OR MIT
URL:            https://ruffle.rs/
Source0:        https://github.com/ruffle-rs/ruffle/archive/refs/tags/nightly-%ver.tar.gz
Provides:       ruffle
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc-c++ cmake java
BuildRequires:  java-latest-openjdk-headless
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcb-cursor)
Packager:       madonuko <mado@fyralabs.com>

%description %_description

%files
%doc README.md
%license LICENSE.md
%license LICENSE.dependencies
%_bindir/ruffle

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%prep
%autosetup -n ruffle-nightly-%ver
%cargo_prep_online

%build
%{cargo_license_online} > LICENSE.dependencies

%install
cd desktop
%cargo_install

%changelog
* Mon Jul 29 2024 madonuko <mado@fyralabs.com>
- Initial package
