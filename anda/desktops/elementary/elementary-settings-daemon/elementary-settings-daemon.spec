%global srcname settings-daemon
%global appname io.elementary.settings-daemon
%global iface   io.elementary.SettingsDaemon.AccountsService

Name:           elementary-settings-daemon
Version:        8.1.0
Release:        1%?dist
Summary:        Settings Daemon and Portal for Pantheon
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/settings-daemon
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(packagekit-glib2)

Requires:       xdg-desktop-portal

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %appname


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%post
%systemd_user_post %{appname}.xdg-desktop-portal.service
%systemd_post %{appname}.check-for-firmware-updates.timer


%preun
%systemd_user_preun %{appname}.xdg-desktop-portal.service
%systemd_preun %{appname}.check-for-firmware-updates.timer


%files -f %appname.lang
%license LICENSE
%doc README.md

%config(noreplace) %{_datadir}/applications/%{appname}.desktop

%{_bindir}/%{appname}

%{_libexecdir}/%{appname}.xdg-desktop-portal

%{_datadir}/accountsservice/interfaces/%{iface}.xml
%{_datadir}/dbus-1/interfaces/%{iface}.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.settings-daemon.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/xdg-desktop-portal/portals/%{appname}.portal

%{_userunitdir}/%{appname}.xdg-desktop-portal.service
%{_unitdir}/%{appname}.check-for-firmware-updates.service
%{_unitdir}/%{appname}.check-for-firmware-updates.timer

%{_sysconfdir}/xdg/autostart/%appname.desktop


%changelog
%autochangelog
