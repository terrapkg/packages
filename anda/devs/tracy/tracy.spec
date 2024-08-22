%global _desc Tracy is a real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.

Name:			tracy
Version:		0.11.1
Release:		1%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  pkgconfig(egl) pkgconfig(glfw3) pkgconfig(freetype2) pkgconfig(dbus-1) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb) pkgconfig(wayland-client) pkgconfig(wayland-protocols) pkgconfig(xkbcommon) pkgconfig(capstone)
BuildRequires:  cmake gcc gcc-c++ meson

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
%meson
%meson_build

for project in capture csvexport import-chrome import-fuchsia update profiler
do
    pushd $project
    %cmake -DDOWNLOAD_CAPSTONE=0
    %cmake_build
    popd
done

%install
%meson_install

# NOTE: the subprojects don't have install targets so we do it manually
install -Dm755 capture/%__cmake_builddir/tracy-capture %buildroot%_bindir/tracy-capture
install -Dm755 csvexport/%__cmake_builddir/tracy-csvexport %buildroot%_bindir/tracy-csvexport
install -Dm755 import-chrome/%__cmake_builddir/tracy-import-chrome %buildroot%_bindir/tracy-import-chrome
install -Dm755 import-fuchsia/%__cmake_builddir/tracy-import-fuchsia %buildroot%_bindir/tracy-import-fuchsia
install -Dm755 update/%__cmake_builddir/tracy-update %buildroot%_bindir/tracy-update
install -Dm755 profiler/%__cmake_builddir/tracy-profiler %buildroot%_bindir/tracy

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
%_bindir/tracy-import-fuchsia
%_bindir/tracy-update
%_libdir/libtracy.so
%_datadir/applications/tracy.desktop
%_datadir/mime/packages/application-tracy.xml
%_iconsdir/hicolor/scalable/apps/tracy.svg
%_iconsdir/hicolor/scalable/apps/application-tracy.svg

%files devel
%_libdir/pkgconfig/tracy.pc
%_includedir/common
%_includedir/tracy
%_includedir/client

%changelog
* Wed Jul 24 2024 Owen Zimmerman <owen@fyralabs.com> - 0.11-1
- Initial package.
