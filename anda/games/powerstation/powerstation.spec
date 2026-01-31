Name:           powerstation
Version:        0.7.0
Release:        1%{?dist}
Summary:        Daemon for controlling TDP and performance over DBus

SourceLicense:  GPL-3.0-or-later
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND GPL-3.0-or-later AND ISC AND LGPL-3.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/ShadowBlip/PowerStation
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>

ExcludeArch:    %{ix86}

BuildRequires:  rust-packaging
BuildRequires:  pciutils-devel
BuildRequires:  systemd-devel
BuildRequires:  clang cmake
Requires:       dbus
Requires:       zlib-ng-compat

%description
Powerstation is a daemon for controlling TDP and performance over DBus.
It is designed for use on AMD platforms with access to libryzenadj.

%prep
%autosetup -n PowerStation-%{version}
%cargo_prep_online

%build
%{cargo_build} --locked
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%crate_install_bin

# DBus system policy
install -Dm644 rootfs%_datadir/dbus-1/system.d/org.shadowblip.PowerStation.conf \
  -t %buildroot%_datadir/dbus-1/system.d

install -Dm644 rootfs%_unitdir/powerstation.service -t %buildroot%_unitdir

sed -i 's/After=graphical-session.target//g' %buildroot%_unitdir/powerstation.service

echo 'enable powerstation.service' | install -Dm644 /dev/stdin %buildroot%_presetdir/95-enable-powerstation.preset

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%_bindir/powerstation
%_datadir/dbus-1/system.d/org.shadowblip.PowerStation.conf
%_unitdir/powerstation.service
%_presetdir/95-enable-powerstation.preset

%post
%systemd_post powerstation.service

%preun
%systemd_preun powerstation.service

%postun
%systemd_postun_with_restart powerstation.service


%changelog
* Fri Jan 30 2026 madonuko <mado@fyralabs.com> - 0.7.0-1
- Ported from https://copr-dist-git.fedorainfracloud.org/packages/gloriouseggroll/nobara-43/powerstation.git/tree/powerstation.spec?h=f43
