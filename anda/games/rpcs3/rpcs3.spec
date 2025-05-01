%global _distro_extra_cflags -Wno-maybe-uninitialized -fuse-linker-plugin -fuse-ld=mold
%global _distro_extra_cxxflags -include %_includedir/c++/*/cstdint

Name:           rpcs3
Version:        0.0.36
Release:        1%?dist
Summary:        PlayStation 3 emulator and debugger
License:        GPL-2.0-only
URL:            https://github.com/RPCS3/rpcs3
%dnl Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  glew openal-soft cmake vulkan-validation-layers gcc gcc-c++ git-core mold
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
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xkbcommon)
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
BuildRequires:  qt6-qtbase-private-devel vulkan-devel jack-audio-connection-kit-devel llvm-devel

%description
%summary.

%prep
%git_clone %url v%version

%build
%cmake -DDISABLE_LTO=TRUE -DZSTD_BUILD_SHARED=ON -DZSTD_BUILD_STATIC=OFF\
    -DUSE_NATIVE_INSTRUCTIONS=OFF                      \
    -DCMAKE_C_FLAGS="$CFLAGS"                          \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS"                      \
    -DSTATIC_LINK_LLVM=OFF                             \
    -DUSE_SYSTEM_FAUDIO=ON                          \
#    -DUSE_PRECOMPILED_HEADERS=OFF                      \
#    -DUSE_SDL=ON                                       \
#    -DCMAKE_AR="$AR"                                   \
#    -DCMAKE_RANLIB="$RANLIB"                           \
#    -DUSE_SYSTEM_SDL=ON                                \
#    -DUSE_SYSTEM_CURL=ON                               \
#    -DUSE_SYSTEM_FFMPEG=ON                             \
#    -DUSE_SYSTEM_OPENCV=ON                             \
#    -DUSE_DISCORD_RPC=ON                               \
#    -DOpenGL_GL_PREFERENCE=LEGACY                      \
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
