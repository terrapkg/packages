Name:           plasma6-applet-appgrid
Version:        1.9.3
Release:        1%{?dist}
Summary:        A modern application launcher for KDE Plasma
# Main code: GPL-2.0-or-later
# dev.xarbit.appgrid.metainfo.xml: CC0-1.0
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://appgrid.xarbit.dev
Packager:       hilltty <49129010+hilltty@users.noreply.github.com>
Source0:        https://github.com/xarbit/plasma6-applet-appgrid/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)
BuildRequires:  cmake(AppStreamQt)

Requires:       plasma-workspace
Requires:       plasma-desktop
Requires:       kf6-kiconthemes
Requires:       kf6-ksvg

%description
A modern application launcher for KDE Plasma. It offers unified
search, favorites, categories, and both a panel and a centered popup
presentation.

%prep
%autosetup -n %{name}-%{version}

%conf
%cmake -DAPPGRID_VERSION_OVERRIDE=%{version}

%build
%cmake_build

%install
%cmake_install
%find_lang dev.xarbit.appgrid

%files -f dev.xarbit.appgrid.lang
%license LICENSE
%doc README.md
%{_qt6_plugindir}/plasma/applets/dev.xarbit.appgrid.so
%{_qt6_plugindir}/plasma/applets/dev.xarbit.appgrid.panel.so
%{_metainfodir}/dev.xarbit.appgrid.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/dev.xarbit.appgrid.svg

%changelog
* Mon Jun 15 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.9.1-2
- Sync with upstream

* Fri May 29 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.8.5-1
- pass version to cmake, update description

* Mon May 25 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.8.0-1
- fix: add cmake(PlasmaActivities) BuildRequires, add icon to files

* Tue May 19 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.7.10-1
- Sync with upstream: add icon to files, update Requires, update URL

* Sat Apr 25 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.7.8-1
- Update to 1.7.8

* Fri Apr 24 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.2.1-1
- Initial package
