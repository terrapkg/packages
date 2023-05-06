%define debug_package %nil

%ifarch x86_64
%global src ArmCord-%version
%elifarch aarch64
%global src ArmCord-%version-arm64
%elifarch armv7l
%global src ArmCord-%version-armv7l
%endif

Name:			armcord-bin
Version:		3.1.7
Release:		1%?dist
License:		OSL-3.0
Summary:		Custom lightweight Discord client designed to enhance your experience
URL:			https://github.com/ArmCord/ArmCord
Group:			Applications/Internet
Source0:		%url/releases/download/v%version/%src.tar.gz
Source1:		armcord.png
Requires:		electron libnotify xdg-utils
ExclusiveArch:	x86_64 aarch64 armv7l
Conflicts:		armcord

%description
ArmCord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%autosetup -n %src

cat <<EOF > .armcord.desktop
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

%install
mkdir -p %buildroot/usr/bin %buildroot/usr/share/applications %buildroot/usr/share/pixmaps %buildroot/opt/armcord
cp -a * %buildroot/opt/armcord
ln -s /opt/armcord/armcord %buildroot/usr/bin/armcord
chmod +x -R %buildroot/opt/armcord/*
chmod 755 %buildroot/opt/armcord/armcord
install -Dm644 .armcord.desktop %buildroot/usr/share/applications/ArmCord.desktop
install -Dm644 %SOURCE1 %buildroot/usr/share/pixmaps/armcord.png

%files
/opt/armcord
/usr/bin/armcord
/usr/share/applications/ArmCord.desktop
/usr/share/pixmaps/armcord.png

%changelog
* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package

