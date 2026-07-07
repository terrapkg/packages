Name:           vibepanel
Version:        0.15.0
Release:        1%{?dist}
Summary:        GTK4 panel for Wayland with notifications, OSD, and quick settings – between a status bar and a desktop shell
URL:            https://github.com/prankstr/vibepanel
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        %{sourcelicense} AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  rust
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel

Requires:       gtk4
Requires:       gtk4-layer-shell
Requires:       pulseaudio-libs
Requires:       upower
Requires:       NetworkManager
Requires:       bluez

Recommends:     power-profiles-daemon

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n vibepanel-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/rpm/vibepanel %{buildroot}%{_bindir}/vibepanel
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/vibepanel
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package vibepanel
