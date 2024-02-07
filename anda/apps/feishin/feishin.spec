Name:			feishin
Version:		0.5.3
Release:		1%?dist
Summary:		A modern self-hosted music player 
License:		GPL-3.0
URL:			https://github.com/jeffvli/feishin
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	nodejs-npm mpv jq

%description
%summary.

%prep
%autosetup

cat package.json | jq '.author += { "email": "jeffvictorli@gmail.com" }' | jq '.build.linux += { "maintainer": "mado@fyralabs.com", "vendor": "Fyra Labs Terra" }' > a
mv a package.json
cat package.json

cat<<EOF > feishin.desktop
[Desktop Entry]
Type=Application
Name=Feishin
Comment=Rewrite of Sonixd
Exec=/usr/bin/feishin
Icon=feishin
Terminal=false
Categories=Network;Audio;Music
Keywords=Music;Jellyfin;Audio;Stream;Sonixd
EOF

%build
npm i --legacy-peer-deps update-browserslist-db@latest
npm audit fix --force
npx update-browserslist-db@latest
npm run build
%ifarch x86_64

%define a linux
%elifarch aarch64
%define a arm64
%endif

npx electron-builder -- --%a

%install
mkdir -p %buildroot%_datadir/{feishin,pixmaps,applications} %buildroot%_bindir
tar xf release/build/Feishin-*.tar.xz -C %buildroot%_datadir/feishin/ --strip-components=1
install -Dm644 assets/icons/icon.png %buildroot%_datadir/pixmaps/feishin.png
ln -s %_datadir/feishin/feishin %_buildroot%_bindir/feishin
install -Dm644 feishin.desktop %buildroot%_datadir/applications/

%files
%doc README.md CHANGELOG.md
%license LICENSE
%_bindir/feishin
%_datadir/feishin/
%_datadir/applications/feishin.desktop
%_datadir/pixmaps/feishin.png

%changelog
%autochangelog
