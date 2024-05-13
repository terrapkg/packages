%global forgeurl https://github.com/KDE/latte-dock/

%global commit 10be08a7940b86d1cdca963a01542c92b064c7bd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date %(date '+%Y%m%d')
%global snapshot_info %{commit_date}.%{shortcommit}

Name:     latte-dock-nightly
Version:  0.10.0^%{snapshot_info}

%forgemeta
Release:  1%?dist
Summary:  Latte is a dock based on plasma frameworks
License:  GPL-2.0-or-later

URL:      %{forgeurl}
Source0:  https://github.com/KDE/latte-dock/archive/%{commit}.tar.gz

BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libSM-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kitemmodels-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  wayland-devel
BuildRequires:  plasma-workspace-devel

Recommends:     %{name}-lang

Conflicts:      latte-dock
Provides:       latte-dock = 0.10.0^%{snapshot_info}
Provides:       latte-dock%{?_isa} = 0.10.0^%{snapshot_info}

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%package lang
Summary: Translation files for latte-dock
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description lang
%{summary}.

%prep
%{forgesetup}
%autosetup -n %{archivename}

%build
%cmake_kf5 \
  -Wno-dev

%cmake_build
%install

%cmake_install
%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_bindir}/latte-dock
%{_datadir}/metainfo/org.kde.latte-dock.appdata.xml
%{_datadir}/metainfo/org.kde.latte.plasmoid.appdata.xml
%{_datadir}/metainfo/org.kde.latte.shell.appdata.xml
%{_kf5_datadir}/applications/org.kde.latte-dock.desktop
%{_kf5_datadir}/dbus-1/interfaces/org.kde.LatteDock.xml
%{_kf5_datadir}/icons/breeze/*/*/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/knotifications5/lattedock.notifyrc
%{_kf5_datadir}/kservicetypes5/latte-indicator.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.plasmoid/
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.containment/
%{_kf5_datadir}/plasma/shells/org.kde.latte.shell/
%{_kf5_datadir}/latte
%{_kf5_datadir}/knsrcfiles/latte-indicators.knsrc
%{_kf5_datadir}/knsrcfiles/latte-layouts.knsrc
%{_kf5_qmldir}/org/kde/latte
%{_qt5_plugindir}/kpackage/packagestructure/latte_indicator.so
%{_qt5_plugindir}/plasma/containmentactions/plasma_containmentactions_lattecontextmenu.so

%files lang -f %{name}.lang

%changelog
* Sun Dec 25 2022 lleyton <lleyton@fyralabs.com> - 0.10.0^20221226.93c50a7-1
- Comply with packaging policy
* Sun Dec 25 2022 windowsboy111 <windowsboy111@fyralabs.com> - 0.10.9-1
- Initial package

