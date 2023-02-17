%define debug_package %{nil}

Name:			discord
Version:		0.0.25
Release:		1%{?dist}
Summary:		Free Voice and Text Chat for Gamers.
URL:			discord.com
Source0:		https://dl.discordapp.net/apps/linux/%{version}/discord-%{version}.tar.gz
License:		https://discord.com/terms
Requires:		libatomic glibc alsa-lib GConf2 libnotify libstdc++ libappindicator libcxx libXScrnSaver
Requires:		nspr >= 4.13
Requires:		nss >= 3.27
Requires:		libX11 >= 1.6
Requires:		libXtst >= 1.2
Group:			Applications/Internet
ExclusiveArch:	x86_64
%description
Imagine a place where you can belong to a school club, a gaming group,
or a worldwide art community. Where just you and a handful of friends
can spend time together. A place that makes it easy to talk every day
and hang out more often.

%prep
%autosetup -n Discord

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord
cp -rv * %{buildroot}%{_datadir}/discord
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord.desktop %{buildroot}%{_datadir}/applications/discord.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord.png

%files
%{_datadir}/discord/
%{_datadir}/applications/discord.desktop
%{_datadir}/pixmaps/discord.png

%changelog
* Thu Jan 19 2023 windowsboy111 <wboy111@outlook.com> - 0.0.143-1
- Initial package
