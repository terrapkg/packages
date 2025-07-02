%define debug_package %nil
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:			feishin
Version:		0.17.0
Release:		1%?dist
Summary:		A modern self-hosted music player
License:		GPL-3.0
URL:			https://github.com/jeffvli/feishin
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:		fuse mpv
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	jq libxcrypt-compat pnpm

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
pnpm i
pnpm run postinstall
pnpm run build
%ifarch x86_64

%define a linux
%elifarch aarch64
%define a arm64
%endif

pnpm exec electron-builder --linux dir --%a

%install
mkdir -p %buildroot%_datadir/{pixmaps,applications} %buildroot%_bindir
mv dist/*-unpacked %buildroot%_datadir/feishin
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
