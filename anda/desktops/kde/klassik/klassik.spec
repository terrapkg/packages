Name:          klassik
Version:       1.0.0
Release:       1%{?dist}
Summary:       A modern recreation of the classic KDE 3 desktop experience for KDE Plasma 6
License:       GPL-3.0-or-later
URL:           https://github.com/neeeeow/Klassik
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:      Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kio-devel
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  libplasma-devel
BuildRequires:  plasma-activities-stats-devel
BuildRequires:  plasma-activities-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  libksysguard-devel
BuildRequires:  kdecoration-devel

Requires:       kwin

%description
%{summary}.

%prep
%autosetup -C -S git

%conf
%cmake_kf6

%build
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_qt6_plugindir}/org.kde.kdecoration3/com.github.neeeeow.klassik.kwin.kde2.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.clock.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.kmenu.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.lockout.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.panel.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.quicklaunch.so
%{_qt6_plugindir}/plasma/applets/com.github.neeeeow.klassik.taskmanager.so
%{_qt6_plugindir}/styles/com.github.neeeeow.klassik.qstyle.so
%{_datadir}/color-schemes/BeOS.colors
%{_datadir}/color-schemes/CDE.colors
%{_datadir}/color-schemes/DigitalCDE.colors
%{_datadir}/color-schemes/KDEOne.colors
%{_datadir}/color-schemes/KDETwo.colors
%{_datadir}/color-schemes/Keramik.colors
%{_datadir}/color-schemes/KeramikEmerald.colors
%{_datadir}/color-schemes/KeramikWhite.colors
%{_datadir}/color-schemes/Plastik.colors
%{_datadir}/color-schemes/SolarisCDE.colors
%{_datadir}/plasma/desktoptheme/klassik/dialogs/background.svg
%{_datadir}/plasma/desktoptheme/klassik/metadata.json
%{_datadir}/plasma/desktoptheme/klassik/widgets/background.svg
%{_datadir}/plasma/desktoptheme/klassik/widgets/panel-background.svg
%{_datadir}/plasma/desktoptheme/klassik/widgets/tooltip.svg
%{_datadir}/plasma/layout-templates/com.github.neeeeow.klassik.panel.default/contents/layout.js
%{_datadir}/plasma/layout-templates/com.github.neeeeow.klassik.panel.default/metadata.json
%{_datadir}/plasma/look-and-feel/com.github.neeeeow.klassik.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/com.github.neeeeow.klassik.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%{_datadir}/plasma/look-and-feel/com.github.neeeeow.klassik.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/com.github.neeeeow.klassik.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/com.github.neeeeow.klassik.desktop/metadata.json
%{_datadir}/wallpapers/andes-venezolanos/contents/images/3840x2880.png
%{_datadir}/wallpapers/andes-venezolanos/metadata.json
%{_datadir}/wallpapers/blue-bend/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/blue-bend/metadata.json
%{_datadir}/wallpapers/default_blue/contents/images/1024x768.jpg
%{_datadir}/wallpapers/default_blue/metadata.json
%{_datadir}/wallpapers/triplegears/contents/images/1280x1024.jpg
%{_datadir}/wallpapers/triplegears/metadata.json

%changelog
* Sat Oct 10 2026 Owen Zimmerman <cypress@fyralabs.com> - 1.0.0-1
- Initial commit
