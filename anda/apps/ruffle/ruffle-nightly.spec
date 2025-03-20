%global ver 2025-03-18
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
BuildRequires:  anda-srpm-macros mold
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
%_bindir/ruffle_desktop
%_datadir/applications/rs.ruffle.Ruffle.desktop
%_iconsdir/hicolor/scalable/apps/rs.ruffle.Ruffle.svg
%_metainfodir/rs.ruffle.Ruffle.metainfo.xml

%prep
%autosetup -n ruffle-nightly-%ver -p1
%cargo_prep_online
sed -iE 's@^Exec=ruffle %%u$@Exec=ruffle_desktop %%u@' desktop/packages/linux/rs.ruffle.Ruffle.desktop
cat desktop/packages/linux/rs.ruffle.Ruffle.desktop

%build
%{cargo_license_online} > LICENSE.dependencies

%install
cd desktop
%cargo_install
install -Dm644 packages/linux/rs.ruffle.Ruffle.svg %buildroot%_iconsdir/hicolor/scalable/apps/rs.ruffle.Ruffle.svg
install -Dm644 packages/linux/rs.ruffle.Ruffle.desktop %buildroot%_datadir/applications/rs.ruffle.Ruffle.desktop
install -Dm644 packages/linux/rs.ruffle.Ruffle.metainfo.xml %buildroot%_metainfodir/rs.ruffle.Ruffle.metainfo.xml

%changelog
* Mon Jul 29 2024 madonuko <mado@fyralabs.com>
- Initial package
