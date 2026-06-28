%global commit 0a022f149000bdaed644c2609e19aa7b8badf825
%global commit_date 20260626
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# terrible evil no good very bad hack
# fix one day
%global __requires_exclude_from (.*)lib(.*)so(.*)

Name:           legcord-nightly
%electronmeta -aD
Version:        %commit_date.%shortcommit
Release:        1%{?dist}
License:        OSL-3.0 AND %{electron_license}
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Group:          Applications/Internet
Packager:       Owen <owen@fyralabs.com>
Requires:       xdg-utils
Obsoletes:      armcord < 3.3.2-1
Conflicts:      legcord
BuildRequires:  anda-srpm-macros pnpm nodejs-npm git-core gcc gcc-c++ make desktop-file-utils zlib-ng-compat-devel nvm

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%git_clone %{url}.git %{commit}
%vendor_nodejs -v 26

%build
%pnpm_build -r build

%install
%electron_install -i legcord -l -I dist/.icon-set/icon_16.png -I dist/.icon-set/icon_32.png -I dist/.icon-set/icon_48x48.png -I dist/.icon-set/icon_64.png -I dist/.icon-set/icon_128.png -I dist/.icon-set/icon_256.png -I dist/.icon-set/icon_512.png -I dist/.icon-set/icon_1024.png

dist/Legcord-*.AppImage --appimage-extract '*.desktop'
%desktop_file_install -k Exec,Icon -v "%{_libdir}/legcord-nightly/Legcord",legcord -u %U -f squashfs-root/legcord.desktop

%files
%doc README.md
%license license.txt
%{_bindir}/legcord-nightly
%{_datadir}/applications/legcord.desktop
%{_libdir}/legcord-nightly/
%{_iconsdir}/hicolor/16x16/apps/legcord.png
%{_iconsdir}/hicolor/32x32/apps/legcord.png
%{_iconsdir}/hicolor/48x48/apps/legcord.png
%{_iconsdir}/hicolor/64x64/apps/legcord.png
%{_iconsdir}/hicolor/128x128/apps/legcord.png
%{_iconsdir}/hicolor/256x256/apps/legcord.png
%{_iconsdir}/hicolor/512x512/apps/legcord.png
%{_iconsdir}/hicolor/1024x1024/apps/legcord.png

%changelog
* Mon May 18 2026 june-fish <june@fyralabs.com> - 1.2.4-1
- Use electron macros

* Fri Nov 22 2024 owen <owen@fyralabs.com> - 1.0.2-2
- Add nightly package.

* Mon Oct 21 2024 madonuko <mado@fyralabs.com> - 1.0.2-2
- Rename to LegCord.

* Mon Aug 26 2024 madonuko <mado@fyralabs.com> - 3.3.0-1
- Update to license.txt

* Sat Jun 17 2023 madonuko <mado@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.

* Sat May 6 2023 madonuko <mado@fyralabs.com> - 3.1.7-1
- Initial package
