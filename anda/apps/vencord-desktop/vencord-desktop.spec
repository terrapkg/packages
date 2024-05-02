%define debug_package %nil

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/vesktop/.*\\.so

Name:		vencord-desktop
Provides:   VencordDesktop = %{version}-%{release}
Version:	1.5.2
Release:	1%?dist
License:	GPL-3.0
Summary:	Vesktop is a cross platform desktop app aiming to give you a snappier Discord experience with Vencord pre-installed
URL:		https://github.com/Vencord/Vesktop
Group:		Applications/Internet
#Source1:	launch.sh
Source0:    https://github.com/Vencord/Vesktop/archive/refs/tags/v%{version}.tar.gz
Requires:   xdg-utils
BuildRequires:	nodejs-npm git
# Conflicts:	vesktop-bin

%description
vesktop is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
git init
git remote add origin %url || :
git reset --hard
git fetch
git checkout v%version

cat <<EOF > vesktop.desktop
[Desktop Entry]
Name=Vesktop
Comment=%summary
GenericName=Internet Messenger
Type=Application
Exec=/usr/bin/vencorddesktop
Icon=vesktop
Categories=Network;InstantMessaging;
StartupWMClass=VencordDesktop

Keywords=discord;vesktop;vencord;shelter;armcord;electron;
EOF


%build
npx pnpm@8 install --no-frozen-lockfile
npx pnpm@8 package:dir


%install

mkdir -p %buildroot/usr/share/vesktop
cp -r dist/*-unpacked/. %buildroot/usr/share/vesktop/.

install -Dm755 dist/*-unpacked/vencorddesktop %buildroot/usr/bin/vencorddesktop
ln -sf /usr/share/vesktop/vencorddesktop %buildroot/usr/bin/vencorddesktop
install -Dm644 vesktop.desktop %buildroot/usr/share/applications/vesktop.desktop
install -Dm644 build/icon.png %buildroot/usr/share/pixmaps/vesktop.png

%files
%doc README.md
%license LICENSE
/usr/bin/vencorddesktop
/usr/share/applications/vesktop.desktop
/usr/share/pixmaps/vesktop.png
/usr/share/vesktop/*

%changelog
* Tue Nov 07 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 0.4.3-1
- Initial package


