%define debug_package %nil
%global _build_id_links none

%ifarch x86_64
%global src Legcord-%version-linux-x64
%elifarch aarch64
%global src Legcord-%version-linux-arm64
%elifarch armv7l
%global src Legcord-%version-linux-armv7l
%endif

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/(armcord|legcord)/.*\\.so

Name:           legcord-bin
Version:        1.1.1
Release:        1%?dist
License:        OSL-3.0
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Group:          Applications/Internet
Source0:        %url/releases/download/v%version/%src.tar.gz
Source1:        legcord.png
Source2:        https://raw.githubusercontent.com/Legcord/Legcord/v%version/README.md
Requires:       xdg-utils
ExclusiveArch:  x86_64 aarch64 armv7l
Conflicts:      legcord
Conflicts:      legcord-nightly
BuildRequires:  add-determinism
Obsoletes:      armcord < 3.3.2-1

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%autosetup -n %src

cat <<EOF > .legcord.desktop
[Desktop Entry]
Name=Legcord
Comment=%summary
GenericName=Internet Messenger
Type=Application
Exec=%_bindir/legcord
Icon=legcord
Categories=Network;InstantMessaging;
StartupWMClass=legcord
Keywords=discord;armcord;legcord;vencord;shelter;electron;
EOF

%build

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/applications %buildroot%_datadir/pixmaps %buildroot%_datadir/legcord %buildroot%_docdir/%name
cp -a * %buildroot%_datadir/legcord/
ln -s %_datadir/legcord/legcord %buildroot%_bindir/legcord
ln -s %_datadir/legcord %buildroot%_datadir/armcord
chmod +x -R %buildroot%_datadir/legcord/*
chmod 755 %buildroot%_datadir/legcord/legcord
install -Dm644 .legcord.desktop %buildroot%_datadir/applications/LegCord.desktop
install -Dm644 %SOURCE1 %buildroot%_datadir/pixmaps/legcord.png
install -Dm644 %SOURCE2 %buildroot%_docdir/%name/

# HACK: rpm bug for unability to replace existing files on system.
%pre
if [ -d %_datadir/armcord ] && [ ! -L %_datadir/armcord ]; then
  echo "Found old %_datadir/armcord directory, removing…"
  rm -rf %_datadir/armcord
fi

%files
%doc README.md
%_datadir/legcord
%_datadir/armcord
%_bindir/legcord
%_datadir/applications/LegCord.desktop
%_datadir/pixmaps/legcord.png

%changelog
* Mon Oct 21 2024 madonuko <mado@fyralabs.com> - 1.0.2-2
- Rename to LegCord.

* Sat Jun 17 2023 madonuko <mado@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.
- Use /usr/share/ instead of /opt/

* Sat May 6 2023 madonuko <mado@fyralabs.com> - 3.1.7-1
- Initial package
