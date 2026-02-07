Name:           steamos-manager
Version:        25.12.0
Release:        1%?dist
Summary:        SteamOS Manager is a system daemon that aims to abstract Steam's interactions with the operating system.
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND Apache-2.0 OR BSL-1.0 AND Apache-2.0 OR MIT AND Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND BSD-3-Clause OR MIT OR Apache-2.0 AND ISC AND LGPL-2.1 OR MIT OR Apache-2.0 AND MIT AND MIT OR Apache-2.0 AND MIT OR Apache-2.0 OR LGPL-2.1-or-later AND Unlicense OR MIT AND Zlib OR Apache-2.0 OR MIT
URL:            https://gitlab.steamos.cloud/holo/steamos-manager
Source0:        %url/-/archive/v%version/steamos-manager-v%version.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  rust
BuildRequires:  mold
BuildRequires:  glib2-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  pkgconfig(libudev)
Packager:       Tulip Blossom <tulilirockz@outlook.com>

%description
SteamOS Manager is a system daemon that aims to abstract Steam's interactions
with the operating system. The goal is to have a standardized interface so that
SteamOS specific features in the Steam client, e.g. TDP management, can be
exposed in any Linux distro that provides an implementation of this DBus API.

%package gamescope-session-plus
Summary:        Compatibility symlink service for starting steamos-manager on gamescope-session-plus
Requires:       %{name} = %{evr}

%description gamescope-session-plus
%summary.

%prep
%autosetup -n %name-v%version
%cargo_prep_online

%build
%cargo_build

%install
%{cargo_license_online -a} > LICENSE.dependencies
%make_install
rm %{buildroot}%{_unitdir}/sddm.service.d/reset-oneshot-boot.conf # steamOS specific
rm %{buildroot}%{_userunitdir}/orca.service # not used by anyone apparently, steamOS specific(?)
install -d %{buildroot}%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service
%{__ln_s} -f %{buildroot}%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service %{_userunitdir}/steamos-manager.service

%post
%systemd_post steamos-manager.service

%preun
%systemd_preun steamos-manager.service

%postun
%systemd_postun_with_restart steamos-manager.service

%files
%license %{_datadir}/licenses/steamos-manager/LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/steamosctl
%{_datadir}/dbus-1/interfaces/com.steampowered.SteamOSManager1.Manager.xml
%{_datadir}/dbus-1/interfaces/com.steampowered.SteamOSManager1.xml
%{_datadir}/dbus-1/services/com.steampowered.SteamOSManager1.service
%{_datadir}/dbus-1/system.d/com.steampowered.SteamOSManager1.conf
%{_datadir}/dbus-1/system-services/com.steampowered.SteamOSManager1.service
%{_datadir}/steamos-manager/devices/*.toml
%{_datadir}/steamos-manager/platform.toml
%{_prefix}/lib/steamos-manager
%{_unitdir}/steamos-manager.service
%{_userunitdir}/steamos-manager.service
%{_userunitdir}/steamos-manager-session-cleanup.service

%files gamescope-session-plus
%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service

%changelog
* Wed Feb 04 2026 Tulip Blossom <tulilirockz@outlook.com> - 25.12.0-1
- Intial Commit
