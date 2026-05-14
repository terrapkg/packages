Name:           discord-canary
Version:        1.0.1081
Release:        1%{?dist}
Summary:        Free Voice and Text Chat for Gamers
URL:            discord.com
Source0:        https://dl-canary.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
Source1:        https://discord.com/terms#/terms.html
License:        Proprietary
Requires:       zenity
Group:          Applications/Internet
ExclusiveArch:  x86_64

%electronmeta -D

%description
All-in-one voice and text chat for gamers that's free, secure, and works on
both your desktop and phone.

%prep
%autosetup -n DiscordCanary

%build

%install
install -Dpm755 updater_bootstrap -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name} -t %{buildroot}%{_bindir}
install -Dpm644 discord.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%desktop_file_install %{name}.desktop
cp %{SOURCE1} -t .

%files
%license terms.html
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue May 5 2026 Gilver E. <roachy@fyralabs.com> - 1.0.1025-2
- Update build for new bootstrap format

* Thu Dec 01 2022 root - 0.0.144-1
- new version

* Thu Nov 17 2022 madonuko <mado@fyralabs.com> - 0.0.143-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Fri Oct 28 2022 root - 0.0.142-1
- new version

* Thu Oct 27 2022 root - 0.0.141-1
- new version

* Wed Oct 19 2022 madonuko <mado@fyralabs.com> - 0.0.140-1
- new version

* Sun Oct 16 2022 madonuko <mado@fyralabs.com> - 0.0.139
- Repackaged for Terra

* Tue Feb 22 2022 Ultramarine Release Tracking Service - 0.0.133-2
- Mass rebuild for release um36

* Sat Nov 20 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
