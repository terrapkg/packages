%define debug_package %{nil}
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           discord-canary
Version:        0.0.428
Release:        1%?dist
Summary:        Free Voice and Text Chat for Gamers
URL:            discord.com
Source0:        https://dl-canary.discordapp.net/apps/linux/%{version}/discord-canary-%{version}.tar.gz
License:        https://discord.com/terms
Requires:       glibc GConf2 nspr >= 4.13 nss >= 3.27 libX11 >= 1.6 libXtst >= 1.2
Group:          Applications/Internet
ExclusiveArch:  x86_64
%description
Imagine a place where you can belong to a school club, a gaming group, or a
worldwide art community. Where just you and a handful of friends can spend time
together. A place that makes it easy to talk every day and hang out more often.

%prep
%autosetup -n DiscordCanary

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-canary
cp -rv * %{buildroot}%{_datadir}/discord-canary
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %_datadir/discord-canary/discord-canary.desktop %{buildroot}%{_datadir}/applications/
ln -s %_datadir/discord-canary/discord.png %{buildroot}%{_datadir}/pixmaps/discord-canary.png

%files
%{_datadir}/discord-canary/
%{_datadir}/applications/discord-canary.desktop
%{_datadir}/pixmaps/discord-canary.png

%changelog
* Thu Dec 01 2022 root - 0.0.144-1
- new version

* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 0.0.143-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Thu Oct 27 2022 root - 0.0.141-1
- new version

* Wed Oct 19 2022 windowsboy111 <wboy111@outlook.com> - 0.0.140-1
- new version

* Sun Oct 16 2022 windowsboy111 <wboy111@outlook.com> - 0.0.139
- Repackaged for Terra

* Tue Feb 22 2022 Ultramarine Release Tracking Service - 0.0.133-2
- Mass rebuild for release um36

* Sat Nov 20 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
