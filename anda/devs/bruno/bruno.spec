Name:           bruno
Version:        1.21.0
Release:        1%?dist
Summary:        Opensource API Client for Exploring and Testing APIs
License:        MIT
URL:            https://www.usebruno.com
Source0:        https://github.com/usebruno/bruno/archive/refs/tags/v%version.tar.gz
Source1:        com.usebruno.app.Bruno.desktop
Source2:        bruno.sh
Requires:       electron alsa-lib
BuildRequires:  nodejs-npm asar electron

%description
Bruno is a new and innovative API client, aimed at revolutionizing the status quo represented by Postman and similar tools out there.

%prep
%autosetup

# ref aur
# disabling husky however I can since I'm not in a git repository
sed -i -e 's/"husky":.*//g' -e 's/"husky install"/"true"/g' package.json

%build
export NODE_ENV=production
export NODE_OPTIONS=--openssl-legacy-provider

npm i --include=dev
npm run build:bruno-query
npm run build:bruno-common
npm run build:graphql-docs
npm run build:web

electronDist="%_libdir/electron"
electronVer="$(cat ${electronDist}/version)"
sed -i -e "s~\"dist:linux\":.*~\"dist:linux\": \"electron-builder --linux --x64 --dir --config electron-builder-config.js -c.electronDist=${electronDist} -c.electronVersion=${electronVer}\",~g" packages/bruno-electron/package.json

npm run build:electron:linux

%install
mkdir -p %buildroot%_datadir/applications/
install -Dm644 %SOURCE1 %buildroot%_datadir/applications/
install -Dm755 %SOURCE2 %buildroot%_bindir/bruno

install -d %buildroot%_libdir/bruno
asar e packages/bruno-electron/out/linux-unpacked/resources/app.asar %buildroot%_libdir/bruno/

for i in 16 24 48 64 128 256 512 1024; do
  install -Dm644 "packages/bruno-electron/resources/icons/png/${i}x${i}.png" "%buildroot%_iconsdir/hicolor/${i}x${i}/apps/com.usebruno.app.Bruno.png"
done

%files
%doc readme.md
%license license.md
%_bindir/bruno/
%_libdir/bruno/
%_datadir/applications/com.usebruno.app.Bruno.desktop
%_iconsdir/hicolor/*/apps/com.usebruno.app.Bruno.png
