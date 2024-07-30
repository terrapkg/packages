%define debug_package %nil
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:			feishin
Version:		0.7.2
Release:		1%?dist
Summary:		A modern self-hosted music player
License:		GPL-3.0
URL:			https://github.com/jeffvli/feishin
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:		fuse mpv
BuildRequires:	nodejs-npm jq libxcrypt-compat

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
npm install --legacy-peer-deps
npm run postinstall
npm run build
%ifarch x86_64

%define a linux
%elifarch aarch64
%define a arm64
%endif

npx electron-builder --linux dir --%a

%install
mkdir -p %buildroot%_datadir/{pixmaps,applications} %buildroot%_bindir
mv release/build/*-unpacked %buildroot%_datadir/feishin
install -Dm644 assets/icons/icon.png %buildroot%_datadir/pixmaps/feishin.png
ln -s %_datadir/feishin/feishin %buildroot%_bindir/feishin
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
