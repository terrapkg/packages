%global ver 2024-09-07
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
%_bindir/ruffle_desktop
%_datadir/applications/ruffle_desktop.desktop
%_iconsdir/hicolor/scalable/apps/ruffle_desktop.svg

%prep
%autosetup -n ruffle-nightly-%ver
%cargo_prep_online

cat<<EOF > ruffle_desktop.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Ruffle Desktop
Comment=%summary
Exec=%_bindir/ruffle_desktop
Icon=ruffle_desktop
Terminal=false
StartupNotify=false
Categories=Application;
MimeType=application/x-shockwave-flash;
EOF

%build
%{cargo_license_online} > LICENSE.dependencies

%install
cd desktop
%cargo_install
install -Dm644 assets/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/ruffle_desktop.svg
install -Dm644 ../ruffle_desktop.desktop %buildroot%_datadir/applications/ruffle_desktop.desktop

%changelog
* Mon Jul 29 2024 madonuko <mado@fyralabs.com>
- Initial package
