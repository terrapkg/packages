%bcond_with mold

Name:           millennium
Version:        3.4.1
Release:        1%?dist
Summary:        Open-source modding framework for creating and managing Steam Client themes and plugins
License:        MIT
URL:            https://steambrew.app
Source0:        https://github.com/SteamClientHomebrew/Millennium/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildSystem:    cmake
BuildOption(conf):  -DDISTRO_NIX=ON -DBUILD_SHARED_LIBS=ON -DBUiLD_STATIC_LIBS=OFF
BuildOption(conf):  -DCURL_LIBRARY=%_libdir/libcurl.so -DCURL_INCLUDE_DIR=%_includedir/curl/
BuildOption(conf):  -DZLIB_LIBRARY=%_libdir/libz.so -DZLIB_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DBZIP2_LIBRARIES=%_libdir/libbz2.so -DBZIP2_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DLIBLZMA_LIBRARY=%_libdir/liblzma.so -DLIBLZMA_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DLIBLZMA_HAS_AUTO_DECODER=1 -DLIBLZMA_HAS_EASY_ENCODER=1 -DLIBLZMA_HAS_LZMA_PRESET=1
BuildRequires:  cmake(zlib)
BuildRequires:  cmake(minizip-ng)
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  bun-bin
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-ng-compat-static
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  bzip2-devel
BuildRequires:  bzip2-libs
BuildRequires:  xz-devel
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel
BuildRequires:  libgcc(x86-32)
BuildRequires:  libstdc++(x86-32)
BuildRequires:  openssl-devel(x86-32)
BuildRequires:  openssl-libs(x86-32)
BuildRequires:  libidn2(x86-32)

ExclusiveArch:  x86_64

%description
Open-source modding framework for creating and managing Steam Client themes and plugins.

%conf -p
sed 's/find_package(ZLIB/find_package(zlib/' -i scripts/cmake/bootstrap_deps.cmake

%files
%doc README.md
%license LICENSE.md

%changelog
* Thu Sep 17 2026 madonuko <mado@fyralabs.com>
- initial package
