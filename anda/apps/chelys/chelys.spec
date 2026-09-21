%undefine __brp_mangle_shebangs

%global appid io.github.texlyre.chelys

Name:           chelys
Version:        1.2.1
Release:        1%{?dist}
Summary:        A local desktop companion app for TeXlyre
URL:            https://github.com/TeXlyre/chelys
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.desktop
Source2:        %{appid}.metainfo.xml
License:        AGPL-3.0-or-later

BuildRequires:  cargo
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  anda-srpm-macros
BuildRequires:  %{tauri_buildrequires -a}
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%summary.

%prep
%git_clone
%tauri_prep

%build
%npm_build -r build -B

%install
install -Dm755 src-tauri/target/rpm/Chelys %{buildroot}%{_bindir}/Chelys
%desktop_file_install %{SOURCE1}
%terra_appstream -o %{SOURCE2}

install -Dm644 src-tauri/icons/128x128.png %{buildroot}%{_hicolordir}/128x128/apps/chelys.png
install -Dm644 src-tauri/icons/128x128@2x.png %{buildroot}%{_hicolordir}/256x256/apps/chelys.png
install -Dm644 src-tauri/icons/32x32.png %{buildroot}%{_hicolordir}/32x32/apps/chelys.png
%{tauri_cargo_license} > LICENSE.dependencies

%check
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/Chelys
%{_hicolordir}/128x128/apps/chelys.png
%{_hicolordir}/256x256/apps/chelys.png
%{_hicolordir}/32x32/apps/chelys.png
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Mon Jan 19 2026 Cypress Reed <cypress@fyralabs.com>
- Initial commit
