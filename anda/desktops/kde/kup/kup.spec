%global _qt_major_version 6
%global ver kup-0.10.0
%global commit 130face33a7500b6f881cf8dc7114a2ba2ea1081

Name:			kup
Version:		%(echo %ver | sed -E 's/^kup-//')
Release:		1%?dist
Summary:		Backup scheduler for the Plasma desktop
License:		GPL-3.0-or-later WITH LicenseRef-KDE-Accepted-GPL
URL:			https://invent.kde.org/system/kup
Source0:        %url/-/archive/%ver.tar.gz
Packager:		madonuko <mado@fyralabs.com>
Requires:		(bup or rsync)
Suggests:		bup
BuildRequires:	cmake extra-cmake-modules
BuildRequires:	cmake(Qt%{_qt_major_version}Core)
BuildRequires:	cmake(Qt%{_qt_major_version}Widgets)
BuildRequires:	cmake(KF%{_qt_major_version}Solid)
BuildRequires:	cmake(KF%{_qt_major_version}KIO)
BuildRequires:	cmake(KF%{_qt_major_version}IdleTime)
BuildRequires:	cmake(KF%{_qt_major_version}I18n)
BuildRequires:	cmake(KF%{_qt_major_version}Notifications)
BuildRequires:	cmake(KF%{_qt_major_version}CoreAddons)
BuildRequires:	cmake(KF%{_qt_major_version}DBusAddons)
BuildRequires:	cmake(KF%{_qt_major_version}Config)
BuildRequires:	cmake(KF%{_qt_major_version}JobWidgets)
BuildRequires:	cmake(KF%{_qt_major_version}WidgetsAddons)
BuildRequires:	cmake(KF%{_qt_major_version}XmlGui)
BuildRequires:	cmake(KF%{_qt_major_version}KCMUtils)
BuildRequires:	cmake(KF%{_qt_major_version}Crash)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Plasma)
BuildRequires:	cmake(Plasma5Support)

%description
Kup is created for helping people to keep up-to-date backups of their personal files. Connecting a USB hard drive is the primary supported way to store files, but saving files to a server over a network connection is also possible for advanced users.

When you plug in your external hard drive Kup will automatically start copying your latest changes, but of course it will only do so if you have been active on your computer for some number of hours since the last time you took a backup (and it can of course ask you first, before copying anything).
In general Kup tries to not disturb you needlessly.

There are two types of backup schemes supported, one which keeps the backup folder completely in sync with what you have on your computer, deleting from the backup any file that you have deleted on your computer etc. The other scheme also keeps older versions of your files in the backup folder. When using this, only the small parts of your files that has actually changed since last backup will be saved and therefore incremental backups are very cheap. This is especially useful if you are working on big files. At the same time it's as easy to access your files as if a complete backup was taken every time; every backup contains a complete version of your directories. Behind the scenes all the content that is actually the same is only stored once. To make this happen Kup runs the backup program "bup" in the background, look at https://github.com/bup/bup for more details.

%prep
%autosetup -n %name-%ver-%commit
mv LICENSES/* .

%build
%cmake_kf6 \
   -DQT_MAJOR_VERSION=%{_qt_major_version} \
   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
   -DCMAKE_BUILD_TYPE=Release \
   -DBUILD_TESTING=OFF \
   -DKDE_INSTALL_USE_QT_SYS_PATHS=ON 
%cmake_build

%install
%cmake_install

%find_lang kup

%files -f kup.lang
%doc README.md
%license GPL-2.0-only.txt GPL-2.0-or-later.txt GPL-3.0-only.txt LicenseRef-KDE-Accepted-GPL.txt
%_sysconfdir/xdg/autostart/kup-daemon.desktop
%_bindir/kup-daemon
%_bindir/kup-filedigger
%_bindir/kup-purger
%_kf6_plugindir/kio/kio_bup.so
%_qt6_plugindir/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%_qt6_plugindir/plasma5support/dataengine/plasma_engine_kup.so
%_datadir/applications/kcm_kup.desktop
%_iconsdir/hicolor/scalable/apps/kup.svg
%_datadir/knotifications6/kupdaemon.notifyrc
%_metainfodir/org.kde.kup.appdata.xml
%_metainfodir/org.kde.kupapplet.appdata.xml
%_datadir/plasma/plasmoids/org.kde.kupapplet/contents/ui/FullRepresentation.qml
%_datadir/plasma/plasmoids/org.kde.kupapplet/contents/ui/main.qml
%_datadir/plasma/plasmoids/org.kde.kupapplet/metadata.json
%_datadir/plasma5support/services/kupdaemonservice.operations
%_datadir/plasma5support/services/kupservice.operations
%_datadir/qlogging-categories6/kup.categories
