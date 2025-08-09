%define	debug_package %{nil}

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:			signal-desktop	
Version:		7.65.0
Release:		1%?dist
Summary:		A private messenger for Windows, macOS, and Linux
URL:			https://signal.org
Source0:		https://github.com/signalapp/Signal-Desktop/archive/refs/tags/v%{version}.tar.gz
# signal.desktop from https://github.com/signalflatpak/signal/blob/master/org.signal.Signal.desktop
Source1:		signal.desktop
License:		AGPL-3.0 AND %electron_licenses
BuildRequires:		pulseaudio-libs-devel libX11-devel pnpm make gcc g++ python3 
Requires:		pulseaudio-libs 
Requires:               glib2
Requires:               gtk3
Requires:               libwayland-cursor
Requires:               libwayland-client 
Requires:               libxkbcommon
Requires:               glibc 
Requires:               gdk-pixbuf2
Requires:               libthai
Requires:               nettle
Requires:               avahi-libs
Requires:               libXfixes
Requires:               libX11
Requires:               libjpeg-turbo
Requires:               sqlite-libs
Requires:               json-glib
Requires:               libdatrie
Requires:               libxml2
Requires:               libbrotli
Requires:               cairo
Requires:               xz-libs
Requires:               libxcb
Requires:               nss-util
Requires:               nss
Requires:               dbus-libs
Requires:               mesa-libgbm
Requires:               at-spi2-atk
Requires:               expat
Requires:               alsa-lib

%description
Signal Desktop links with Signal on Android or iOS and lets you message from your Windows, macOS, and Linux computers.

%prep
%autosetup -n Signal-Desktop-%{version}

%build
pnpm install
pnpm run build-linux --dir

%install
install -Dm755 release/linux-arm64-unpacked/libEGL.so %{buildroot}%{_libdir}/signal-desktop/libEGL.so
install -Dm755 release/linux-arm64-unpacked/libGLESv2.so %{buildroot}%{_libdir}/signal-desktop/libGLESv2.so
install -Dm755 release/linux-arm64-unpacked/libffmpeg.so %{buildroot}%{_libdir}/signal-desktop/libffmpeg.so
install -Dm755 release/linux-arm64-unpacked/libvk_swiftshader.so %{buildroot}%{_libdir}/signal-desktop/libvk_swiftshader.so
install -Dm755 release/linux-arm64-unpacked/libvulkan.so.1 %{buildroot}%{_libdir}/signal-desktop/libvulkan.so.1
install -Dm644 release/linux-arm64-unpacked/icudtl.dat %{buildroot}%{_libdir}/signal-desktop/icudtl.dat
install -Dm644 release/linux-arm64-unpacked/v8_context_snapshot.bin %{buildroot}%{_libdir}/signal-desktop/v8_context_snapshot.bin
install -Dm644 release/linux-arm64-unpacked/chrome_100_percent.pak %{buildroot}%{_libdir}/signal-desktop/chrome_100_percent.pak
install -Dm644 release/linux-arm64-unpacked/chrome_200_percent.pak %{buildroot}%{_libdir}/signal-desktop/chrome_200_percent.pak
install -Dm644 release/linux-arm64-unpacked/resources.pak %{buildroot}%{_libdir}/signal-desktop/resources.pak
install -Dm644 release/linux-arm64-unpacked/vk_swiftshader_icd.json %{buildroot}%{_libdir}/signal-desktop/vk_swiftshader_icd.json
install -Dm644 release/linux-arm64-unpacked/resources/app.asar %{buildroot}%{_libdir}/signal-desktop/resources/app.asar
cp -r release/linux-arm64-unpacked/resources/app.asar.unpacked %{buildroot}%{_libdir}/signal-desktop/resources/

install -Dm755 release/linux-arm64-unpacked/chrome-sandbox %{buildroot}%{_libdir}/signal-desktop/chrome-sandbox
install -Dm755 release/linux-arm64-unpacked/chrome_crashpad_handler %{buildroot}%{_libdir}/signal-desktop/chrome_crashpad_handler

install -Dm755 release/linux-arm64-unpacked/signal-desktop %{buildroot}%{_libdir}/signal-desktop/signal-desktop

install -Dm644 release/linux-arm64-unpacked/resources/org.signalapp.view-aep.policy %{buildroot}%{_datadir}/polkit-1/rules.d/org.signalapp.view-aep.policy
install -Dm644 release/linux-arm64-unpacked/resources/org.signalapp.enable-backups.policy %{buildroot}%{_datadir}/polkit-1/rules.d/org.signalapp.enable-backups.policy

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

%post
ln -s %_libdir/signal-desktop/signal-desktop %_bindir/signal-desktop

%files
%license LICENSE
%license release/linux-arm64-unpacked/LICENSE.electron.txt
%license release/linux-arm64-unpacked/LICENSES.chromium.html
%doc CONTRIBUTING.md
%doc ACKNOWLEDGMENTS.md
%doc README.md
%ghost %{_bindir}/signal-desktop
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
* Fri Aug 8 2025 june-fish <git@june.fish>
- Initial Package
