Name:			osu-lazer
Version:		2023.207.0
Release:		1%{?dist}
Summary:		The future of osu! and the beginning of an open era! Commonly known by the codename osu!lazer. Pew pew.
BuildArch:		x86_64
URL:			https://osu.ppy.sh/
License:		MIT, CC-BY-NC-4.0
Requires:		zlib osu-mime fuse
Source0:		https://github.com/ppy/osu/releases/download/%{version}/osu.AppImage
Source1:		https://raw.githubusercontent.com/ppy/osu/%{version}/assets/lazer.png
Source2:		https://raw.githubusercontent.com/ppy/osu-resources/%{version}/LICENCE.md
Source3:		osu-lazer.desktop
Source4:		osu-lazer-uri-handler.desktop

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
install -Dm644 %{SOURCE1} %{buildroot}/usr/share/pixmaps/osu-lazer.png
install -Dm644 -t %{buildroot}/usr/share/licenses/%{name} %{SOURCE2}
install -Dm644 -t %{buildroot}/usr/share/applications %{SOURCE3}
install -Dm644 -t %{buildroot}/usr/share/applications %{SOURCE4}

%files
%license %{SOURCE2}
/usr/share/applications/osu-lazer*.desktop
/usr/bin/osu-lazer
/opt/osu-lazer/osu.AppImage


%changelog
* Mon Feb 13 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package