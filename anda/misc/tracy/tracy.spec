%global _desc Tracy is a real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.

Name:			tracy
Version:		0.10
Release:		1%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  cmake meson gcc gcc-c++ libxkbcommon dbus-devel libglvnd glfw-devel freetype-devel pkgconfig(capstone) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb)
Patch:          https://github.com/wolfpld/tracy/commit/1a971d867d6fa5bf6dc57d705dcbbc6020031e7a.patch

%description
%_desc


%package devel
Summary: Development files for the tracy package

%description devel
%_desc
This package contains the development files for the tracy package.


%prep
%autosetup -p1


%build
export CXX='g++ -fPIE -I/usr/include/freetype2/'
%meson
%meson_build
%make_build -C capture/build/unix release
%make_build -C csvexport/build/unix release
%make_build -C import-chrome/build/unix release
%make_build -C library/unix release
%make_build -C profiler/build/unix release
%make_build -C update/build/unix release


%install
%meson_install

install -Dm755 capture/build/unix/capture-release %buildroot%_bindir/tracy-capture
install -Dm755 csvexport/build/unix/csvexport-release %buildroot%_bindir/tracy-csvexport
install -Dm755 import-chrome/build/unix/import-chrome-release %buildroot%_bindir/tracy-import-chrome
install -Dm755 library/unix/libtracy-release.so %buildroot%_libdir/libtracy.so
install -Dm755 profiler/build/unix/Tracy-release %buildroot%_bindir/tracy
install -Dm755 update/build/unix/update-release %buildroot%_bindir/tracy-update

install -Dm644 extra/desktop/tracy.desktop %buildroot%_datadir/applications/tracy.desktop
install -Dm644 icon/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/tracy.svg
install -Dm644 extra/desktop/application-tracy.xml %buildroot%_datadir/mime/packages/application-tracy.xml
install -Dm644 icon/application-tracy.svg %buildroot%_iconsdir/hicolor/scalable/apps/application-tracy.svg


%files
%license LICENSE
%doc README.*
%_bindir/tracy
%_bindir/tracy-capture
%_bindir/tracy-csvexport
%_bindir/tracy-import-chrome
%_bindir/tracy-update
%_libdir/libtracy.so
%_datadir/applications/tracy.desktop
%_datadir/mime/packages/application-tracy.xml
%_iconsdir/hicolor/scalable/apps/tracy.svg
%_iconsdir/hicolor/scalable/apps/application-tracy.svg


%files devel
%_includedir/Tracy*
%_includedir/client/Tracy*
%_includedir/client/tracy*
%_includedir/common/Tracy*
%_includedir/common/tracy*
%_libdir/libtracy.a
