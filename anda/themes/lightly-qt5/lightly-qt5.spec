%global style Lightly
%global _style lightly
%global dev boehs
%global _qt_major_version 5
 
%global forgeurl https://github.com/%{dev}/%{style}
%global commit be5adc66bf3c7fe5038a42ba4dd6d5aed7544a46
%global date 20240217
 
%forgemeta
 
Name:           %{_style}-qt%{_qt_major_version}
Version:        0.43
Release:        %autorelease 
Summary:        A modern style for qt applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
 
URL:            %{forgeurl}
Source:         %{forgesource}
 
 
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= 5.78.0
 
BuildRequires:  kf%{_qt_major_version}-rpm-macros
BuildRequires:  kf%{_qt_major_version}-filesystem
 
BuildRequires:  cmake(Qt%{_qt_major_version}Core)
BuildRequires:  cmake(Qt%{_qt_major_version}DBus)
BuildRequires:  cmake(Qt%{_qt_major_version}Gui)
BuildRequires:  cmake(Qt%{_qt_major_version}Quick)
BuildRequires:  cmake(Qt%{_qt_major_version}UiTools)
BuildRequires:  cmake(Qt%{_qt_major_version}Widgets)
BuildRequires:  cmake(Qt%{_qt_major_version}X11Extras)
 
BuildRequires:  cmake(KF%{_qt_major_version}CoreAddons)
BuildRequires:  cmake(KF%{_qt_major_version}Config)
BuildRequires:  cmake(KF%{_qt_major_version}ConfigWidgets)
BuildRequires:  cmake(KF%{_qt_major_version}Crash)
BuildRequires:  cmake(KF%{_qt_major_version}FrameworkIntegration)
BuildRequires:  cmake(KF%{_qt_major_version}GuiAddons)
BuildRequires:  cmake(KF%{_qt_major_version}GlobalAccel)
BuildRequires:  cmake(KF%{_qt_major_version}I18n)
BuildRequires:  cmake(KF%{_qt_major_version}IconThemes)
BuildRequires:  cmake(KF%{_qt_major_version}Init)
BuildRequires:  cmake(KF%{_qt_major_version}KCMUtils)
BuildRequires:  cmake(KF%{_qt_major_version}KIO)
BuildRequires:  cmake(KF%{_qt_major_version}Kirigami2)
BuildRequires:  cmake(KF%{_qt_major_version}Notifications)
BuildRequires:  cmake(KF%{_qt_major_version}Package)
BuildRequires:  cmake(KF%{_qt_major_version}Plasma)
BuildRequires:  cmake(KF%{_qt_major_version}Wayland)
BuildRequires:  cmake(KF%{_qt_major_version}WindowSystem)
BuildRequires:  cmake(KDecoration2)
 
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
 
BuildRequires:  kwin-devel
BuildRequires:  libepoxy-devel
BuildRequires:  kf%{_qt_major_version}-kpackage-devel
 
Obsoletes:      %{_style} <= %{version}
 
%description
%{style} is a fork of breeze theme style that aims to be visually modern and minimalistic.
 
%prep
%forgeautosetup -p1
 
%build
%cmake_kf5 -DQT_MAJOR_VERSION=%{_qt_major_version} -DWITH_DECORATIONS=OFF
%cmake_build
 
%install
%cmake_install
 
# Remove files present in lightly-qt6
rm -rf %{buildroot}%{_datadir}/color-schemes
rm -rf %{buildroot}%{_datadir}/icons
rm -rf %{buildroot}%{_datadir}/kstyle
rm -rf %{buildroot}%{_libdir}/cmake/%{style}
 
%files
%license COPYING
%doc AUTHORS README.md
 
%{_bindir}/lightly-settings%{_qt_major_version}
 
%{_libdir}/kconf_update_bin/kde4%{_style}
%{_libdir}/lib%{_style}common%{_qt_major_version}.so.*
 
%{_qt5_plugindir}/kstyle_%{_style}_config.so
%{_qt5_plugindir}/styles/%{_style}.so
 
%{_datadir}/kconf_update/kde4%{_style}.upd
%{_datadir}/kservices%{_qt_major_version}/%{_style}styleconfig.desktop
 
%changelog
%autochangelog 
%autochangelog
