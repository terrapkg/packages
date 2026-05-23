%dnl %undefine __brp_mangle_shebangs

Name:           vibepanel
Version:        0.14.1
Release:        1%{?dist}
Summary:        GTK4 panel for Wayland with notifications, OSD, and quick settings – between a status bar and a desktop shell
URL:            https://github.com/prankstr/vibepanel
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        %{sourcelicense}

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
install -Dm 755 target/release/vibepanel %{buildroot}%{_bindir}/vibepanel
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/vibepanel
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package vibepanel
