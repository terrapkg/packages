Name:		kde-liquidshell
Version:	1.10.0
Release:	1%?dist
Summary:	Basic desktop shell using QtWidgets
Provides:	liquidshell = %version

License:	GPL-3.0
URL:		https://invent.kde.org/system/liquidshell
Source0:	https://download.kde.org/stable/liquidshell/liquidshell-%version.tar.xz

BuildRequires:	cmake
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(Qt5)
BuildRequires:	kf5-rpm-macros
BuildRequires:	extra-cmake-modules
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtbase-static
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5BluezQt)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	pkgconfig(packagekitqt5)
Requires:	kwin
Requires:	plasma-workspace-x11
Requires:	plasma-workspace
Recommends:	polkit-kde

%description
liquidshell is a basic Desktop Shell implemented using QtWidgets.

%prep
%autosetup -n liquidshell-%version

%build
%cmake_kf5 -DWITH_PACKAGEKIT=true
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc README
%license COPYING
%{_bindir}/liquidshell
%{_bindir}/start_liquidshell
%{_datadir}/applications/org.kde.liquidshell.desktop
%{_datadir}/icons/hicolor/48x48/apps/liquidshell.png
%{_datadir}/knotifications5/liquidshell.notifyrc
%{_metainfodir}/org.kde.liquidshell.appdata.xml
%{_datadir}/xsessions/liquidshell-session.desktop
%{_datadir}/locale/*/LC_MESSAGES/liquidshell.mo

%changelog
%autochangelog
