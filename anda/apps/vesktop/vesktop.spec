%define debug_package %nil

%global giturl https://github.com/Vencord/Vesktop
%global appid dev.vencord.Vesktop

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/vesktop/.*\\.so

Name:		vesktop
Obsoletes:  VencordDesktop < 1.5.8-1
Obsoletes:  vencord-desktop < 1.5.8-1
Version:	1.6.4
Release:	2%?dist
License:	GPL-3.0
Summary:	Vesktop is a cross platform desktop app aiming to give you a snappier Discord experience with Vencord pre-installed
URL:		https://vesktop.dev
Group:		Applications/Internet
#Source1:	launch.sh
Source0:    %{giturl}/archive/refs/tags/v%{version}.tar.gz
Source1:    %{giturl}/releases/download/v%{version}/%{appid}.metainfo.xml
Requires:   xdg-utils
%if 0%{?fedora} >= 44
BuildRequires: nodejs24-npm-bin git
%else
BuildRequires:	nodejs-npm git
%endif
# Conflicts:	vesktop-bin

%description
vesktop is a custom client designed to enhance your Discord experience
while keeping everything lightweight.

%prep
git init
git remote add origin %giturl || :
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
install -Dm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/vesktop
%{_bindir}/vencorddesktop
%{_datadir}/applications/vesktop.desktop
%{_iconsdir}/hicolor/scalable/apps/vesktop.svg
%{_datadir}/vesktop/*
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Feb 04 2026 Kaitlyn <kaitlynyaa@kaitlynyaa.dev> - 1.6.4
- Added appstream metainfo and fixed buildrequires to adhere to new npm package naming scheme
* Thu Jul 24 2025 Atmois <info@atmois.com> - 1.5.8-2
- Rename from vencord-desktop to vesktop and amend the spec file accordingly
* Tue Nov 07 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 0.4.3-1
- Initial package

