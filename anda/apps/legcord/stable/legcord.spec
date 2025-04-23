%define debug_package %nil

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/(armcord|legcord)/.*\\.so

Name:           legcord
Version:        1.1.1
Release:        1%?dist
License:        OSL-3.0
Summary:        Custom lightweight Discord client designed to enhance your experience
URL:            https://github.com/Legcord/Legcord
Group:          Applications/Internet
Source1:        launch.sh
Packager:       madonuko <mado@fyralabs.com>
Requires:       electron xdg-utils
Provides:       armcord
Obsoletes:      armcord < 3.3.2-1
Conflicts:      legcord-bin
Conflicts:      legcord-nightly
BuildArch:      noarch
BuildRequires:  anda-srpm-macros pnpm

%description
Legcord is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
%git_clone %url v%version

cat <<EOF > legcord.desktop
[Desktop Entry]
Name=Legcord
Comment=%summary
GenericName=Internet Messenger
Type=Application
Exec=/usr/bin/legcord
Icon=legcord
Categories=Network;InstantMessaging;
StartupWMClass=legcord
Keywords=discord;armcord;legcord;vencord;shelter;electron;
EOF


%build
pnpm install --no-frozen-lockfile
pnpm run packageQuick


%install
install -Dm644 dist/*-unpacked/resources/app.asar %buildroot/usr/share/legcord/app.asar

install -Dm755 %SOURCE1 %buildroot/usr/bin/legcord
install -Dm644 legcord.desktop %buildroot/usr/share/applications/LegCord.desktop
install -Dm644 build/icon.png %buildroot/usr/share/pixmaps/legcord.png

ln -s %_datadir/legcord %buildroot%_datadir/armcord

# HACK: rpm bug for unability to replace existing files on system.
%pre
if [ -d %_datadir/armcord ] && [ ! -L %_datadir/armcord ]; then
  echo "Found old %_datadir/armcord directory, removing…"
  rm -rf %_datadir/armcord
fi

%files
%doc README.md
%license license.txt
/usr/bin/legcord
/usr/share/applications/LegCord.desktop
/usr/share/pixmaps/legcord.png
/usr/share/legcord/app.asar
/usr/share/armcord

%changelog
* Mon Oct 21 2024 madonuko <mado@fyralabs.com> - 1.0.2-2
- Rename to LegCord.

* Mon Aug 26 2024 madonuko <mado@fyralabs.com> - 3.3.0-1
- Update to license.txt

* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.2.0-2
- Remove libnotify dependency.
- Fix desktop entry.
- Set as noarch package because there are not binary files.

* Sat May 6 2023 windowsboy111 <windowsboy111@fyralabs.com> - 3.1.7-1
- Initial package
