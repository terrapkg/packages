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
BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release -DDISTRO_NIX=ON -DBUILD_SHARED_LIBS=ON -DBUiLD_STATIC_LIBS=OFF -DTHREADS_PREFER_PTHREAD_FLAG=ON -DMILLENNIUM_BUILD_TESTS=OFF
BuildOption(conf):  -DCURL_LIBRARY=/usr/lib/libcurl.so -DCURL_INCLUDE_DIR=%_includedir/curl/
BuildOption(conf):  -DZLIB_LIBRARY=/usr/lib/libz.so -DZLIB_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DBZIP2_LIBRARIES=%_libdir/libbz2.so -DBZIP2_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DLIBLZMA_LIBRARY=%_libdir/liblzma.so -DLIBLZMA_INCLUDE_DIR=%_includedir
BuildOption(conf):  -DLIBLZMA_HAS_AUTO_DECODER=1 -DLIBLZMA_HAS_EASY_ENCODER=1 -DLIBLZMA_HAS_LZMA_PRESET=1
BuildOption(conf):  -DLIBM_LIBRARIES=/usr/lib64/libm.so -DLIBDL_LIBRARIES=/usr/lib64/libdl.a
BuildRequires:  cmake(zlib)
BuildRequires:  cmake(minizip-ng)
BuildRequires:  minizip-ng(x86-32)
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  bun-bin
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  libcurl-devel
BuildRequires:  libcurl-devel(x86-32)
BuildRequires:  json-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  zlib-ng-compat-static
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  zlib-ng-compat-devel(x86-32)
BuildRequires:  libzstd-devel(x86-32)
BuildRequires:  xz-devel(x86-32)
BuildRequires:  bzip2-devel
BuildRequires:  bzip2-devel(x86-32)
BuildRequires:  bzip2-libs
BuildRequires:  xz-devel
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel
BuildRequires:  libgcc(x86-32)
BuildRequires:  libatomic(x86-32)
BuildRequires:  libstdc++(x86-32)
BuildRequires:  openssl-devel(x86-32)
BuildRequires:  openssl-libs(x86-32)
BuildRequires:  libidn2(x86-32)
BuildRequires:  glibc-devel(x86-32)

ExclusiveArch:  x86_64

%description
Open-source modding framework for creating and managing Steam Client themes and plugins.

%conf -p
sed 's/find_package(ZLIB/find_package(zlib/' -i scripts/cmake/bootstrap_deps.cmake
sed '/find_package(zlib       REQUIRED)/a\    set_target_properties(ZLIB::ZLIB PROPERTIES IMPORTED_LOCATION "/usr/lib/libz.so")' -i scripts/cmake/bootstrap_deps.cmake
sed '/find_package(minizip-ng REQUIRED)/a\    set_target_properties(MINIZIP::minizip-ng PROPERTIES IMPORTED_LOCATION "/usr/lib/libminizip-ng.so.4.1.0" INTERFACE_LINK_LIBRARIES "/usr/lib/libz.so;/usr/lib/libbz2.so;/usr/lib/liblzma.so;/usr/lib/libzstd.so;ssl;crypto")' -i scripts/cmake/bootstrap_deps.cmake

cd src/typescript
bun install --frozen-lockfile
(cd ttc && bun run build)
(cd sdk && bun run build)
(cd frontend && bun run build)
cd ../..

sed 's/if(LJ_64)$/if(LJ_64 AND "${LJ_TARGET_ARCH}" STREQUAL "x64")/' -i thirdparty/forks/luajit/LuaJIT.cmake
sed '/target_link_libraries(${MILLENNIUM_RTB_NAME}/i\target_compile_options(${MILLENNIUM_RTB_NAME} PRIVATE -m32)\ntarget_link_options(${MILLENNIUM_RTB_NAME} PRIVATE -m32)' -i src/lua_host/CMakeLists.txt

%files
%doc README.md
%license LICENSE.md
%{_bindir}/luajit
%{_includedir}/luajit/
%{_libdir}/libluajit.a

%changelog
* Thu Sep 17 2026 madonuko <mado@fyralabs.com>
- initial package
