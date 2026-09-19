%undefine __brp_mangle_shebangs

%global appid           app.yaak.Yaak
%global tauri_dir       crates-tauri/yaak-app-client
%global wasm_pack_root  %{_builddir}/wasm-pack

Name:           yaak
Version:        2026.7.1
Release:        1%{?dist}
Summary:        A fast, privacy-first API client
SourceLicense:  MIT
License:        %{sourcelicense} AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR BSL-1.0) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://yaak.app
Source0:        https://github.com/mountain-loop/yaak/archive/refs/tags/v%{version}.tar.gz
Source1:        app.yaak.Yaak.desktop

BuildRequires:  %{tauri_buildrequires -a}
BuildRequires:  anda-srpm-macros
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  typescript
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  cargo
BuildRequires:  rust-std-static-wasm32-unknown-unknown
BuildRequires:  perl
BuildRequires:  cmake
BuildRequires:  wasm-pack
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Yaak is a fast, privacy-first desktop API client for REST, GraphQL, Server-Sent
Events, WebSockets, and gRPC. It is offline-first, stores projects in a
Git-friendly format, and includes an extensible plugin system.

%prep
%autosetup -n yaak-%{version}
%tauri_prep -n %{tauri_dir}
sed -i '/"apps\/yaak-proxy"/d; s|"apps/yaak-client",|"apps/yaak-client"|; s|"bootstrap:build": "npm run build --workspace @yaakapp/yaak-client"|"bootstrap:build": "npm run build"|' package.json
sed -i 's|"targets": \["app", "appimage", "deb", "dmg", "nsis", "rpm"\]|"targets": []|' \
    %{tauri_dir}/tauri.release.conf.json

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# cc-rs appends target-specific flags to global CFLAGS. Fedora's host flags
# contain x86-only options that clang rejects for WASM, so use a portable C
# baseline for this mixed native/WASM build.
export CFLAGS="-O2 -g -ffunction-sections -fdata-sections -fPIC"
export CFLAGS_wasm32_unknown_unknown="-O3 -ffunction-sections -fdata-sections -fPIC"
export CFLAGS_wasm64_unknown_unknown="-O3 -ffunction-sections -fdata-sections -fPIC"
%npm_build -r client:bundle
%tauri_cargo_license_summary -f updater,license,wry
%{tauri_cargo_license -f updater,license,wry} > LICENSE.dependencies

%install
# cargo2rpm cannot infer a crate name from Yaak's workspace manifest, but
# Tauri produces the application binary at this known target path.
install -Dpm755 target/release/yaak-app-client \
    %{buildroot}%{_bindir}/yaak
%desktop_file_install %{SOURCE1}
install -Dpm644 %{tauri_dir}/icons/icon.png \
    %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png
install -Dpm644 flatpak/%{appid}.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%check
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/yaak
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/512x512/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
