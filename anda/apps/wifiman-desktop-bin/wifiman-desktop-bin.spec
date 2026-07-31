%define debug_package %{nil}
%global __strip /bin/true

%global appname wifiman-desktop
%global appid   com.wifiman.WiFimanDesktop

Name:           wifiman-desktop-bin
Version:        1.2.8
Release:        1%{?dist}
Summary:        Ubiquiti WiFiman desktop client for network scanning and UniFi Teleport VPN

License:        Proprietary
URL:            https://wifiman.com
Source0:        https://desktop.wifiman.com/%{appname}-%{version}-amd64.deb
Source1:        %{appid}.metainfo.xml
Source2:        %{appname}.desktop

ExclusiveArch:  x86_64

BuildRequires:  anda-srpm-macros
BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar
BuildRequires:  terra-appstream-helper

Recommends:     libayatana-appindicator-gtk3
Requires:       iw
Requires:       net-tools
Requires:       xdg-utils
Provides:       wifiman-desktop = %{version}-%{release}

Packager:       Caio Bruno <cbrunofb@gmail.com>

%description
WiFiman Desktop is Ubiquiti's desktop client for analyzing Wi-Fi and wired
networks: it scans for nearby devices, runs speed tests, and connects to a UniFi
network over the Teleport VPN. The GUI (a Tauri/WebKitGTK app) talks to a root
system daemon that bundles its own WireGuard userspace tools for Teleport.

This package repackages the official upstream .deb; no source is published.

%prep
%autosetup -Tc
ar x %{SOURCE0}
tar xf data.tar.gz

%build

%install
install -Dpm0755 usr/bin/%{appname} %{buildroot}%{_bindir}/%{appname}

# Under /usr/lib, not /usr/lib64: the unit's ExecStart hardcodes this path.
install -d %{buildroot}%{_prefix}/lib/%{appname}
cp -a usr/lib/%{appname}/. %{buildroot}%{_prefix}/lib/%{appname}/

install -Dpm0644 usr/lib/%{appname}/%{appname}.service \
                 %{buildroot}%{_unitdir}/%{appname}.service
rm -f %{buildroot}%{_prefix}/lib/%{appname}/%{appname}.service

install -Dpm0644 %{SOURCE2} %{buildroot}%{_appsdir}/%{appname}.desktop
for s in 32x32 128x128; do
    install -Dpm0644 usr/share/icons/hicolor/$s/apps/%{appname}.png \
                     %{buildroot}%{_hicolordir}/$s/apps/%{appname}.png
done
install -Dpm0644 usr/share/icons/hicolor/256x256@2/apps/%{appname}.png \
                 %{buildroot}%{_hicolordir}/256x256@2/apps/%{appname}.png

%terra_appstream -o %{SOURCE1}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appname}.desktop

%post
%systemd_post %{appname}.service

%preun
%systemd_preun %{appname}.service

%postun
%systemd_postun_with_restart %{appname}.service

%files
%{_bindir}/%{appname}
%{_prefix}/lib/%{appname}/
%{_unitdir}/%{appname}.service
%{_appsdir}/%{appname}.desktop
%{_hicolordir}/32x32/apps/%{appname}.png
%{_hicolordir}/128x128/apps/%{appname}.png
%{_hicolordir}/256x256@2/apps/%{appname}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Fri Jul 31 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
