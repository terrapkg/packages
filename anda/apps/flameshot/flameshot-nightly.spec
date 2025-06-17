#? https://github.com/flameshot-org/flameshot/blob/master/packaging/rpm/fedora/flameshot.spec

%global ver 12.1.0
%global commit d420a53a4a61cb39842ee632fb8183ab07b58879
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20250617
%global devel_name QtColorWidgets

Name:			flameshot.nightly
Version:		%ver^%{commit_date}git.%shortcommit
Release:		2%?dist
License:		GPL-3.0-or-later AND ASL-2.0 AND GPL-2.0-only AND LGPL-3.0-only AND FAL-1.3
Summary:		Powerful yet simple to use screenshot software
URL:			https://flameshot.org
%dnl Source0:		https://github.com/flameshot-org/flameshot/archive/%commit/flameshot-%commit.tar.gz
Packager:  madonuko <mado@fyralabs.com>

BuildRequires:	cmake >= 3.13.0
BuildRequires:	gcc-c++ >= 7
BuildRequires:	fdupes
BuildRequires:	libappstream-glib
BuildRequires:	ninja-build
BuildRequires:	desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

Requires:		hicolor-icon-theme
Requires:		qt6-qtbase 
Requires:		qt6-qttools 
Requires:		qt6-qtsvg%{?_isa} 

%dnl Provides:		flameshot = %version-%release
Conflicts:		flameshot

Recommends:		xdg-desktop-portal%{?_isa}
Recommends:		(xdg-desktop-portal-gnome%{?_isa} if gnome-shell%{?_isa})
Recommends:		(xdg-desktop-portal-kde%{?_isa} if plasma-workspace-wayland%{?_isa})
Recommends:		(xdg-desktop-portal-wlr%{?_isa} if wlroots%{?_isa})

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

Features:

 * Customizable appearance.
 * Easy to use.
 * In-app screenshot edition.
 * DBus interface.
 * Upload to Imgur


%pkg_completion -Bfz flameshot

%package devel
Summary:      Flameshot development files
Requires:     %{name} = %{version}

%description devel
Development files for Flameshot.

%prep
%git_clone https://github.com/flameshot-org/flameshot.git %commit

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
%cmake_build

%install
%cmake_install
# https://fedoraproject.org/wiki/PackagingDrafts/find_lang
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%{_datadir}/flameshot/translations/Internationalization_grc.qm
%doc README.md
%license LICENSE
%dir %{_datadir}/flameshot
%dir %{_datadir}/flameshot/translations
%{_bindir}/flameshot
%{_libdir}/lib%{devel_name}.so.*
%{_datadir}/applications/org.flameshot.Flameshot.desktop
%{_metainfodir}/org.flameshot.Flameshot.metainfo.xml
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/flameshot.1*

%files devel
%{_libdir}/lib%{devel_name}.so
%{_libdir}/cmake/%{devel_name}/
%{_libdir}/pkgconfig/%{devel_name}.pc
%{_includedir}/%{devel_name}/
