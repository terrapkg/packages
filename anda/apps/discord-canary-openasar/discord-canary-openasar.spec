%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           discord-canary-openasar
Version:        0.0.423
Release:        1%?dist
Summary:        A snappier Discord rewrite with features like further customization and theming
License:        MIT AND https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl-canary.discordapp.net/apps/linux/%{version}/discord-canary-%{version}.tar.gz
Source1:        %{url}/releases/download/nightly/app.asar
Group:          Applications/Internet
Requires:       glibc GConf2
Requires:       nspr >= 4.13
Requires:       nss >= 3.27
Requires:       libX11 >= 1.6
Requires:       libXtst >= 1.2
ExclusiveArch:  x86_64

%description
OpenAsar is a rewrite of part of Discord's desktop code, making it snappier and
include more features like further customization and theming.

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
ln -s %_datadir/discord-canary-openasar/discord-canary.desktop %{buildroot}%{_datadir}/applications/discord-canary-openasar.desktop
ln -s %_datadir/discord-canary-openasar/discord.png %{buildroot}%{_datadir}/pixmaps/discord-canary-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-canary-openasar/resources/app.asar
chmod o+w %{buildroot}%{_datadir}/discord-canary-openasar/resources -R


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
