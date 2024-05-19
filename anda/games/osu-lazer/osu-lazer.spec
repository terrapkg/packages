%define osuresver 2024.517.0
%global debug_package %{nil}
%define __strip /bin/true

Name:			osu-lazer
Version:		2024.519.0
Release:		1%?dist
Summary:		The future of osu! and the beginning of an open era! Commonly known by the codename osu!lazer. Pew pew.
ExclusiveArch:	x86_64
URL:			https://osu.ppy.sh/
License:		MIT AND CC-BY-NC-4.0
Requires:		osu-mime fuse
Source0:		https://github.com/ppy/osu/releases/download/%{version}/osu.AppImage
Source1:		https://raw.githubusercontent.com/ppy/osu/%{version}/assets/lazer.png
Source2:		https://raw.githubusercontent.com/ppy/osu-resources/%{osuresver}/LICENCE.md
Source3:		osu-lazer.desktop
Source4:		osu-lazer-uri-handler.desktop

%description
%{summary}

%prep
cat <<EOF > osu-lazer
#!/bin/sh
env OSU_EXTERNAL_UPDATE_PROVIDER=1 /opt/osu-lazer/osu.AppImage "$@"
EOF


%build

%install
install -Dm755 %{SOURCE0} %{buildroot}/opt/osu-lazer/osu.AppImage
install -Dm755 -t %{buildroot}/usr/bin osu-lazer

# Install pixmap, desktop and license file
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}/
install -Dm644 %{SOURCE1} %{buildroot}/usr/share/pixmaps/osu-lazer.png
install -Dm644 %{SOURCE2} %{buildroot}/%{_datadir}/licenses/%{name}/LICENSE.md
install -Dm644 -t %{buildroot}/usr/share/applications %{SOURCE3}
install -Dm644 -t %{buildroot}/usr/share/applications %{SOURCE4}

%files
%license LICENSE.md
/usr/share/applications/osu-lazer*.desktop
/usr/bin/osu-lazer
/opt/osu-lazer/osu.AppImage
/usr/share/pixmaps/osu-lazer.png


%changelog
* Mon Feb 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2023.207.0-1
- Initial package
