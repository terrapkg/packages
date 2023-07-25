%global forgeurl https://gitlab.com/ubports/development/core/qtmir
# The commit Debian uses so no need for mirclient, not from mainline but ubports/focal_-_mir2.0
%global commit bd21224b0fcd3edeaa56e5ccb90ac57a1785352d
%forgemeta

Name:          qtmir
Version:       0.8.0
Release:       %autorelease
Summary:       Mir backed compositor using Qt

License:       LGPLv3+ AND GPLv3+
URL:           https://gitlab.com/ubports/development/core/qtmir
Source0:       %{url}/-/archive/%commit/qtmir-%commit.tar.gz
Patch0:        https://sources.debian.org/data/main/q/qtmir/0.8.0~git20230223.bd21224-3/debian/patches/1003_require-miroil-in-pkgconfig-file.patch
#Patch1:        https://gitlab.com/ubports/development/core/qtmir/-/commit/24351ad41224fdbf2a42dbda6c380a54e4631ab5.patch

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Sensors)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(mirserver)
BuildRequires: pkgconfig(mir-renderer-gl-dev)
BuildRequires: pkgconfig(miral)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(lomiri-url-dispatcher)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(lttng-ust)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(valgrind)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: cmake(Qt5FontDatabaseSupport)
BuildRequires: qt-devel
# Not in pkgconfig
BuildRequires: properties-cpp-devel
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: glm-devel
BuildRequires: boost-devel

Requires:      process-cpp
Requires:      xorg-x11-server-Xwayland

%description
Mir backed compositor using QT which is used in Lomiri.

%package devel
Summary:  Qtmir development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for qtmir.

%package demo
Summary: Qtmir demos
Requires: %{name}%{?_isa} = %{version}-%{release}

%description demo
This package contains development files needed for qtmir.

%prep
%autosetup -n qtmir-%commit -p1
sed -i 's!X-Ubuntu-Touch=true!X-Lomiri-Splash-Show=false!' data/xwayland.qtmir.desktop

%build
%cmake -DWerror=OFF -DWITH_MIR2=on -DWITH_CONTENTHUB=OFF

%cmake_build

%install
%cmake_install

%files
%doc README
%license COPYING COPYING.LESSER
%{_libdir}/libqtmirserver.so.*
%{_qt5_plugindir}/platforms/libqpa-mirserver.so
%dir %{_qt5_qmldir}/QtMir
%dir %{_qt5_qmldir}/QtMir/Application
%{_qt5_qmldir}/QtMir/Application/libqtmirapplicationplugin.so
%{_qt5_qmldir}/QtMir/Application/qmldir
%{_datadir}/applications/xwayland.qtmir.desktop
%{_datadir}/icons/hicolor/256x256/apps/xwayland.qtmir.png
%{_datadir}/glib-2.0/schemas/com.canonical.qtmir.gschema.xml

%files devel
%{_libdir}/libqtmirserver.so
%{_libdir}/pkgconfig/qtmirserver.pc
%dir %{_includedir}/qtmir
%dir %{_includedir}/qtmir/qtmir
%{_includedir}/qtmir/qtmir/*.h

%files demo
%{_bindir}/qtmir-demo-*
%{_datadir}/applications/qtmir-demo-client.desktop
%dir %{_datadir}/qtmir
%dir %{_datadir}/qtmir/benchmarks
%{_datadir}/qtmir/benchmarks/*.py
%{_datadir}/qtmir/benchmarks/*.R
%dir %{_datadir}/qtmir/qtmir-demo-client
%{_datadir}/qtmir/qtmir-demo-client/*.qml
%dir %{_datadir}/qtmir/qtmir-demo-shell
%{_datadir}/qtmir/qtmir-demo-shell/*.qml
%{_datadir}/qtmir/qtmir-demo-shell/*.png

%changelog
%autochangelog
