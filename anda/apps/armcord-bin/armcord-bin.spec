%define debug_package %nil
%global _build_id_links none

%ifarch x86_64
%global src ArmCord-%version-linux-x64
%elifarch aarch64
%global src ArmCord-%version-linux-arm64
%elifarch armv7l
%global src ArmCord-%version-linux-armv7l
%endif

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/armcord/.*\\.so

Name:			armcord-bin
Version:		3.3.1
Release:		1%?dist
License:		OSL-3.0
Summary:		Custom lightweight Discord client designed to enhance your experience
URL:			https://github.com/ArmCord/ArmCord
Group:			Applications/Internet
Source0:		%url/releases/download/v%version/%src.tar.gz
Source1:		armcord.png
Source2:		https://raw.githubusercontent.com/ArmCord/ArmCord/v%version/README.md
Requires:		electron xdg-utils
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
Exec=%_bindir/armcord
Icon=armcord
Categories=Network;InstantMessaging;
StartupWMClass=armcord
Keywords=discord;armcord;vencord;shelter;electron;
EOF

%build

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/applications %buildroot%_datadir/pixmaps %buildroot%_datadir/armcord %buildroot%_docdir/%name
cp -a * %buildroot%_datadir/armcord/
ln -s %_datadir/armcord/armcord %buildroot%_bindir/armcord
chmod +x -R %buildroot%_datadir/armcord/*
chmod 755 %buildroot%_datadir/armcord/armcord
install -Dm644 .armcord.desktop %buildroot%_datadir/applications/ArmCord.desktop
install -Dm644 %SOURCE1 %buildroot%_datadir/pixmaps/armcord.png
install -Dm644 %SOURCE2 %buildroot%_docdir/%name/

%files
%doc README.md
%_datadir/armcord
%_bindir/armcord
%_datadir/applications/ArmCord.desktop
%_datadir/pixmaps/armcord.png

%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.
- Use /usr/share/ instead of /opt/

* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.1.7-1
- Initial package
