Name:			discord
Version:		1.0.136
Release:		2%{?dist}
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

%electronmeta -D

%description
All-in-one voice and text chat for gamers that's free, secure, and works on
both your desktop and phone.

%prep
%autosetup -n Discord

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -Dpm755 ./* -t %{buildroot}%{_libdir}/discord
mkdir -p %{buildroot}%{_appsdir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_libdir}/discord/discord.desktop -t %{buildroot}%{_appsdir}
mv %{buildroot}%{_libdir}/discord/discord.png -t %{buildroot}%{_datadir}/pixmaps
ln -s %{_libdir}/discord/discord %{buildroot}%{_bindir}/discord

%files
%{_bindir}/discord
%{_libdir}/discord/
%{_appsdir}/discord.desktop
%{_datadir}/pixmaps/discord.png

%changelog
* Mon May 4 2026 Gilver E. <roachy@fyralabs.com> - 1.0.136-2
- Updated /usr/bin symlink
* Thu Jan 19 2023 madonuko <mado@fyralabs.com> - 0.0.143-1
- Initial package
