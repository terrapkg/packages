%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}

Name:           powerstation
Version:        0.7.0
Release:        2%{?dist}
Summary:        Daemon for controlling TDP and performance over DBus

License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/PowerStation
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>

ExcludeArch:    %{ix86}

BuildRequires:  rust-packaging
BuildRequires:  pciutils-devel
BuildRequires:  systemd-devel
BuildRequires:  clang
Requires:       dbus
Requires:       zlib-ng-compat

%description
Powerstation is a daemon for controlling TDP and performance over DBus.
It is designed for use on AMD platforms with access to libryzenadj.

%prep
%autosetup -n PowerStation-%{version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

# DBus system policy
install -Dm644 rootfs%_datadir/dbus-1/system.d/org.shadowblip.PowerStation.conf \
  -t %buildroot%_datadir/dbus-1/system.d

install -Dm644 rootfs%_unitdir/powerstation.service -t %buildroot%_unitdir

sed -i 's/After=graphical-session.target//g' %buildroot%_unitdir/powerstation.service

echo 'enable powerstation.service' | install -Dm644 /dev/stdin %buildroot%_presetdir/95-enable-powerstation.service

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%_bindir/powerstation
%_datadir/dbus-1/system.d/org.shadowblip.PowerStation.conf
%_unitdir/powerstation.service
%_presetdir/20-enable-powerstation.service

%post
%systemd_post powerstation.service

%preun
%systemd_preun powerstation.service

%postun
%systemd_postun_with_restart powerstation.service


%changelog
* Fri Jan 30 2026 madonuko <mado@fyralabs.com> - 0.7.0-1
- Ported from https://copr-dist-git.fedorainfracloud.org/packages/gloriouseggroll/nobara-43/powerstation.git/tree/powerstation.spec?h=f43
