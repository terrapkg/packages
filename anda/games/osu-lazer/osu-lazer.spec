%define osuresver 2026.108.0
%global debug_package %{nil}
%define __strip /bin/true

Name:			osu-lazer
Version:		2026.119.0
Release:		2%?dist
Summary:		The future of osu! and the beginning of an open era! Commonly known by the codename osu!lazer. Pew pew.
ExclusiveArch:	x86_64
URL:			https://osu.ppy.sh/
License:		MIT AND CC-BY-NC-4.0
BuildRequires:  desktop-file-utils
Requires:		osu-mime fuse
Source0:		https://github.com/ppy/osu/releases/download/%{version}-lazer/osu.AppImage
Source1:		https://raw.githubusercontent.com/ppy/osu/%{version}-lazer/assets/lazer.png
Source2:		https://raw.githubusercontent.com/ppy/osu-resources/%{osuresver}/LICENCE.md
Source3:		osu-lazer.desktop
Source4:		osu-lazer-uri-handler.desktop

%description
%{summary}

%prep
cat <<'EOF' > osu-lazer
#!/bin/sh
env OSU_EXTERNAL_UPDATE_PROVIDER=1 /opt/osu-lazer/osu.AppImage "$@"
EOF


%build

%install
install -Dm755 %{SOURCE0} %{buildroot}/opt/osu-lazer/osu.AppImage
install -Dm755 -t %{buildroot}%{_bindir} osu-lazer

# Install pixmap, desktop and license file
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}/
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/osu-lazer.png
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.md
install -Dm644 %{SOURCE3} %{buildroot}%{_appsdir}/osu-lazer.desktop
install -Dm644 %{SOURCE4} %{buildroot}%{_appsdir}/osu-lazer-uri-handler.desktop

%check
desktop-file-validate %{buildroot}%{_appsdir}/osu-lazer.desktop
desktop-file-validate %{buildroot}%{_appsdir}/osu-lazer-uri-handler.desktop

%files
%license LICENSE.md
%{_appsdir}/osu-lazer*.desktop
%{_bindir}/osu-lazer
/opt/osu-lazer/osu.AppImage
%{_datadir}/pixmaps/osu-lazer.png

%changelog
* Wed Dec 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Use macros, add %check, clean up %install
* Mon Feb 13 2023 madonuko <mado@fyralabs.com> - 2023.207.0-1
- Initial package
