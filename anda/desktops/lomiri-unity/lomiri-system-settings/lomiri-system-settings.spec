%global forgeurl https://gitlab.com/ubports/development/core/lomiri-system-settings
%global commit 73c2249ea78d2ca080ed907a9d60c18ce42db25f
%forgemeta

Name:       lomiri-system-settings
Version:    1.1.0
Release:    1%?dist
Summary:    The system settings application for Lomiri
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-system-settings
Source0:    %{url}/-/archive/%commit/lomiri-system-settings-%commit.tar.gz
Patch0:     https://sources.debian.org/data/main/l/lomiri-system-settings/1.1.0-4/debian/patches/2000_use-maliit-keyboard-for-language-plugin.patch
Patch1:     https://sources.debian.org/data/main/l/lomiri-system-settings/1.0.1-2/debian/patches/2001_disable-current-language-switching.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(icu-i18n)
#BuildRequires: pkgconfig(libandroid-properties)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: cmake(QmlPlugins)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Qml)
BuildRequires: qt5-qtbase-private-devel
Recommends:    suru-icon-theme
Requires:      maliit-keyboard
Requires:      ayatana-indicator-datetime
Requires:      lomiri-settings-components

%description
The system settings application (and library) for the Lomiri desktop enviroment.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n lomiri-system-settings-%commit -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/lomiri-system-settings
%{_libdir}/libLomiriSystemSettings.so.*
%{_libdir}/libLomiriSystemSettingsPrivate.so.*
%dir %{_libdir}/lomiri-system-settings
%{_libdir}/lomiri-system-settings/*.so
%dir %{_libdir}/lomiri-system-settings/private
%dir %{_libdir}/lomiri-system-settings/private/Lomiri
%{_libdir}/lomiri-system-settings/private/Lomiri/SystemSettings/
%{_datadir}/applications/lomiri-system-settings.desktop
%{_datadir}/glib-2.0/schemas/com.lomiri.lomiri-system-settings.gschema.xml
%dir %{_datadir}/lomiri-system-settings
%{_datadir}/lomiri-system-settings/*.settings
%{_datadir}/lomiri-system-settings/*.svg
%{_datadir}/lomiri-system-settings/*.png
%{_datadir}/lomiri-system-settings/url-map.ini
%dir %{_datadir}/lomiri-system-settings/icons
%{_datadir}/lomiri-system-settings/icons/*.svg
%{_datadir}/lomiri-system-settings/qml-plugins/
%{_datadir}/lomiri-url-dispatcher/urls/lomiri-system-settings.url-dispatcher

%files devel
%dir %{_includedir}/LomiriSystemSettings
%{_includedir}/LomiriSystemSettings/*.h
%{_includedir}/LomiriSystemSettings/ItemBase
%{_includedir}/LomiriSystemSettings/PluginInterface
%dir %{_includedir}/LomiriSystemSettings/private
%{_includedir}/LomiriSystemSettings/private/*.h
%{_libdir}/libLomiriSystemSettings.so
%{_libdir}/libLomiriSystemSettingsPrivate.so
%{_libdir}/pkgconfig/LomiriSystemSettings.pc

%changelog
%autochangelog
