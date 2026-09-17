%global appid           app.yaak.Yaak
%global tauri_dir       crates-tauri/yaak-app-client
%global wasm_pack_root  %{_builddir}/wasm-pack

Name:           yaak
Version:        2026.7.1
Release:        1%{?dist}
Summary:        A fast, privacy-first API client
License:        MIT
URL:            https://yaak.app
Source0:        https://github.com/mountain-loop/yaak/archive/refs/tags/v%{version}.tar.gz
Source1:        yaak.desktop
Packager:       Cypress Reed <cypress@fyralabs.com>

BuildRequires:  %{tauri_buildrequires -a}
BuildRequires:  anda-srpm-macros
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  typescript
BuildRequires:  desktop-file-utils
BuildRequires:  cargo
BuildRequires:  rust-std-static-wasm32-unknown-unknown
BuildRequires:  perl
BuildRequires:  cmake

%description
Yaak is a fast, privacy-first desktop API client for REST, GraphQL, Server-Sent
Events, WebSockets, and gRPC. It is offline-first, stores projects in a
Git-friendly format, and includes an extensible plugin system.

%prep
%autosetup -n yaak-%{version}
%tauri_prep -n %{tauri_dir}
# The upstream Tauri hook bootstraps every workspace, including the unrelated
# proxy app. Keep all plugin/template builds, but exclude the proxy workspace.
sed -i '/"apps\/yaak-proxy",/d; s|"bootstrap:build": "npm run build --workspace @yaakapp/yaak-client"|"bootstrap:build": "npm run build"|' package.json

# Yaak's templates workspace invokes wasm-pack, which is not available as an
# RPM dependency in the target repositories. Follow upstream's documented
# bootstrap and keep the tool isolated from the build environment.
cargo install --locked --root %{wasm_pack_root} wasm-pack

%build
export PATH="%{wasm_pack_root}/bin:$PATH"
export CMAKE_ARGS="${CMAKE_ARGS:-} -DCMAKE_POLICY_VERSION_MINIMUM=3.5"
# client:bundle selects the release Tauri configuration and builds the frontend,
# Rust application, sidecars, and Linux bundle through the upstream build script.
%npm_build -r client:bundle
%tauri_cargo_license_summary -f updater,license,wry
%{tauri_cargo_license -f updater,license,wry} > LICENSE.dependencies

%install
%tauri_install -f updater,license,wry
%desktop_file_install %{SOURCE1}
install -Dpm644 %{tauri_dir}/icons/icon.png \
    %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png
install -Dpm644 flatpak/app.yaak.Yaak.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%check
%desktop_file_validate %{buildroot}%{_appsdir}/yaak.desktop

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/yaak
%{_appsdir}/yaak.desktop
%{_hicolordir}/512x512/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
