Name:           kwin-winlike-gestures
Version:        1.0.0
Release:        1%{?dist}
Summary:        Configurable Windows like 3/4-finger touchpad gestures
License:        GPL-2.0-or-later
URL:            https://github.com/LiberaTeMetuMortis/kwin-winlike-gestures
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildSystem:    cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(KWin)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libdrm)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Configurable Windows like 3/4-finger touchpad gestures
for KDE Plasma 6 Wayland: a KWin plugin with its own System Settings page.

%conf -a
%cmake_kf6

%files
%license LICENSE
%doc README.md
%{_qt6_plugindir}/kwin/plugins/winlikegestures.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_winlikegestures.so
%{_kf6_datadir}/applications/kcm_winlikegestures.desktop
%{_kf6_datadir}/qlogging-categories6/kwin_winlike_gestures.categories

%changelog
* Wed Nov 25 2026 Owen Zimmerman <owen@fyralabs.com> - 1.0.0-1
- Initial commit
