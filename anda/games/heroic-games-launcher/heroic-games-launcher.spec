%global org_name Heroic-Games-Launcher
%global git_name %(echo %{org_name} | sed 's/-//g')
%global appid com.heroicgameslauncher.hgl
%global shortname heroic
%global legendary_version 0.20.39
%global gogdl_version 1.2.0
%global nile_version 1.1.2
%global comet_version 0.2.0

Name:          %{shortname}-games-launcher
Version:       2.19.1
Release:       2%?dist
Summary:       A games launcher for GOG, Amazon, and Epic Games
License:       GPL-3.0-only AND MIT AND BSD-3-Clause
URL:           https://heroicgameslauncher.com
BuildRequires: anda-srpm-macros
BuildRequires: pnpm
Requires:      alsa-lib
Requires:      gtk3
Requires:      hicolor-icon-theme
Requires:      nss
Requires:      python3
Requires:      which
Recommends:    (falcond or gamemode)
Recommends:    mangohud
Recommends:    umu-launcher
Provides:      bundled(comet) = %{comet_version}
Provides:      bundled(gogdl) = %{gogdl_version}
Provides:      bundled(legendary) = %{legendary_version}
Provides:      bundled(nile) = %{nile_version}
Packager:      Gilver E. <roachy@fyralabs.com>

%electronmeta -D

%description
Heroic is a Free and Open Source Epic, GOG, and Amazon Prime Games launcher for Linux, Windows, and macOS.

%prep
%git_clone https://github.com/%{org_name}/%{git_name} v%{version}

%build
%pnpm_build -r download-helper-binaries -v

%install
rm -rf dist/linux-unpacked/resources/app.asar.unpacked/node_modules/font-list/libs/{darwin,win32}
rm -rf dist/linux-unpacked/resources/app.asar.unpacked/node_modules/font-list/libs/{darwin,win32}
%ifarch aarch64
# Keep the x86_64 Windows binaries run through Wine just in case
rm -rf dist/linux-unpacked/resources/app.asar.unpacked/build/bin/x64/{darwin,linux}
%else
rm -rf dist/linux-unpacked/resources/app.asar.unpacked/build/bin/arm64
%endif

%electron_install -d heroic -b heroic -S heroic -I -i %{appid} -l
%desktop_file_install -k Exec -v %{_libdir}/%{shortname}/%{shortname} -u %u flatpak/%{appid}.desktop

install -Dpm644 flatpak/templates/%{appid}.metainfo.xml.template %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%doc     README.md
%doc     CODE_OF_CONDUCT.md
%license COPYING
%license bundled_licenses/*
%{_libdir}/%{shortname}/
%{_bindir}/%{shortname}
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/16x16/apps/%{appid}.png
%{_hicolordir}/32x32/apps/%{appid}.png
%{_hicolordir}/48x48/apps/%{appid}.png
%{_hicolordir}/64x64/apps/%{appid}.png
%{_hicolordir}/128x128/apps/%{appid}.png
%{_hicolordir}/256x256/apps/%{appid}.png
%{_hicolordir}/512x512/apps/%{appid}.png
%{_hicolordir}/1024x1024/apps/%{appid}.png

%changelog
* Sun Mar 02 2025 Gilver E. <rockgrub@disroot.org>
- Update to 2.16.0
- Fix incorrect RPM dependencies
* Thu Jan 30 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
