Name:			tracy
Version:		0.10
Release:		1%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  cmake meson gcc libxkbcommon dbus-devel libglvnd glfw-devel freetype-devel pkgconfig(capstone) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb)
Patch:          https://github.com/wolfpld/tracy/commit/1a971d867d6fa5bf6dc57d705dcbbc6020031e7a.patch

%description
%A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.

%prep
%autosetup -n tracy-0.10

%build
%make_build -C capture/build/unix release
%make_build -C csvexport/build/unix release
%make_build -C import-chrome/build/unix release
%make_build -C library/unix release
%make_build -C profiler/build/unix release
%make_build -C update/build/unix release

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 Tracy-release %{buildroot}/usr/bin/Tracy-release

%files

%license LICENSE
%doc README.*
%{_datadir}/tracy/capture
%{_datadir}/tracy/cmake
%{_datadir}/tracy/CMakeLists.txt
%{_datadir}/tracy/Config.cmake.in
%{_datadir}/tracy/csvexport
%{_datadir}/tracy/doc
%{_datadir}/tracy/dtl
%{_datadir}/tracy/examples
%{_datadir}/tracy/extra
%{_datadir}/tracy/getopt
%{_datadir}/tracy/icon
%{_datadir}/tracy/imgui
%{_datadir}/tracy/import-chrome
%{_datadir}/tracy/import-fuchsia
%{_datadir}/tracy/library
%{_datadir}/tracy/manual
%{_datadir}/tracy/meson.build
%{_datadir}/tracy/meson.options
%{_datadir}/tracy/NEWS
%{_datadir}/tracy/nfd
%{_datadir}/tracy/profiler
%{_datadir}/tracy/public
%{_datadir}/tracy/python
%{_datadir}/tracy/server
%{_datadir}/tracy/test
%{_datadir}/tracy/update
%{_datadir}/tracy/zstd

%changelog
* Thu Jul 10 2024 Owen Zimmerman
- Initial package.

%autochangelog
