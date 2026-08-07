# terrible evil no good very bad hack
# fix one day
%global __requires_exclude_from (.*)lib(.*)so(.*)

Name:           legcord
%electronmeta -D
Version:        1.3.0
Release:        1%{?dist}
License:        OSL-3.0 AND %{electron_license}
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Source0:        Legcord.desktop
Group:          Applications/Internet
Packager:       madonuko <mado@fyralabs.com>
Requires:       xdg-utils
Obsoletes:      armcord < 3.3.2-1
Obsoletes:      legcord-bin < 1.1.5-2
Conflicts:      legcord-nightly
BuildRequires:  anda-srpm-macros pnpm nodejs-npm git-core gcc gcc-c++ make desktop-file-utils zlib-ng-compat-devel

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%git_clone %url v%version

%build
%pnpm_build -r build

%install
%electron_install -i legcord -l -I dist/.icon-set/
%desktop_file_install %{S:0}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/Legcord.desktop

%files
%doc README.md
%license license.txt
%{_bindir}/legcord
%{_datadir}/applications/Legcord.desktop
%{_libdir}/legcord/
%{_iconsdir}/hicolor/16x16/apps/legcord.png
%{_iconsdir}/hicolor/24x24/apps/legcord.png
%{_iconsdir}/hicolor/32x32/apps/legcord.png
%{_iconsdir}/hicolor/48x48/apps/legcord.png
%{_iconsdir}/hicolor/64x64/apps/legcord.png
%{_iconsdir}/hicolor/128x128/apps/legcord.png
%{_iconsdir}/hicolor/256x256/apps/legcord.png
%{_iconsdir}/hicolor/512x512/apps/legcord.png

%changelog
* Thu Jul 30 2026 Owen-sz <owen@fyralabs.com> - 1.3.0-1
- Vendor our own .desktop file

* Mon May 18 2026 june-fish <june@fyralabs.com> - 1.2.4-1
- Use electron macros

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
