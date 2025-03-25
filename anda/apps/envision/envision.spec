%global commit 1ed031a2bf25c81ba3795e42c5b063779bb391bf
%global commit_date 20250214
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           envision-nightly
Version:        %commit_date.%shortcommit
Release:        2%?dist
Summary:        UI for building, configuring and running Monado, the open source OpenXR runtime
SourceLicense:  AGPL-3.0-or-later
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND AGPL-3.0-or-later AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
URL:            https://gitlab.com/gabmus/envision/
Source0:        %url/-/archive/%commit/envision-%commit.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.72.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  openxr-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  git-core
Recommends:     android-tools
Conflicts:      envision

%description
%summary.

%prep
%autosetup -n envision-%commit
%cargo_prep_online

%build
# generate constants.rs from constants.rs.in
%meson

# skip subdir
sed -E "/^subdir\('src'\)/d" -i meson.build

%meson --reconfigure
%meson_build

%install
%meson_install
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/envision
%_datadir/applications/org.gabmus.envision.Devel.desktop
%_datadir/envision/
%_iconsdir/hicolor/scalable/apps/org.gabmus.envision.Devel.svg
%_iconsdir/hicolor/symbolic/apps/org.gabmus.envision.Devel-symbolic.svg
%_metainfodir/org.gabmus.envision.Devel.appdata.xml
