%define debug_package %{nil}
%define commit 40b27dd1b8dd48277207db1b165c220c3441484c

Name:           discord-canary-openasar
Version:        0.0.146
Release:        3%{?dist}
Summary:        OpenAsar is a rewrite of part of Discord's desktop code, making it snappier and include more features like further customization and theming
License:        MIT and https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl-canary.discordapp.net/apps/linux/%{version}/discord-canary-%{version}.tar.gz
Source1:        %{url}/releases/download/nightly/app.asar
Requires:       libatomic, glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27, libstdc++, libX11 >= 1.6, libXtst >= 1.2, libappindicator, libcxx, libXScrnSaver
ExclusiveArch:  x86_64

%description
%{summary}.

%prep
%autosetup -n DiscordCanary

%build
sed "s@discord-canary@discord-canary-openasar@g" discord-canary.desktop > a
sed "s@Discord Canary@Discord Canary OpenAsar@g" a > discord-canary.desktop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-canary-openasar
cp -rv * %{buildroot}%{_datadir}/discord-canary-openasar
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord-canary.desktop %{buildroot}%{_datadir}/applications/discord-canary-openasar.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-canary-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-canary-openasar/app.asar


%files
%{_datadir}/discord-canary-openasar/
%{_datadir}/applications/discord-canary-openasar.desktop
%{_datadir}/pixmaps/discord-canary-openasar.png


%changelog
* Wed Jan 18 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.0.146-1
- Renamed from openasar-canary to discord-canary-openasar
- Fix issues after removing discord-canary package
- Bundle discord-canary

* Thu Oct 20 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- 
