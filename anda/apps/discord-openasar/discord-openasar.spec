%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           discord-openasar
Version:        0.0.61
Release:        1%?dist
Summary:        A snappier Discord rewrite with features like further customization and theming
License:        MIT AND https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl.discordapp.net/apps/linux/%{version}/discord-%{version}.tar.gz
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
%autosetup -n Discord

%build
sed "s@discord@discord-openasar@g" discord.desktop > a
sed "s@Discord@Discord OpenAsar@g" a > discord.desktop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/discord-openasar
cp -rv * %{buildroot}%{_datadir}/discord-openasar
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %_datadir/discord-openasar/discord.desktop %{buildroot}%{_datadir}/applications/discord-openasar.desktop
ln -s %_datadir/discord-openasar/discord.png %{buildroot}%{_datadir}/pixmaps/discord-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-openasar/resources/app.asar
chmod o+w %{buildroot}%{_datadir}/discord-openasar/resources -R
ln -s %_datadir/discord-openasar/Discord %buildroot%_bindir/discord-openasar


%files
%_bindir/discord-openasar
%{_datadir}/discord-openasar/
%{_datadir}/applications/discord-openasar.desktop
%{_datadir}/pixmaps/discord-openasar.png


%changelog
* Sat Jan 21 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.0.38-1
- Initial package
