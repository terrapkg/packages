Name:           darkly
Version:        0.5.38
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        Forked from the lightly theme, this style brings a fresh and unique look to your applications
URL:            https://github.com/Bali10050/Darkly
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kdecoration-devel

Requires:       hicolor-icon-theme
Requires:       kdecoration
Requires:       qt6-qtdeclarative
Requires:       kf6-kcoreaddons
Requires:       kf6-kcmutils
Requires:       kf6-kcolorscheme
Requires:       kf6-kconfig
Requires:       kf6-kguiaddons
Requires:       kf6-kiconthemes
Requires:       kf6-kwindowsystem
Requires:       kf6-frameworkintegration
Requires:       kf6-plasma

%description
%{summary}.

%package devel
Summary:       Development files for %{name}
Requires:      %{name} = %{evr}

%description   devel
This package contains the development libraries for %{name}.


%prep
%autosetup -n Darkly-%{version}

%conf
%cmake -DBUILD_QT6=ON \
       -DBUILD_QT5=OFF

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_bindir}/darkly-settings6
%{_appsdir}/darklystyleconfig.desktop
%{_appsdir}/kcm_darklydecoration.desktop
%{_datadir}/color-schemes/Darkly.colors
%{_scalableiconsdir}/darkly-settings.svgz
%{_datadir}/kservices6/darklydecorationconfig.desktop
%{_datadir}/kstyle/themes/darkly.themerc
%{_datadir}/plasma/desktoptheme/darkly/*

%files devel
%{_libdir}/cmake/Darkly/
%{_qt6_plugindir}/kstyle_config/darklystyleconfig.so
%{_qt6_plugindir}/org.kde.kdecoration3/org.kde.darkly.so
%{_qt6_plugindir}/org.kde.kdecoration3.kcm/kcm_darklydecoration.so
%{_qt6_plugindir}/styles/darkly6.so

%changelog
* Tue Jun 02 2026 Owen Zimmerman <owen@fyralabs.com> - 0.5.37-1
- Initial commit
