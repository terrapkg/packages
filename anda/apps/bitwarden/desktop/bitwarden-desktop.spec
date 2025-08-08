%ifarch aarch64
%global armsuffix -arm64
%endif

Name:           bitwarden-desktop
Version:        2025.7.0
Release:        1%?dist
Summary:        Bitwarden desktop client
License:        GPL-3.0-only
URL:            https://bitwarden.com
Source0:        https://github.com/bitwarden/clients/archive/refs/tags/desktop-v%version.tar.gz

Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  nodejs-npm
BuildRequires:  electron
BuildRequires:  rpm_macro(cargo_install)

%electronmeta

%description
%summary.

%prep
%autosetup -n clients-desktop-v%version
npm ci --include optional --include dev --include prod

%build
pushd apps/desktop
touch electron-rebuild && chmod +x ./electron-rebuild
cat<<EOF > husky
#!/bin/sh
yes | npx husky
EOF
chmod +x ./husky
export PATH="$PATH:$(pwd)"
npm ci --include optional --include dev --include prod
pushd desktop_native/napi
npm i & 
%cargo_prep_online
#cargo_license_summary_online
%{cargo_license_online} > ../../../../LICENSE.napi_dependencies
wait
CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' \
  npm exec napi build --platform --js false --profile rpm -- & #--target %_arch-unknown-linux-gnu
popd
pushd desktop_native/proxy
%cargo_prep_online
#cargo_license_summary_online
%{cargo_license_online} > ../../../../LICENSE.proxy_dependencies
#cargo_build
popd
NODE_ENV=production npm exec webpack --config ./webpack.preload.js &
NODE_ENV=production npm exec webpack --config ./webpack.main.js &
NODE_ENV=production npm exec webpack --config ./webpack.renderer.js &
wait
rm -rf ./dist
yes | npm exec electron-builder --dir # -p never

%install
pushd apps/desktop
pushd desktop_native/proxy
%cargo_install
popd
%electron_install

%files
%doc README.md SECURITY.md CONTRIBUTING.md
%license LICENSE.txt LICENSE_GPL.txt LICENSE_BITWARDEN.txt
%license LICENSE.napi_dependencies LICENSE.proxy_dependencies
