Name:           discord-ptb
Version:        0.0.34
Release:        %autorelease
Summary:        Free Voice and Text Chat for Gamers.
URL:            discord.com
Source0:        https://dl-ptb.discordapp.net/apps/linux/%{version}/discord-ptb-%{version}.tar.gz
License:        https://discord.com/terms
Requires:       libatomic, glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27, libstdc++, libX11 >= 1.6, libXtst >= 1.2, libappindicator, libcxx, libXScrnSaver
Group:          Applications/Internet
ExclusiveArch:  x86_64
%description
Imagine a place where you can belong to a school club, a gaming group, or a worldwide art community. Where just you and a handful of friends can spend time together. A place that makes it easy to talk every day and hang out more often.

%prep
%autosetup -n DiscordPTB


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-ptb
cp -rv * %{buildroot}%{_datadir}/discord-ptb
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord-ptb.desktop %{buildroot}%{_datadir}/applications/discord-ptb.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-ptb.png

%files
%{_datadir}/discord-ptb/
%{_datadir}/applications/discord-ptb.desktop
%{_datadir}/pixmaps/discord-ptb.png

%changelog
* Sun Oct 16 2022 windowsboy111 <wboy111@outlook.com> - 0.0.33
- Initial Package.
