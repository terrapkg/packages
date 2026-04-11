%global commit 7b4d0f49351a60d1f93d48f081b4c0e35e10fa6d
%global shortcommit %{sub %{commit} 0 7}
%global commitdate 20260325

Name:             steamos-manager-powerstation
Version:          0~%{commitdate}.git%{shortcommit}
Release:          3%{?dist}
Summary:          SteamOS Manager is a system daemon that aims to abstract Steam's interactions with the operating system
License:          MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (Apache-2.0 OR BSL-1.0) AND Apache-2.0 OR MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND (LGPL-2.1 OR MIT OR Apache-2.0) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:              https://github.com/OpenGamingCollective/steamos-manager
Source0:          %{url}/archive/%{commit}.tar.gz
Source1:          steamos_manager.te
Source2:          steamos_manager.if
Source3:          steamos_manager.fc
BuildRequires:    anda-srpm-macros
BuildRequires:    cargo-rpm-macros
BuildRequires:    clang-devel
BuildRequires:    rust
BuildRequires:    mold
BuildRequires:    glib2-devel
BuildRequires:    speech-dispatcher-devel
BuildRequires:    pkgconfig(libudev)
BuildRequires:    selinux-policy-devel
Packager:         Kyle Gospodnetich <me@kylegospodneti.ch>

Provides:         steamos-manager
Conflicts:        steamos-manager
Requires:         powerstation
Requires:         gamescope-session-ogui-steam
Requires:         selinux-policy
Requires(post):   policycoreutils
Requires(postun): policycoreutils

%description
SteamOS Manager is a system daemon that aims to abstract Steam's interactions
with the operating system. The goal is to have a standardized interface so that
SteamOS specific features in the Steam client, e.g. TDP management, can be
exposed in any Linux distro that provides an implementation of this DBus API.
This version has been patched with additional compatibility with powerstation
and OGC gamescope-sessions.

%package gamescope-session-plus
Summary:        Compatibility symlink service for starting steamos-manager on gamescope-session-plus
Requires:       %{name} = %{evr}

%description gamescope-session-plus
%summary.

%prep
%autosetup -n steamos-manager-%{commit}
install -Dp -m644 -t data/selinux %{SOURCE1} %{SOURCE2} %{SOURCE3}
%cargo_prep_online

%build
%cargo_build
make -f /usr/share/selinux/devel/Makefile -C data/selinux steamos_manager.pp

%install
%{cargo_license_online -a} > LICENSE.dependencies
%make_install
rm %{buildroot}%{_unitdir}/sddm.service.d/reset-oneshot-boot.conf # steamOS specific
rm %{buildroot}%{_userunitdir}/orca.service # not used by anyone apparently, steamOS specific(?)
install -D -m644 data/selinux/steamos_manager.pp %{buildroot}%{_datadir}/selinux/packages/steamos_manager.pp
install -d %{buildroot}%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service
ln -s %{_userunitdir}/steamos-manager.service %{buildroot}%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service

%post
%systemd_post steamos-manager.service
%systemd_user_post steamos-manager.service
%systemd_user_post steamos-manager-configure-cecd.service
%systemd_user_post steamos-manager-session-cleanup.service
semodule -i %{_datadir}/selinux/packages/steamos_manager.pp 2>/dev/null || :
restorecon -R /usr/lib/steamos-manager /usr/bin/steamosctl /usr/share/steamos-manager /etc/steamos-manager 2>/dev/null || :

%preun
%systemd_preun steamos-manager.service
%systemd_user_preun steamos-manager.service
%systemd_user_preun steamos-manager-configure-cecd.service
%systemd_user_preun steamos-manager-session-cleanup.service

%postun
%systemd_postun_with_restart steamos-manager.service
%systemd_user_postun steamos-manager.service
%systemd_user_postun steamos-manager-configure-cecd.service
%systemd_user_postun steamos-manager-session-cleanup.service
if [ $1 -eq 0 ]; then
    semodule -r steamos_manager 2>/dev/null || :
fi

%files
%license %{_datadir}/licenses/steamos-manager/LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/steamosctl
#{_datadir}/dbus-1/interfaces/com.steampowered.SteamOSManager1.Manager.xml
%{_datadir}/dbus-1/interfaces/com.steampowered.SteamOSManager1.xml
%{_datadir}/dbus-1/services/com.steampowered.SteamOSManager1.service
%{_datadir}/dbus-1/system.d/com.steampowered.SteamOSManager1.conf
%{_datadir}/dbus-1/system-services/com.steampowered.SteamOSManager1.service
%{_datadir}/steamos-manager/devices/*.toml
%{_datadir}/steamos-manager/platform.toml
%{_prefix}/lib/steamos-manager
%{_unitdir}/steamos-manager.service
%{_userunitdir}/steamos-manager.service
%{_userunitdir}/steamos-manager-configure-cecd.service
%{_userunitdir}/steamos-manager-session-cleanup.service
%{_datadir}/selinux/packages/steamos_manager.pp

%files gamescope-session-plus
%{_userunitdir}/gamescope-session-plus.service.wants/steamos-manager.service

%changelog
* Wed Mar 18 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 26.0.1-1
- Intial Commit
