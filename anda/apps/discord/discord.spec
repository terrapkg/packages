%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:			discord
Version:		0.0.62
Release:		1%?dist
Summary:		Free Voice and Text Chat for Gamers
URL:			https://discord.com
Source0:		https://dl.discordapp.net/apps/linux/%{version}/discord-%{version}.tar.gz
License:		https://discord.com/terms
Requires:		glibc GConf2
Requires:		nspr >= 4.13
Requires:		nss >= 3.27
Requires:		libX11 >= 1.6
Requires:		libXtst >= 1.2
Group:			Applications/Internet
ExclusiveArch:	x86_64
%description
All-in-one voice and text chat for gamers that's free, secure, and works on
both your desktop and phone.

%prep
%autosetup -n Discord

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/discord
cp -rv * %{buildroot}%{_datadir}/discord
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %_datadir/discord/discord.desktop %{buildroot}%{_datadir}/applications/discord.desktop
ln -s %_datadir/discord/discord.png %{buildroot}%{_datadir}/pixmaps/discord.png
ln -s %_datadir/discord/Discord %buildroot%_bindir/discord

%files
%_bindir/discord
%{_datadir}/discord/
%{_datadir}/applications/discord.desktop
%{_datadir}/pixmaps/discord.png

%changelog
* Thu Jan 19 2023 windowsboy111 <wboy111@outlook.com> - 0.0.143-1
- Initial package
