%global debug_package %{nil}
%global __provides_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*))$
%ifnarch aarch64 
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\aarch64*\\.so.*))$
%elifarch aarch64
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\x86_64*\\.so.*)|(.*\\x86-64*\\.so.*))$
%endif
%define _build_id_links none
%global org_name Heroic-Games-Launcher
%global git_name %(echo %{org_name} | sed 's/-//g')
%global reverse_dns com.heroicgameslauncher.hgl
%global shortname heroic
%global legendary_version 0.20.36
%global gogdl_version 1.1.2
%global nile_version 1.1.2
%global comet_version 0.2.0

Name:          %{shortname}-games-launcher
Version:       2.16.1
Release:       2%?dist
Summary:       A games launcher for GOG, Amazon, and Epic Games
License:       GPL-3.0-only AND MIT AND BSD-3-Clause
URL:           https://heroicgameslauncher.com
BuildRequires: anda-srpm-macros
BuildRequires: desktop-file-utils
### Electron builder builds some things with GCC(++), Git, and Make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: nodejs
BuildRequires: pnpm
BuildRequires: python3
BuildRequires: sed
Requires:      alsa-lib
Requires:      gtk3
Requires:      hicolor-icon-theme
Requires:      nss
Requires:      python3
Requires:      which
Recommends:    gamemode
Recommends:    mangohud
Recommends:    umu-launcher
Provides:      bundled(comet) = %{comet_version}
Provides:      bundled(gogdl) = %{gogdl_version}
Provides:      bundled(legendary) = %{legendary_version}
Provides:      bundled(nile) = %{nile_version}
Packager:      Gilver E. <rockgrub@disroot.org>

%description
Heroic is a Free and Open Source Epic, GOG, and Amazon Prime Games launcher for Linux, Windows, and macOS.

%prep
%git_clone https://github.com/%{org_name}/%{git_name} v%{version}
sed -i 's/Exec=.*%u/Exec=\/usr\/share\/%{shortname}\/%{shortname} %U/g' flatpak/%{reverse_dns}.desktop
sed -i 's/Icon=.*/Icon=%{shortname}/g' flatpak/%{reverse_dns}.desktop

%build
pnpm install
pnpm run download-helper-binaries
pnpm dist:linux

%install
mkdir -p %{buildroot}%{_datadir}/%{shortname}
mv $(find . -iname "*LICENSE*" -not -path "./node_modules/*" -and -not -path "./public/*") .
mv LICENSE LICENSE.fonts
%ifarch aarch64
### Needs testing once aarch64 Heroic is complete:
#rm -rf dist/linux-unpacked/resources/app.asar.unpacked/build/bin/x64
mv dist/linux-arm64-unpacked/* %{buildroot}%{_datadir}/%{shortname}
%else
rm -rf dist/linux-unpacked/resources/app.asar.unpacked/build/bin/arm64
mv dist/linux-unpacked/* %{buildroot}%{_datadir}/%{shortname}
%endif
mkdir -p %{buildroot}%{_bindir}
# Make names executable
ln -sr %{_datadir}/%{shortname}/%{shortname} %{buildroot}%{_bindir}/%{name}
ln -sr %{_datadir}/%{shortname}/%{shortname} %{buildroot}%{_bindir}/%{shortname}
install -Dm644 dist/.icon-set/icon_16x16.png %{buildroot}%{_iconsdir}/hicolor/16x16/%{shortname}.png
install -Dm644 dist/.icon-set/icon_32x32.png %{buildroot}%{_iconsdir}/hicolor/32x32/%{shortname}.png
install -Dm644 dist/.icon-set/icon_48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/%{shortname}.png
install -Dm644 dist/.icon-set/icon_64x64.png %{buildroot}%{_iconsdir}/hicolor/64x64/%{shortname}.png
install -Dm644 dist/.icon-set/icon_128x128.png %{buildroot}%{_iconsdir}/hicolor/128x128/%{shortname}.png
install -Dm644 dist/.icon-set/icon_256x256.png %{buildroot}%{_iconsdir}/hicolor/256x256/%{shortname}.png
install -Dm644 dist/.icon-set/icon_512x512.png %{buildroot}%{_iconsdir}/hicolor/512x512/%{shortname}.png
install -Dm644 dist/.icon-set/icon_1024.png %{buildroot}%{_iconsdir}/hicolor/1024x1024/%{shortname}.png
install -Dm644 flatpak/%{reverse_dns}.desktop %{buildroot}%{_datadir}/applications/%{shortname}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{shortname}.desktop

%files
%doc     README.md
%doc     CODE_OF_CONDUCT.md
%license COPYING
%license legendary.LICENSE
%license LICENSES.chromium.html
%license LICENSE.electron.txt
%license LICENSE.fonts
%dir %{_datadir}/%{shortname}
%{_datadir}/%{shortname}/*
%{_bindir}/%{shortname}
%{_bindir}/%{name}
%{_datadir}/applications/%{shortname}.desktop
%{_iconsdir}/hicolor/16x16/%{shortname}.png
%{_iconsdir}/hicolor/32x32/%{shortname}.png
%{_iconsdir}/hicolor/48x48/%{shortname}.png
%{_iconsdir}/hicolor/64x64/%{shortname}.png
%{_iconsdir}/hicolor/128x128/%{shortname}.png
%{_iconsdir}/hicolor/256x256/%{shortname}.png
%{_iconsdir}/hicolor/512x512/%{shortname}.png
%{_iconsdir}/hicolor/1024x1024/%{shortname}.png

%changelog
* Sun Mar 02 2025 Gilver E. <rockgrub@disroot.org>
- Update to 2.16.0
- Fix incorrect RPM dependencies
* Thu Jan 30 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
