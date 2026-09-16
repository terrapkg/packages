Name:          kwin-material-decoration
Version:       26.09.07
Release:       1%{?dist}
Summary:       Material-ish window decoration theme for KWin
License:       GPL-2.0-only
URL:           https://github.com/guiodic/material-decoration
Source0:       https://github.com/guiodic/material-decoration/archive/refs/tags/%{version}.tar.gz

Packager:      Cypress Reed <cypress@fyralabs.com>

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  pkgconfig(KF6CoreAddons)
BuildRequires:  pkgconfig(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  pkgconfig(KF6WindowSystem)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KWin)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  cmake(kf6kcmutils)

Requires:       kwin

%description
%summary.

%prep
%autosetup -C

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_qt6_plugindir}/org.kde.kdecoration3/materialdecoration.so
%{_qt6_plugindir}/org.kde.kdecoration3.kcm/materialdecoration_kcm.so
%{_appsdir}/materialdecoration_kcm.desktop
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/materialdecoration.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/materialdecoration.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/materialdecoration.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/materialdecoration.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/materialdecoration.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/materialdecoration.mo
%{_metainfodir}/materialdecoration_kcm.json

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
