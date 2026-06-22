%global app_id dk.yumex.Yumex
%global app_build release

Name:     yumex
Version:  5.4.0
Release:  1%{?dist}
Summary:  Yum Extender graphical package management tool

Packager: Jacob Secunda <secundaja@gmail.com>

Group:    Applications/System
License:  GPL-3.0-or-later
URL:      https://github.com/timlau/yumex-ng
Source0:  %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:  %{app_id}-updater.desktop

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: meson
BuildRequires: blueprint-compiler >= 0.4.0
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: systemd-rpm-macros

Requires: python3-gobject
Requires: libadwaita >= 1.6
Requires: gtk4
Requires: python3-dbus
Requires: flatpak-libs > 1.15.0
Requires: appstream >= 1.0.2

Recommends: %{name}-updater

# dnf5 requirements
Requires: dnf5daemon-server >= 5.2.12
Provides: yumex-dnf5 = %{evr}
Obsoletes: yumex-dnf5 < %{evr}

%description
Graphical package tool for maintain packages on the system.

%package -n %{name}-updater
Summary:  Yum Extender update notifier app
Requires: %{name} = %{evr}
Requires: python3-gobject
Requires: gtk3
Requires: python3-dbus
Requires: flatpak-libs > 1.15.0
Requires: libappindicator-gtk3

Provides: yumex-dnf5-updater-systray = %{evr}
Obsoletes: yumex-dnf5-updater-systray < %{evr}
Provides: yumex-updater-systray = %{evr}
Obsoletes: yumex-updater-systray < %{evr}

%description -n %{name}-updater
Checks for and notifies when updates are available.

%prep
%autosetup

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{app_id}.desktop
%desktop_file_validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{app_id}-updater.desktop

%conf
%meson --buildtype=%{app_build}

%build
%meson_build

%install
%meson_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/%{app_id}-updater.desktop

%find_lang %{name}

%files -f  %{name}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_appsdir}/%{app_id}*.desktop
%{_scalableiconsdir}/dk.yumex.Yumex.svg
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml

%files -n %{name}-updater
%ghost %{_userunitdir}/%{name}-updater.service
%ghost %{_userpresetdir}/*%{name}-updater.preset
%{_bindir}/yumex_updater
%{_scalableiconsdir}/yumex-update-*.svg
%{_sysconfdir}/xdg/autostart/%{app_id}-updater.desktop

%changelog
* Tue Jun 23 2026 Jacob Secunda <secundaja@gmail.com> - 5.4.0-1
- Initial package
