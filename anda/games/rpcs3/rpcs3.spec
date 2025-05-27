%global _distro_extra_cflags -Wno-maybe-uninitialized -fuse-linker-plugin -fuse-ld=mold
%global _distro_extra_cxxflags -include %_includedir/c++/*/cstdint
# GLIBCXX_ASSERTIONS is known to break RPCS3
%global build_cflags %(echo %{__build_flags_lang_c} | sed 's/-Wp,-D_GLIBCXX_ASSERTIONS//g') %{?_distro_extra_cflags}
%global build_cxxflags %(echo %{__build_flags_lang_cxx} | sed 's/-Wp,-D_GLIBCXX_ASSERTIONS//g') %{?_distro_extra_cxxflags}
%ifarch aarch64
# Need to get rid of everything Clang can't use and undefine -Wunused-command-line-argument where possible due to the project's build flags
%global build_cflags %(echo %{build_cflags} | sed 's:-Werror ::g' | sed 's:-Wunused-command-line-argument ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-hardened-ld ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-hardened-ld-errors ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-package-notes ::g') -Wno-unused-command-line-argument
%global build_cxxflags %(echo %{build_cxxflags} | sed 's:-Werror ::g' | sed 's:-Wunused-command-line-argument ::g' | sed 's:-specs\=/usr/lib/rpm/redhat/redhat-annobin-cc1 ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-hardened-ld ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-hardened-ld-errors ::g' | sed 's:-specs=/usr/lib/rpm/redhat/redhat-package-notes ::g') -Wno-unused-command-line-argument
%endif
%global commit 2d9a24d1d6ef0682cfed9ee04d411a8caac9f15a
%global ver 0.0.36-17972

Name:           rpcs3
Version:        %(echo %{ver} | sed 's/-/^/g')
Release:        1%?dist
Summary:        PlayStation 3 emulator and debugger
License:        GPL-2.0-only
URL:            https://github.com/RPCS3/rpcs3
%dnl Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  anda-srpm-macros glew openal-soft cmake vulkan-validation-layers git-core mold
%ifarch x86_64
BuildRequires:  gcc gcc-c++
%elifarch aarch64
BuildRequires:  clang
%endif
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
%git_clone %url %commit

%build
%ifarch aarch64
# Looking at the CMakeLists.txt, this is the intended compiler and there are no fixes for GCC on aarch64
export CC=clang
export CXX=clang++
%endif
%cmake -DDISABLE_LTO=TRUE                              \
    -DZSTD_BUILD_SHARED=OFF                            \
    -DZSTD_BUILD_STATIC=ON                             \
    -DUSE_NATIVE_INSTRUCTIONS=OFF                      \
    -DCMAKE_C_FLAGS="$CFLAGS"                          \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS"                      \
    -DSTATIC_LINK_LLVM=OFF                             \
    -DUSE_SYSTEM_FAUDIO=ON                             \
    -DUSE_SDL=ON                                       \
    -DUSE_SYSTEM_SDL=ON                                \
    -DBUILD_LLVM=OFF                                   \
    -DUSE_PRECOMPILED_HEADERS=OFF                      \
    -DUSE_DISCORD_RPC=ON                               \
    -DUSE_SYSTEM_FFMPEG=ON                             \
    -DUSE_SYSTEM_OPENCV=ON                             \
%if 0%{?fedora} < 43
    -DUSE_SYSTEM_CURL=ON
%endif
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
