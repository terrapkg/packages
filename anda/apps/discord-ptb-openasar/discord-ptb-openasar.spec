%define debug_package %{nil}

Name:           discord-ptb-openasar
Version:        0.0.41
Release:        1%{?dist}
Summary:        OpenAsar is a rewrite of part of Discord's desktop code, making it snappier and include more features like further customization and theming
License:        MIT and https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl-ptb.discordapp.net/apps/linux/%{version}/discord-ptb-%{version}.tar.gz
Source1:        %{url}/releases/download/nightly/app.asar
Group:          Applications/Internet
Requires:       libatomic, glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27, libstdc++, libX11 >= 1.6, libXtst >= 1.2, libappindicator, libcxx, libXScrnSaver
ExclusiveArch:  x86_64

%description
%{summary}.

%prep
%autosetup -n DiscordPTB

%build
sed "s@discord-ptb@discord-ptb-openasar@g" discord-ptb.desktop > a
sed "s@Discord Ptb@Discord Ptb OpenAsar@g" a > discord-ptb.desktop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-ptb-openasar
cp -rv * %{buildroot}%{_datadir}/discord-ptb-openasar
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord-ptb.desktop %{buildroot}%{_datadir}/applications/discord-ptb-openasar.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-ptb-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-ptb-openasar/resources/app.asar
chmod o+w %{buildroot}%{_datadir}/discord-ptb-openasar/resources -R


%files
%{_datadir}/discord-ptb-openasar/
%{_datadir}/applications/discord-ptb-openasar.desktop
%{_datadir}/pixmaps/discord-ptb-openasar.png


%changelog
* Sat Jan 21 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.0.38-1
- Initial package
