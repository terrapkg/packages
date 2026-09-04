Name:           millennium
Version:        3.4.0
Release:        1%?dist
Summary:        Open-source modding framework for creating and managing Steam Client themes and plugins
License:        MIT
URL:            https://steambrew.app
Source0:        https://github.com/SteamClientHomebrew/Millennium/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildSystem:    cmake
BuildOption(conf):  -DDISTRO_NIX=ON -DBUILD_SHARED_LIBS=ON -DBUiLD_STATIC_LIBS=OFF
BuildOption(conf):  -DCURL_LIBRARY=%_libdir/libcurl.so -DCURL_INCLUDE_DIR=%_includedir/curl/
BuildRequires:  cmake(zlib)
BuildRequires:  zlib-ng-compat-static


%description
Open-source modding framework for creating and managing Steam Client themes and plugins.

%conf -p
sed 's/find_package(ZLIB/find_package(zlib/' -i scripts/cmake/bootstrap_deps.cmake
sed 's/find_package(CURL/find_package(curl/' -i scripts/cmake/bootstrap_deps.cmake

%files
%doc README.md
%license LICENSE.md
