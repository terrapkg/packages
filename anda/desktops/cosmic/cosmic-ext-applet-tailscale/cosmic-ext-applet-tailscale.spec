%global appid com.bhh32.gui-scale-applet

Name:           cosmic-ext-applet-tailscale
Version:        3.10.2
Release:        1%{?dist}
SourceLicense:  BSD-3-Clause
License:        %{sourcelicense}
Summary:        COSMIC applet for Tailscale
URL:            https://github.com/cosmic-utils/gui-scale-applet
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
BuildRequires:  systemd-devel
Requires:       cosmic-osd
Requires:       tailscale
Provides:       gui-scale-applet
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/gui-scale-applet                             %{buildroot}%{_bindir}/gui-scale-applet
install -Dm0644 data/com.bhh32.gui-scale-applet.desktop                 %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 data/com.bhh32.gui-scale-applet.metainfo.xml            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 data/icons/scalable/apps/com.bhh32.gui-scale-applet.png %{buildroot}%{_hicolordir}/256x256/apps/%{appid}.png

%files
%doc README.md docs/*
%license LICENSE
%{_bindir}/gui-scale-applet
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/256x256/apps/%{appid}.png

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com> - 3.10.2-1
- Initial commit
