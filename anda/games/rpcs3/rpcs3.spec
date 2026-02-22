# RPCS3 builds often break with GCC
%global toolchain clang
# Define which LLVM/Clang version RPCS3 needs
%if 0%{?fedora} >= 45
%global llvm_major 21
%global __cc clang-%{llvm_major}
%global __cxx clang++-%{llvm_major}
%endif
# GLIBCXX_ASSERTIONS is known to break RPCS3
%global build_cflags %(echo "%{__build_flags_lang_c}" | sed 's|-Wp,-D_GLIBCXX_ASSERTIONS ||g') %{?_distro_extra_cflags}
%global build_cxxflags %(echo "%{__build_flags_lang_cxx}" | sed 's|-Wp,-D_GLIBCXX_ASSERTIONS ||g') %{?_distro_extra_cflags}
%global commit 3585881a6c6d8a5fad78ec1949be89a7a20b9be3
%global ver 0.0.39-18812

Name:           rpcs3
Version:        %(echo %{ver} | sed 's/-/^/g')
Release:        1%?dist
Summary:        PlayStation 3 emulator and debugger
License:        GPL-2.0-only
URL:            https://github.com/RPCS3/rpcs3
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:  anda-srpm-macros glew openal-soft cmake vulkan-validation-layers git-core mold
BuildRequires:  llvm%{?llvm_major}-devel
BuildRequires:  clang%{?llvm_major}
BuildRequires:  cmake(FAudio)
BuildRequires:  cmake(OpenAL)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
#BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  doxygen
BuildRequires:  qt6-qtbase-private-devel vulkan-devel jack-audio-connection-kit-devel

%description
%summary.

%prep
%git_clone %url %commit

%build
# Looking at the CMakeLists.txt, this is the intended compiler and there are no fixes for GCC on aarch64
%if %{defined llvm_major}
export LLVM_DIR=%{_libdir}/llvm%{?llvm_major}/%{_lib}/cmake
%endif
%cmake -DDISABLE_LTO=TRUE                                     \
    -DZSTD_BUILD_STATIC=ON                                    \
    -DCMAKE_SKIP_RPATH=ON                                     \
    -DBUILD_SHARED_LIBS:BOOL=OFF                              \
    -DUSE_NATIVE_INSTRUCTIONS=OFF                             \
    -DCMAKE_C_FLAGS="$CFLAGS"                                 \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS"                             \
    -DSTATIC_LINK_LLVM=OFF                                    \
    -DUSE_SYSTEM_FAUDIO=ON                                    \
    -DUSE_SDL=ON                                              \
    -DUSE_SYSTEM_SDL=ON                                       \
    -DBUILD_LLVM=OFF                                          \
    -DUSE_PRECOMPILED_HEADERS=OFF                             \
    -DUSE_DISCORD_RPC=ON                                      \
    -DUSE_SYSTEM_FFMPEG=ON                                    \
    -DUSE_SYSTEM_LIBPNG=ON                                    \
    -DUSE_SYSTEM_ZLIB=ON                                      \
    -DUSE_SYSTEM_OPENCV=ON                                    \
    -DUSE_SYSTEM_CURL=ON                                      \
    -DUSE_SYSTEM_FLATBUFFERS=OFF                              \
    -DUSE_SYSTEM_PUGIXML=OFF                                  \
    -DUSE_SYSTEM_WOLFSSL=OFF                                  \
    -DCMAKE_C_COMPILER="$CC"                                  \
    -DCMAKE_CXX_COMPILER="$CXX"                               \
    -DCMAKE_LINKER=mold                                       \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -fuse-ld=mold"      \
    -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -fuse-ld=mold"    
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%_bindir/rpcs3
%_datadir/applications/rpcs3.desktop
%_datadir/metainfo/rpcs3.metainfo.xml
%_datadir/rpcs3/
%_iconsdir/hicolor/48x48/apps/rpcs3.png
%_iconsdir/hicolor/scalable/apps/rpcs3.svg
