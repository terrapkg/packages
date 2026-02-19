#? https://github.com/flameshot-org/flameshot/blob/master/packaging/rpm/fedora/flameshot.spec

%global ver 13.3.0
%global commit 53d4da8fcd0e00b755b3329674b756d9777d3a89
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20260219
%global devel_name QtColorWidgets
%global _distro_extra_cflags -fuse-ld=mold
%global _distro_extra_cxxflags -fuse-ld=mold

Name:			flameshot.nightly
Version:		%ver^%{commit_date}git.%shortcommit
Release:		2%?dist
License:		GPL-3.0-or-later AND ASL-2.0 AND GPL-2.0-only AND LGPL-3.0-only AND FAL-1.3
Summary:		Powerful yet simple to use screenshot software
URL:			https://flameshot.org
Source0:		https://github.com/flameshot-org/flameshot/archive/%commit/flameshot-%commit.tar.gz
Packager:  madonuko <mado@fyralabs.com>

BuildRequires:	cmake >= 3.13.0
BuildRequires:	gcc-c++ >= 7
BuildRequires:	fdupes
BuildRequires:	libappstream-glib
BuildRequires:	ninja-build
BuildRequires:	desktop-file-utils
BuildRequires:	mold

BuildRequires:	cmake(Qt6Core) >= 6.0.0
BuildRequires:	cmake(KF6GuiAddons) >= 6.7.0
BuildRequires:	cmake(Qt6DBus) >= 6.0.0
BuildRequires:	cmake(Qt6Gui) >= 6.0.0
BuildRequires:	cmake(Qt6LinguistTools) >= 6.0.0
BuildRequires:	cmake(Qt6Network) >= 6.0.0
BuildRequires:	cmake(Qt6Svg) >= 6.0.0
BuildRequires:	cmake(Qt6Widgets) >= 6.0.0

Requires:		hicolor-icon-theme

Conflicts:		flameshot

Recommends:		qt6-qtimageformats
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

%pkg_completion -Bfz flameshot

%package devel
Requires:     %{name} = %{version}
%pkg_devel_files
%_libdir/cmake/*/

%package libs
%pkg_libs_files

%package static
%pkg_static_files

%prep
%autosetup -p1 -n flameshot-%commit

%build
export GIT_HASH=%commit
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON
%cmake_build

%install
%cmake_install
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/flameshot
%dir %{_datadir}/flameshot/translations
%{_bindir}/flameshot
%{_datadir}/applications/org.flameshot.Flameshot.desktop
%{_metainfodir}/org.flameshot.Flameshot.metainfo.xml
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/flameshot.1*
