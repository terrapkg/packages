#? https://gitlab.archlinux.org/archlinux/packaging/packages/signal-desktop/-/blob/main/PKGBUILD
%define	debug_package %{nil}

# Make electron_license macro properly work
%bcond bundled_electron 1

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude ^lib.*\\.so.*$

%ifarch x86_64
%define arch %{nil}
%elifarch aarch64
%define arch arm64-
%endif

Name:			signal-desktop
Version:		7.84.0
Release:		1%?dist
Summary:		A private messenger for Windows, macOS, and Linux
URL:			https://signal.org
Source0:		https://github.com/signalapp/Signal-Desktop/archive/refs/tags/v%{version}.tar.gz
# signal.desktop from https://github.com/signalflatpak/signal/blob/master/org.signal.Signal.desktop
Source1:		signal.desktop
License:		AGPL-3.0 AND %{electron_license}
ExclusiveArch:	x86_64 aarch64

BuildRequires:	 pulseaudio-libs-devel
BuildRequires:  libX11-devel
BuildRequires:	 git-lfs
BuildRequires:  git-core
BuildRequires:  anda-srpm-macros
BuildRequires:	 pnpm
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  python3

Requires:		gtk3
Requires:		libwayland-cursor
Requires:		libwayland-client
Requires:		libxkbcommon
Requires:		gdk-pixbuf2
Requires:		libthai
Requires:		nettle
Requires:		avahi-libs
Requires:		libXfixes
Requires:		libjpeg-turbo
Requires:		sqlite-libs
Requires:		json-glib
Requires:		libdatrie
Requires:		libxml2
Requires:		libbrotli
Requires:		cairo
Requires:		xz-libs
Requires:		libxcb
Requires:		nss-util
Requires:		nss
Requires:		dbus-libs
Requires:		mesa-libgbm
Requires:		at-spi2-atk
Requires:		expat
Requires:		alsa-lib
Requires:       xdg-utils
Requires:       re2
Requires:       (libXtst or libXtst6)
Requires:       libXScrnSaver
Requires:       libnotify
Requires:       (libuuid or libuuid1)
Requires:       at-spi2-core
Requires:       c-ares
Requires:       gtk3
Requires:       minizip

Provides:       signal
Provides:       Signal
Provides:       Signal-Desktop

%description
Signal Desktop links with Signal on Android or iOS and lets you message from your Windows, macOS, and Linux computers.

%prep
%autosetup -n Signal-Desktop-%{version}

%build
pnpm install --frozen-lockfile
pushd sticker-creator
pnpm install --frozen-lockfile
pnpm build
popd
pnpm run build-linux --dir

%install
install -Dm755 release/linux-%{arch}unpacked/libEGL.so %{buildroot}%{_libdir}/signal-desktop/libEGL.so
install -Dm755 release/linux-%{arch}unpacked/libGLESv2.so %{buildroot}%{_libdir}/signal-desktop/libGLESv2.so
install -Dm755 release/linux-%{arch}unpacked/libffmpeg.so %{buildroot}%{_libdir}/signal-desktop/libffmpeg.so
install -Dm755 release/linux-%{arch}unpacked/libvk_swiftshader.so %{buildroot}%{_libdir}/signal-desktop/libvk_swiftshader.so
install -Dm755 release/linux-%{arch}unpacked/libvulkan.so.1 %{buildroot}%{_libdir}/signal-desktop/libvulkan.so.1
install -Dm644 release/linux-%{arch}unpacked/icudtl.dat %{buildroot}%{_libdir}/signal-desktop/icudtl.dat
install -Dm644 release/linux-%{arch}unpacked/v8_context_snapshot.bin %{buildroot}%{_libdir}/signal-desktop/v8_context_snapshot.bin
install -Dm644 release/linux-%{arch}unpacked/chrome_100_percent.pak %{buildroot}%{_libdir}/signal-desktop/chrome_100_percent.pak
install -Dm644 release/linux-%{arch}unpacked/chrome_200_percent.pak %{buildroot}%{_libdir}/signal-desktop/chrome_200_percent.pak
install -Dm644 release/linux-%{arch}unpacked/resources.pak %{buildroot}%{_libdir}/signal-desktop/resources.pak
install -Dm644 release/linux-%{arch}unpacked/vk_swiftshader_icd.json %{buildroot}%{_libdir}/signal-desktop/vk_swiftshader_icd.json
install -Dm644 release/linux-%{arch}unpacked/resources/app.asar %{buildroot}%{_libdir}/signal-desktop/resources/app.asar
cp -r release/linux-%{arch}unpacked/resources/app.asar.unpacked %{buildroot}%{_libdir}/signal-desktop/resources/

