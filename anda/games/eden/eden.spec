Name:           eden
Version:        0.2.1
Release:        1%?dist
Summary:        The Eden Nintendo Switch Emulator
License:        GPL-3.0-or-later
URL:            https://eden-emu.dev
Packager:       madonuko <mado@fyralabs.com>
Source0:        https://git.eden-emu.dev/eden-emu/eden/archive/v%version.tar.gz
BuildSystem:    cmake
BuildRequires:  gcc git-core
BuildRequires:  pkgconfig(libusb)
BuildRequires:  cmake(VulkanMemoryAllocator)
BuildRequires:  cmake(VulkanUtilityLibraries)
BuildRequires:  pkgconfig(gamemode)
BuildRequires:  cmake(sdl3)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(boost)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(lz4)
BuildRequires:  cmake(zstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  doxygen
BuildRequires:  cmake(SPIRV-Headers)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(httplib)
BuildRequires:  cmake(frozen)
BuildRequires:  cmake(cubeb)
BuildRequires:  cmake(cpp-jwt)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gl)
BuildOption(conf):  -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption(conf):  -DYUZU_TESTS=OFF

%description
Eden is a free and opensource (FOSS) Switch 1 emulator started by developer Camille LaVey.
Written in C++, with builds for Windows, Linux, macOS, Android, FreeBSD and more.

%changelog
* Wed Aug 19 2026 madonuko <mado@fyralabs.com> - 0.2.1-1
- Initial package
