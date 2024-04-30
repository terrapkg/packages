Name:           klassy

%global forgeurl https://github.com/paulmcauley/%{name}
%global tag 6.1.breeze6.0.3
%global date 20240411
%forgemeta

Version:        %{tag}
Release:        1%?dist
Summary:        Window Decoration, Application Style and Global Theme plugin for recent versions of the KDE Plasma desktop.
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            %{forgeurl}
Source:         %{forgesource}

Obsoletes:      classikstyles <= %{version}
Obsoletes:      classik <= %{version}

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.102.0

BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-filesystem

BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-filesystem

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

%description
Klassy (formerly ClassiK/ClassikStyles) is a highly customizable binary Window Decoration, Application Style and Global Theme plugin for recent versions of the KDE Plasma desktop. Initially taking inspiration from the iconography of KDE 1, the Klassy defaults are an attempt to create a usable and appealing look for the modern Plasma desktop.

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt

%{_bindir}/%{name}-settings

%{_libdir}/cmake/Klassy/

%{_libdir}/libklassycommon5.so.*
%{_libdir}/libklassycommon6.so.*

%{_kf5_qtplugindir}/styles/klassy5.so
%{_kf6_qtplugindir}/styles/klassy6.so

%{_kf6_qtplugindir}/kstyle_config/klassystyleconfig.so
%{_kf6_qtplugindir}/org.kde.kdecoration2/org.kde.klassy.so
%{_kf6_qtplugindir}/org.kde.kdecoration2.kcm/kcm_klassydecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration2.kcm/klassydecoration/presets/

%{_kf6_datadir}/applications/kcm_klassydecoration.desktop
%{_kf6_datadir}/applications/klassystyleconfig.desktop
%{_kf6_datadir}/applications/klassy-settings.desktop

%{_kf6_datadir}/color-schemes/Klassy*.colors

%{_datadir}/icons/hicolor/
%{_datadir}/icons/%{name}/
%{_datadir}/icons/%{name}-dark/
%{_datadir}/plasma/desktoptheme/%{name}/

%{_kf6_datadir}/kstyle/themes/%{name}.themerc

%{_kf6_datadir}/plasma/layout-templates/org.kde.klassy.*
%{_kf6_datadir}/plasma/look-and-feel/org.kde.klassy*

%changelog
%autochangelog

