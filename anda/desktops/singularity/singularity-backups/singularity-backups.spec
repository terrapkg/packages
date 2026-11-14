%global commit 5ca13d0540013664f35107ab1315afd2a7e4762e
%global commit_date 20261016
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           singularity-backups
Summary:        Backups Scheduler for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/singularityos-lab/singularity-backups
Source0:        %url/archive/%commit/singularity-backups-%commit.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(singularity-1.0)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Backups Scheduler for the Singularity Desktop Environment:
runs scheduled backups in the background.

%prep
%autosetup -C

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/singularity-backups
%{_sysconfdir}/xdg/autostart/dev.sinty.backups.daemon.desktop
%{_libdir}/singularity/plugins/backups-status/backups-status.plugin
%{_libdir}/singularity/plugins/backups-status/libbackups-status.so
%{_libexecdir}/singularity-backups-cloud
%{_libexecdir}/singularity-backups-cpak
%{_libexecdir}/singularity-backups-daemon
%{_libexecdir}/singularity-backups-system-helper
%{_appsdir}/dev.sinty.backups.desktop
%{_datadir}/dbus-1/services/dev.sinty.backups.Daemon.service
%{_datadir}/dbus-1/services/dev.sinty.backups.service
%{_datadir}/glib-2.0/schemas/dev.sinty.backups.gschema.xml
%{_scalableiconsdir}/dev.sinty.backups.svg
%{_datadir}/polkit-1/actions/dev.sinty.backups.policy
%{_datadir}/singularity/app-settings/dev.sinty.backups.json
%{_datadir}/singularity/backups.conf
%{_datadir}/singularity/backups/destinations/cloud.backup-destination
%{_datadir}/singularity/backups/sources/cpak.backup-source
%{_datadir}/singularity/files-actions/dev.sinty.backups.browse.ini
%{_datadir}/singularity/files-actions/dev.sinty.backups.versions.ini

%changelog
* Sat Oct 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