install -Dm755 release/linux-%{arch}unpacked/chrome-sandbox %{buildroot}%{_libdir}/signal-desktop/chrome-sandbox
install -Dm755 release/linux-%{arch}unpacked/chrome_crashpad_handler %{buildroot}%{_libdir}/signal-desktop/chrome_crashpad_handler

install -Dm755 release/linux-%{arch}unpacked/signal-desktop %{buildroot}%{_libdir}/signal-desktop/signal-desktop

install -Dm644 release/linux-%{arch}unpacked/resources/org.signalapp.view-aep.policy %{buildroot}%{_datadir}/polkit-1/rules.d/org.signalapp.view-aep.policy
install -Dm644 release/linux-%{arch}unpacked/resources/org.signalapp.enable-backups.policy %{buildroot}%{_datadir}/polkit-1/rules.d/org.signalapp.enable-backups.policy

install -Dm644 build/icons/png/1024x1024.png %{buildroot}%{_iconsdir}/hicolor/1024x1024/apps/signal.png
install -Dm644 build/icons/png/128x128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/signal.png
install -Dm644 build/icons/png/16x16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/signal.png
install -Dm644 build/icons/png/24x24.png %{buildroot}%{_iconsdir}/hicolor/24x24/apps/signal.png
install -Dm644 build/icons/png/256x256.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/signal.png
install -Dm644 build/icons/png/32x32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/signal.png
install -Dm644 build/icons/png/48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/signal.png
install -Dm644 build/icons/png/512x512.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/signal.png
install -Dm644 build/icons/png/64x64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/signal.png

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/signal.desktop
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/signal-desktop/signal-desktop %{buildroot}%{_bindir}/signal-desktop

%files
%license LICENSE
%doc README.md CONTRIBUTING.md ACKNOWLEDGMENTS.md
%license release/linux-%{arch}unpacked/LICENSE.electron.txt
%license release/linux-%{arch}unpacked/LICENSES.chromium.html
%{_bindir}/signal-desktop
%{_libdir}/signal-desktop/
%{_datadir}/polkit-1/rules.d/org.signalapp.view-aep.policy
%{_datadir}/polkit-1/rules.d/org.signalapp.enable-backups.policy
%{_datadir}/applications/signal.desktop
%{_iconsdir}/hicolor/1024x1024/apps/signal.png
%{_iconsdir}/hicolor/128x128/apps/signal.png
%{_iconsdir}/hicolor/16x16/apps/signal.png
%{_iconsdir}/hicolor/24x24/apps/signal.png
%{_iconsdir}/hicolor/256x256/apps/signal.png
%{_iconsdir}/hicolor/32x32/apps/signal.png
%{_iconsdir}/hicolor/48x48/apps/signal.png
%{_iconsdir}/hicolor/512x512/apps/signal.png
%{_iconsdir}/hicolor/64x64/apps/signal.png

%changelog
* Tue Nov 11 2025 Owen Zimmerman <owen@fyralabs.com>
- Add more Requires:, fix electron_license macro application, fix some formatting
* Fri Aug 8 2025 june-fish <git@june.fish>
- Initial Package
