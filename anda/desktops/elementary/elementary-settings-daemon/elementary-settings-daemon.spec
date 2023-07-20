%global srcname settings-daemon
%global appname io.elementary.settings-daemon
%global iface   io.elementary.SettingsDaemon.AccountsService

Name:           elementary-settings-daemon
Version:        1.2.0
Release:        1%{?dist}
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


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post
%systemd_user_post %{appname}.xdg-desktop-portal.service


%preun
%systemd_user_preun %{appname}.xdg-desktop-portal.service


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_libexecdir}/%{appname}.xdg-desktop-portal

%{_datadir}/accountsservice/interfaces/%{iface}.xml
%{_datadir}/dbus-1/interfaces/%{iface}.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.settings-daemon.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/xdg-desktop-portal/portals/%{appname}.portal

%{_userunitdir}/%{appname}.xdg-desktop-portal.service


%changelog
%autochangelog
