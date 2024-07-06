Name:			tracy
Version:		0.10
Release:		1%?dist
Summary:		A real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications.
License:		BSD-3-Clause
URL:			https://github.com/wolfpld/tracy
Source0:		https://github.com/wolfpld/tracy/archive/refs/tags/v%version.tar.gz
BuildRequires:  cmake meson gcc libxkbcommon libglvnd pkgconfig(glfw) pkgconfig(freetype) pkgconfig(capstone) pkgconfig(dbus) pkgconfig(libunwind) pkgconfig(libdebuginfod) pkgconfig(tbb)
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
%config/tracy/.
%config/tracy/..
%config/tracy/capture
%config/tracy/.clang-tidy
%config/tracy/cmake
%config/tracy/CMakeLists.txt
%config/tracy/Config.cmake.in
%config/tracy/csvexport
%config/tracy/doc
%config/tracy/dtl
%config/tracy/examples
%config/tracy/extra
%config/tracy/getopt
%config/tracy/.git
%config/tracy/.github
%config/tracy/.gitignore
%config/tracy/icon
%config/tracy/imgui
%config/tracy/import-chrome
%config/tracy/import-fuchsia
%config/tracy/library
%config/tracy/LICENSE
%config/tracy/manual
%config/tracy/meson.build
%config/tracy/meson.options
%config/tracy/NEWS
%config/tracy/nfd
%config/tracy/profiler
%config/tracy/public
%config/tracy/python
%config/tracy/README.md
%config/tracy/server
%config/tracy/test
%config/tracy/update
%config/tracy/.vscode
%config/tracy/zstd

%changelog
%autochangelog
