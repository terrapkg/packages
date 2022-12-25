Name:           latte-dock
Version:        0.10.8
Release:        %autorelease
Summary:        Replacement dock for Plasma desktops, providing an elegant and intuitive experience for your tasks and plasmoids
License:        GPLv2+
URL:            https://invent.kde.org/plasma/latte-dock
Source0:        https://github.com/KDE/latte-dock/archive/refs/tags/v%{version}.tar.gz
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

%package lang
Summary: Translation files for latte-dock
Requires: %{name} = %{version}-%{release}
%description lang
%{summary}.

%prep
%autosetup -n latte-dock-%{version}

%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSES/*
/usr/bin/latte-dock
/usr/lib/debug/usr/bin/latte-dock-*.debug
/usr/lib/debug/usr/lib64/qt5/plugins/kpackage/packagestructure/latte_packagestructure_indicator.so-*.debug
/usr/lib/debug/usr/lib64/qt5/plugins/plasma_containmentactions_lattecontextmenu.so-*.debug
/usr/lib/debug/usr/lib64/qt5/qml/org/kde/latte/core/liblattecoreplugin.so-*.debug
/usr/lib/debug/usr/lib64/qt5/qml/org/kde/latte/private/containment/liblattecontainmentplugin.so-*.debug
/usr/lib/debug/usr/lib64/qt5/qml/org/kde/latte/private/tasks/liblattetasksplugin.so-*.debug
/usr/lib64/qt5/plugins/kpackage/packagestructure/latte_packagestructure_indicator.so
/usr/lib64/qt5/plugins/plasma_containmentactions_lattecontextmenu.so
/usr/lib64/qt5/qml/org/kde/latte/*
/usr/share/applications/org.kde.latte-dock.desktop
/usr/share/dbus-1/interfaces/org.kde.LatteDock.xml
/usr/share/icons/breeze/applets/256/org.kde.latte.plasmoid.svg
/usr/share/icons/hicolor/*/apps/latte-dock.svg
/usr/share/knotifications5/lattedock.notifyrc
/usr/share/knsrcfiles/latte-indicators.knsrc
/usr/share/knsrcfiles/latte-layouts.knsrc
/usr/share/kservices5/plasma-applet-org.kde.latte.containment.desktop
/usr/share/kservices5/plasma-applet-org.kde.latte.plasmoid.desktop
/usr/share/kservices5/plasma-containmentactions-lattecontextmenu.desktop
/usr/share/kservices5/plasma-shell-org.kde.latte.shell.desktop
/usr/share/kservicetypes5/latte-indicator.desktop
/usr/share/latte/indicators/default/metadata.desktop
/usr/share/latte/indicators/default/package/config/config.qml
/usr/share/latte/indicators/default/package/config/main.xml
/usr/share/latte/indicators/default/package/ui/main.qml
/usr/share/latte/indicators/org.kde.latte.plasma/*
/usr/share/latte/indicators/org.kde.latte.plasmatabstyle/*
/usr/share/metainfo/org.kde.latte-dock.appdata.xml
/usr/share/metainfo/org.kde.latte.plasmoid.appdata.xml
/usr/share/metainfo/org.kde.latte.shell.appdata.xml
/usr/share/plasma/plasmoids/org.kde.latte.*
/usr/share/plasma/shells/org.kde.latte.shell/*


%changelog
* Sun Dec 25 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
