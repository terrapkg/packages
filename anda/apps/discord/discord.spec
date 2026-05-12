Name:           discord
Version:        1.0.138
Release:        2%{?dist}
Summary:        Free Voice and Text Chat for Gamers
URL:            https://discord.com
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
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
%autosetup -n Discord

%build

%install
install -Dpm755 updater_bootstrap -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name} -t %{buildroot}%{_bindir}
install -Dpm644 %{name}.png -t %{buildroot}%{_datadir}/pixmaps
%desktop_file_install %{name}.desktop
cp %{SOURCE1} -t .

%files
%license terms.html
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue May 5 2026 Gilver E. <roachy@fyralabs.com> - 1.0.136-4
- Remove unused files from package
* Mon May 4 2026 Gilver E. <roachy@fyralabs.com> - 1.0.136-2
- Updated /usr/bin symlink
* Thu Jan 19 2023 madonuko <mado@fyralabs.com> - 0.0.143-1
- Initial package
