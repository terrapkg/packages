%global git_name GoofCord
%global debug_package %{nil}
# Exclude private libraries
%global __provides_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*))$
%ifnarch aarch64 armv7hl armv7l
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\aarch64*\\.so.*))$
%elifarch aarch64 armv7hl armv7l
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\x86_64*\\.so.*)|(.*\\x86-64*\\.so.*))$
%endif

Name:          goofcord
Version:       1.10.1
Release:       1%{?dist}
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: bun-bin
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: nodejs
BuildRequires: nodejs-npm
BuildRequires: python3
%ifarch aarch64
BuildRequires: zlib-ng-compat-devel
%endif
Packager:      Gilver E. <rockgrub@disroot.org>

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -n %{git_name}-%{version}

%build
%ifarch aarch64 armv7hl armv7l
sed -i '/\"x64\",/d' electron-builder.ts
%endif
bun install
bun run packageLinux

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
%ifarch x86_64
mv dist/linux-unpacked/* -t %{buildroot}%{_datadir}/%{name}
%elifarch aarch64
mv dist/linux-arm64-unpacked/* -t %{buildroot}%{_datadir}/%{name}
%elifarch armv7hl armv7l
mv dist/linux-armv7l-unpacked/* -t %{buildroot}%{_datadir}/%{name}
%endif

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 dist/.icon-set/icon_16x16.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_32.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_48x48.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_64.png %{buildroot}/%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_128.png %{buildroot}/%{_iconsdir}/hicolor/128x128/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_256.png %{buildroot}/%{_iconsdir}/hicolor/256x256/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_512.png %{buildroot}/%{_iconsdir}/hicolor/512x512/apps/%{name}.png
install -Dm644 dist/.icon-set/icon_1024.png %{buildroot}/%{_iconsdir}/hicolor/1024x1024/apps/%{name}.png

%ifarch x86_64
dist/%{git_name}-*x86_64.AppImage --appimage-extract '*.desktop'
%elifarch aarch64
dist/%{git_name}-*arm64.AppImage --appimage-extract '*.desktop'
%elifarch armv7hl armv7l
dist/%{git_name}-*armv7l.AppImage --appimage-extract '*.desktop'
%endif
desktop-file-install --set-key=Exec --set-value="%{_datadir}/%{name}/%{name} --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform-hint=auto %U" squashfs-root/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/256x256/apps/%{name}.png
%{_iconsdir}/hicolor/512x512/apps/%{name}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1-1
- Initial package
