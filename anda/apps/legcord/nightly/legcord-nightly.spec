%global commit 0b1a005936552abd5aed144bdc0ca5a82f2fa682
%global commit_date 20250622
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %nil
%global __strip /bin/true
%global __provides_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*))$
%ifnarch aarch64 
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\aarch64*\\.so.*))$
%elifarch aarch64
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*)|(.*\\x86_64*\\.so.*)|(.*\\x86-64*\\.so.*))$
%endif

Name:           legcord-nightly
Version:        %commit_date.%shortcommit
Release:        1%?dist
License:        OSL-3.0
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Group:          Applications/Internet
Packager:       Owen <owen@fyralabs.com>
Requires:       xdg-utils
Obsoletes:      armcord < 3.3.2-1
Conflicts:      legcord
BuildRequires:  anda-srpm-macros pnpm nodejs-npm git-core gcc gcc-c++ make desktop-file-utils zlib-ng-compat-devel

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%git_clone %{url}.git %{commit}

%build
pnpm install
pnpm run build
pnpm run package --linux AppImage tar.gz

%install
mkdir -p %{buildroot}%{_datadir}/legcord
%ifarch aarch64
mv dist/linux-arm64-unpacked/* %{buildroot}%{_datadir}/legcord
%else
mv dist/linux-unpacked/* -t %{buildroot}%{_datadir}/legcord
%endif

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_datadir}/legcord/legcord %{buildroot}%{_bindir}/legcord
install -Dm644 dist/.icon-set/icon_16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/legcord.png
install -Dm644 dist/.icon-set/icon_32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/legcord.png
install -Dm644 dist/.icon-set/icon_48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/legcord.png
install -Dm644 dist/.icon-set/icon_64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/legcord.png
install -Dm644 dist/.icon-set/icon_128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/legcord.png
install -Dm644 dist/.icon-set/icon_256.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/legcord.png
install -Dm644 dist/.icon-set/icon_512.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/legcord.png
install -Dm644 dist/.icon-set/icon_1024.png %{buildroot}%{_iconsdir}/hicolor/1024x1024/apps/legcord.png

dist/Legcord-*.AppImage --appimage-extract '*.desktop'
desktop-file-install --set-key=Exec --set-value="%{_datadir}/legcord/legcord %U" squashfs-root/legcord.desktop

%files
%doc README.md
%license license.txt
%{_bindir}/legcord
%{_datadir}/applications/legcord.desktop
%{_datadir}/legcord/
%{_iconsdir}/hicolor/16x16/apps/legcord.png
%{_iconsdir}/hicolor/32x32/apps/legcord.png
%{_iconsdir}/hicolor/48x48/apps/legcord.png
%{_iconsdir}/hicolor/64x64/apps/legcord.png
%{_iconsdir}/hicolor/128x128/apps/legcord.png
%{_iconsdir}/hicolor/256x256/apps/legcord.png
%{_iconsdir}/hicolor/512x512/apps/legcord.png
%{_iconsdir}/hicolor/1024x1024/apps/legcord.png

%changelog
* Fri Nov 22 2024 owen <owen@fyralabs.com> - 1.0.2-2
- Add nightly package.

* Mon Oct 21 2024 madonuko <mado@fyralabs.com> - 1.0.2-2
- Rename to LegCord.

* Mon Aug 26 2024 madonuko <mado@fyralabs.com> - 3.3.0-1
- Update to license.txt

* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.

* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.1.7-1
- Initial package
