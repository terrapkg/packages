%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           discord-ptb
Version:        0.0.86
Release:        1%?dist
Summary:        Free Voice and Text Chat for Gamers.
URL:            https://discord.com
Source0:        https://dl-ptb.discordapp.net/apps/linux/%{version}/discord-ptb-%{version}.tar.gz
License:        https://discord.com/terms
Requires:       glibc GConf2
Requires:       nspr >= 4.13
Requires:       nss >= 3.27
Requires:       libX11 >= 1.6
Requires:       libXtst >= 1.2
Group:          Applications/Internet
ExclusiveArch:  x86_64
%description
Imagine a place where you can belong to a school club, a gaming group, or a
worldwide art community. Where just you and a handful of friends can spend time
together. A place that makes it easy to talk every day and hang out more often.

%prep
%autosetup -n DiscordPTB

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-ptb
cp -rv * %{buildroot}%{_datadir}/discord-ptb
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %_datadir/discord-ptb/discord-ptb.desktop %{buildroot}%{_datadir}/applications/
ln -s %_datadir/discord-ptb/discord.png %{buildroot}%{_datadir}/pixmaps/discord-ptb.png

%files
%{_datadir}/discord-ptb/
%{_datadir}/applications/discord-ptb.desktop
%{_datadir}/pixmaps/discord-ptb.png

%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 0.0.35-1
- new version

* Thu Oct 20 2022 windowsboy111 <wboy111@outlook.com> - 0.0.34-1
- new version

* Sun Oct 16 2022 windowsboy111 <wboy111@outlook.com> - 0.0.33
- Initial Package.
