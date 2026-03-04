Name:			tracy
Version:		0.13.1
Release:		2%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  pkgconfig(egl) pkgconfig(glfw3) pkgconfig(freetype2) pkgconfig(dbus-1) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb) pkgconfig(wayland-client) pkgconfig(wayland-protocols) pkgconfig(xkbcommon) pkgconfig(capstone) pkgconfig(openssl) pkgconfig(pugixml) pkgconfig(libcurl) pkgconfig(libxslt) pkgconfig(libnghttp2) pkgconfig(libidn2) pkgconfig(libssh2) tbb expat libxml2 openssl-libs
BuildRequires:  cmake gcc gcc-c++ meson

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Tracy is a real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.

%package devel
Summary: Development files for the tracy package

%description devel
Development files for the tracy package.

%prep
%autosetup

%build
%meson -Dcpp_std=c++17
%meson_build
for project in capture csvexport import update profiler
do
    pushd $project
    %cmake -DDOWNLOAD_CAPSTONE=1 \
           -DCMAKE_CXX_STANDARD=17 \
           -DCMAKE_SKIP_RPATH=ON \
           -DCMAKE_SKIP_INSTALL_RPATH=ON
    %cmake_build
    popd
done

%install
%meson_install

# NOTE: the subprojects don't have install targets so we do it manually
install -Dm755 capture/%__cmake_builddir/tracy-capture %buildroot%_bindir/tracy-capture
install -Dm755 csvexport/%__cmake_builddir/tracy-csvexport %buildroot%_bindir/tracy-csvexport
install -Dm755 import/%__cmake_builddir/tracy-import-chrome %buildroot%_bindir/tracy-import-chrome
install -Dm755 import/%__cmake_builddir/tracy-import-fuchsia %buildroot%_bindir/tracy-import-fuchsia
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
%_includedir/tracy/*

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com> - 0.13.1-1
- Fix compile issues, update for 0.13.1

* Wed Jul 24 2024 Owen Zimmerman <owen@fyralabs.com> - 0.11-1
- Initial package.
