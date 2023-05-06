Name:			armcord
Version:		3.1.7
Release:		1%?dist
License:		OSL-3.0
Summary:		Custom lightweight Discord client designed to enhance your experience
URL:			https://github.com/ArmCord/ArmCord
Group:			Applications/Internet
Source0:		%url/archive/refs/tags/v%version.tar.gz
Source1:		launch.sh
Requires:		electron libnotify xdg-utils
BuildRequires:	nodejs-npm
Conflicts:		armcord-bin

%description
ArmCord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%autosetup -n ArmCord-%version

cat <<EOF > armcord.desktop
[Desktop Entry]
Name=ArmCord
Comment=%summary
GenericName=Internet Messenger
Type=Application
Exec=/usr/bin/armcord
Icon=armcord
Categories=Internet;Network;InstantMessaging;
StartupWMClass=armcord
Keywords=discord;armcord;vencord;shelter;electron;
EOF


%build
npx pnpm@6.0 install --frozen-lockfile --ignore-scripts
npm run packageQuick


%install
install -Dm644 dist/*-unpacked/resources/app.asar %buildroot/usr/share/armcord/app.asar

install -Dm755 %SOURCE1 %buildroot/usr/bin/armcord
install -Dm644 armcord.desktop %buildroot/usr/share/applications/ArmCord.desktop
install -Dm644 build/icon.png %buildroot/usr/share/pixmaps/armcord.png

%files
%doc README.md
%license LICENSE
/usr/bin/armcord
/usr/share/applications/ArmCord.desktop
/usr/share/pixmaps/armcord.png
/usr/share/armcord/app.asar

%changelog
* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package

