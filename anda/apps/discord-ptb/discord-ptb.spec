Name:           discord-ptb
Version:        1.0.190
Release:        2%{?dist}
Summary:        Free Voice and Text Chat for Gamers.
URL:            https://discord.com
Source0:        https://dl-ptb.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
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
%autosetup -n DiscordPTB

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
* Tue May 5 2026 Gilver E. <roachy@fyralabs.com> - 1.0.189-2
- Update build for new bootstrap format

* Thu Nov 17 2022 madonuko <mado@fyralabs.com> - 0.0.35-1
- new version

* Thu Oct 20 2022 madonuko <mado@fyralabs.com> - 0.0.34-1
- new version

* Sun Oct 16 2022 madonuko <mado@fyralabs.com> - 0.0.33
- Initial Package.
