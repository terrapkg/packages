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
SourceLicense:  AGPL-3.0-or-later
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND Zlib AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND MIT AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  cargo
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  anda-srpm-macros
BuildRequires:  %{tauri_buildrequires -a}
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream
Recommends:     podman

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
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%check
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/Chelys
%{_hicolordir}/128x128/apps/chelys.png
%{_hicolordir}/256x256/apps/chelys.png
%{_hicolordir}/32x32/apps/chelys.png
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Mon Sep 21 2026 Cypress Reed <cypress@fyralabs.com>
- Initial commit
