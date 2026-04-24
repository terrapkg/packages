Name:           plasma6-applet-appgrid
Version:        1.2.1
Release:        1%{?dist}
Summary:        A modern application launcher for KDE Plasma, inspired by macOS and COSMIC
# Main code: GPL-2.0-or-later
# dev.xarbit.appgrid.metainfo.xml: CC0-1.0
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://github.com/xarbit/plasma6-applet-appgrid
Packager:       hilltty <49129010+hilltty@users.noreply.github.com>
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace)

Requires:       plasma-workspace
Requires:       kf6-kservice
Requires:       kf6-ki18n
Requires:       kf6-kcoreaddons
Requires:       kf6-kio
Requires:       kf6-kwindowsystem
Requires:       layer-shell-qt

%description
AppGrid is a modern application launcher for KDE Plasma 6, inspired by
macOS Launchpad, COSMIC, and Pantheon.

%prep
%autosetup -n plasma6-applet-appgrid-%{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install
%find_lang dev.xarbit.appgrid --with-kde

%files -f dev.xarbit.appgrid.lang
%license LICENSE
%doc README.md
%{_libdir}/qt6/plugins/plasma/applets/dev.xarbit.appgrid.so
%{_libdir}/qt6/plugins/plasma/applets/dev.xarbit.appgrid.panel.so
%{_datadir}/plasma/plasmoids/dev.xarbit.appgrid/
%{_datadir}/plasma/plasmoids/dev.xarbit.appgrid.panel/
%{_metainfodir}/dev.xarbit.appgrid.metainfo.xml

%changelog
* Thu Apr 24 2026 hilltty <49129010+hilltty@users.noreply.github.com> - 1.2.1-1
- Initial package
