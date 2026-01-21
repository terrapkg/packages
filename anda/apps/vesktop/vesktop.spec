%define debug_package %nil

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/vesktop/.*\\.so

Name:		vesktop
Obsoletes:  VencordDesktop < 1.5.8-1
Obsoletes:  vencord-desktop < 1.5.8-1
Version:	1.6.3
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
Exec=/usr/bin/vesktop
Icon=vesktop
Categories=Network;InstantMessaging;
StartupWMClass=vesktop

Keywords=discord;vesktop;vencord;shelter;armcord;electron;
EOF


%build
npx pnpm install --no-frozen-lockfile
npx pnpm package:dir


%install

mkdir -p %buildroot/usr/share/vesktop
cp -r dist/*-unpacked/. %buildroot/usr/share/vesktop/.

install -Dm755 dist/*-unpacked/vesktop %buildroot/usr/bin/vesktop
ln -sf /usr/share/vesktop/vesktop %buildroot/usr/bin/vesktop
ln -sf /usr/bin/vesktop %buildroot/usr/bin/vencorddesktop
install -Dm644 vesktop.desktop %{buildroot}%{_datadir}/applications/vesktop.desktop
install -Dm644 build/icon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/vesktop.svg

%files
%doc README.md
%license LICENSE
%{_bindir}/vesktop
%{_bindir}/vencorddesktop
%{_datadir}/applications/vesktop.desktop
%{_iconsdir}/hicolor/scalable/apps/vesktop.svg
%{_datadir}/vesktop/*

%changelog
* Thu Jul 24 2025 Atmois <info@atmois.com> - 1.5.8-2
- Rename from vencord-desktop to vesktop and amend the spec file accordingly
* Tue Nov 07 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 0.4.3-1
- Initial package

