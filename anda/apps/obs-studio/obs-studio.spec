%global obswebsocketver 5.2.2

Name:			obs-studio
Version:		29.1.1
Release:		1%?dist
Summary:		Open Broadcaster Software Studio
License:		GPL-2.0-or-later and ISC and MIT and BSD-1-Clause and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and LGPL-2.1-or-later and CC0-1.0 and (CC0-1.0 or OpenSSL or Apache-2.0) and LicenseRef-Fedora-Public-Domain and (BSD-3-Clause or GPL-2.0-only)
URL:			https://obsproject.com/
Source0:		https://github.com/obsproject/obs-studio/archive/refs/tags/%version.tar.gz
Source1:		https://github.com/obsproject/obs-websocket/archive/%obswebsocketver/obs-websocket-%obswebsocketver.tar.gz

BuildRequires:	gcc
BuildRequires:	cmake >= 3.16
BuildRequires:	ninja-build
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils

BuildRequires:	alsa-lib-devel
BuildRequires:	asio-devel
BuildRequires:	fdk-aac-free-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	jansson-devel >= 2.5
BuildRequires:	json-devel
BuildRequires:	libcurl-devel
BuildRequires:	libdrm-devel
BuildRequires:	libGL-devel
BuildRequires:	libglvnd-devel
BuildRequires:	librist-devel
BuildRequires:	srt-devel
BuildRequires:	libuuid-devel
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel
BuildRequires:	libX11-devel
BuildRequires:	libxcb-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libxkbcommon-devel
BuildRequires:	luajit-devel
BuildRequires:	mbedtls-devel
BuildRequires:	pciutils-devel
BuildRequires:	pipewire-devel
BuildRequires:	pipewire-jack-audio-connection-kit-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	python3-devel
BuildRequires:	libqrcodegencpp-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtbase-private-devel
BuildRequires:	qt6-qtsvg-devel
BuildRequires:	qt6-qtwayland-devel
BuildRequires:	speexdsp-devel
BuildRequires:	swig
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	websocketpp-devel
BuildRequires:	ffmpeg-free-devel
BuildRequires:	x264-devel
BuildRequires:	vlc-devel
# websocket deps
BuildRequires:	nlohmann-json-devel websocketpp-devel asio-devel

# Ensure QtWayland is installed when libwayland-client is installed
Requires:		(qt6-qtwayland%{?_isa} if libwayland-client%{?_isa})
# For icon folder heirarchy
Requires:		hicolor-icon-theme
# Virtual camera support
Recommends:		kmod-v4l2loopback
# NVIDIA Hardware accelerated encoding: CUDA
Suggests:		xorg-x11-drv-nvidia-cuda
# obs-studio-plugin-vlc-video
# We dlopen() libvlc
Requires:		libvlc.so.%{libvlc_soversion}%{?lib64_suffix}


# These are modified sources that can't be easily unbundled
## License: MIT and CC0-1.0
## Newer version in Fedora with the same licensing
## Request filed upstream for fixing it: https://github.com/simd-everywhere/simde/issues/999
Provides:		bundled(simde) = 0.7.1
## License: BSL-1.0
Provides:		bundled(decklink-sdk)
## License: CC0-1.0 or OpenSSL or Apache-2.0
Provides:		bundled(blake2)
## License: MIT
Provides:		bundled(json11)
## License: MIT
Provides:		bundled(libcaption)
## License: ISC
Provides:		bundled(libff)
## License: BSD-1-Clause
Provides:		bundled(uthash)
## License: BSD-3-Clause
Provides:		bundled(rnnoise)
## License: LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
Provides:		bundled(librtmp)
## License: MIT
Provides:		bundled(libnsgif)
## License: MIT
## Windows only dependency
## Support for Linux will also unbundle it
## Cf. https://github.com/obsproject/obs-studio/pull/8327
Provides:		bundled(intel-mediasdk)

%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.


%prep
%autosetup -p1 -n obs-studio-%{?snapdate:%{commit}}%{!?snapdate:%{version_no_tilde}}
# Prepare plugins/obs-websocket
tar -xf %SOURCE1 --strip-components=1 -C plugins/obs-websocket/
ls plugins/obs-websocket/
sed -e 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' -i cmake/Modules/ObsHelpers.cmake
# Kill rpath settings
sed -e '\|set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/${OBS_LIBRARY_DESTINATION}")|d' -i cmake/Modules/ObsHelpers_Linux.cmake
# touch the missing submodules
touch plugins/obs-browser/CMakeLists.txt
# remove -Werror flag to mitigate FTBFS with ffmpeg 5.1
sed -e 's|-Werror-implicit-function-declaration||g' -i cmake/Modules/CompilerConfig.cmake
sed -e '/-Werror/d' -i cmake/Modules/CompilerConfig.cmake


%build
%cmake -B build -S . \
	-DUNIX_STRUCTURE=1 -GNinja \
	-DCMAKE_SKIP_RPATH=1 \
	-DBUILD_BROWSER=OFF \
	-DENABLE_JACK=ON \
	-DENABLE_LIBFDK=ON \
	-DENABLE_AJA=OFF \
	-DOBS_VERSION_OVERRIDE="%version-%release" \
	-Wno-dev \
	-DOpenGL_GL_PREFERENCE=GLVND
%cmake_build


%install
%cmake_install


%files
%doc README.rst
%license COPYING plugins/{{enc-amf,obs-websocket}/LICENSE,obs-{browser,filters,outputs}/COPYING}


%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 29.1.1-1
- Initial package
- Ref: https://pkgs.rpmfusion.org/cgit/free/obs-studio-freeworld.git/tree/obs-studio-freeworld.spec
- Ref: https://gitlab.archlinux.org/archlinux/packaging/packages/obs-studio/-/blob/main/PKGBUILD
