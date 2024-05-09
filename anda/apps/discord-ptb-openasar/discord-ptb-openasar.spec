%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           discord-ptb-openasar
Version:        0.0.85
Release:        1%?dist
Summary:        A snappier Discord rewrite with features like further customization and theming
License:        MIT AND https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl-ptb.discordapp.net/apps/linux/%{version}/discord-ptb-%{version}.tar.gz
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
%autosetup -n DiscordPTB

%build
sed "s@discord-ptb@discord-ptb-openasar@g" discord-ptb.desktop > a
sed "s@Discord Ptb@Discord Ptb OpenAsar@g" a > discord-ptb.desktop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-ptb-openasar
cp -rv * %{buildroot}%{_datadir}/discord-ptb-openasar
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %_datadir/discord-ptb-openasar/discord-ptb.desktop %{buildroot}%{_datadir}/applications/discord-ptb-openasar.desktop
ln -s %_datadir/discord-ptb-openasar/discord.png %{buildroot}%{_datadir}/pixmaps/discord-ptb-openasar.png
install discord-ptb.desktop %{buildroot}%{_datadir}/applications/discord-ptb-openasar.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-ptb-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-ptb-openasar/resources/app.asar
chmod o+w %{buildroot}%{_datadir}/discord-ptb-openasar/resources -R


%files
%{_datadir}/discord-ptb-openasar/
%{_datadir}/applications/discord-ptb-openasar.desktop
%{_datadir}/pixmaps/discord-ptb-openasar.png


%changelog
* Sat Jan 21 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.0.38-1
- Initial package
