%define commit 93c50a7e8fbc88d15c17efe26eacdce2c616bded

Name:           latte-dock
Version:        0.10.9
Release:        %autorelease
Summary:        Replacement dock for Plasma desktops, providing an elegant and intuitive experience for your tasks and plasmoids
License:        GPLv2+
URL:            https://invent.kde.org/plasma/latte-dock
Source0:        https://github.com/KDE/latte-dock/archive/%{commit}.tar.gz
Requires:       plasma-framework kirigami hicolor-icon-theme plasma-wayland-protocols
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  xcb-util-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  git
BuildRequires:  gettext
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  libSM-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-kirigami-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-devel
Recommends:     %{name}-lang

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%prep
%autosetup -n latte-dock-%{commit}

%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSES/*
/usr/bin/latte-dock
/usr/lib/debug/usr/lib64/qt5/plugins/kpackage/packagestructure/latte_indicator.so-0.10.9-1.fc37.x86_64.debug
/usr/lib/debug/usr/lib64/qt5/plugins/plasma/containmentactions/plasma_containmentactions_lattecontextmenu.so-0.10.9-1.fc37.x86_64.debug
/usr/lib64/qt5/plugins/kpackage/packagestructure/latte_indicator.so
/usr/lib64/qt5/plugins/plasma/containmentactions/plasma_containmentactions_lattecontextmenu.so
/usr/lib64/qt5/qml/org/kde/latte/*
/usr/share/applications/org.kde.latte-dock.desktop
/usr/share/dbus-1/interfaces/org.kde.LatteDock.xml
/usr/share/icons/breeze/applets/256/org.kde.latte.plasmoid.svg
/usr/share/icons/hicolor/*/apps/latte-dock.svg
/usr/share/knotifications5/lattedock.notifyrc
/usr/share/knsrcfiles/latte-indicators.knsrc
/usr/share/knsrcfiles/latte-layouts.knsrc
/usr/share/kservicetypes5/latte-indicator.desktop
/usr/share/latte/*
/usr/share/metainfo/org.kde.latte-dock.appdata.xml
/usr/share/metainfo/org.kde.latte.plasmoid.appdata.xml
/usr/share/metainfo/org.kde.latte.shell.appdata.xml
/usr/share/plasma/plasmoids/org.kde.latte.*
/usr/share/plasma/shells/org.kde.latte.shell/*
/usr/share/locale/*/LC_MESSAGES/latte-dock.mo
/usr/share/locale/*/LC_MESSAGES/latte_indicator_org.kde.latte.*.mo
/usr/share/locale/*/LC_MESSAGES/plasma_applet_org.kde.latte.*.mo
/usr/share/locale/*/LC_MESSAGES/plasma_containmentactions_lattecontextmenu.mo


%changelog
* Sun Dec 25 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
