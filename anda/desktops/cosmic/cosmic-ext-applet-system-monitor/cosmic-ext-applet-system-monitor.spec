%global appid dev.DBrox.CosmicSystemMonitor

Name:           cosmic-ext-applet-system-monitor
Version:        0.2.10
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        %{sourcelicense}
Summary:        A highly configurable resource monitor applet for the COSMIC DE
URL:            https://github.com/D-Brox/cosmic-ext-applet-system-monitor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
BuildRequires:  systemd-devel
Requires:       cosmic-osd
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
install -Dm0755 target/rpm/cosmic-ext-applet-system-monitor     %{buildroot}%{_bindir}/cosmic-ext-applet-system-monitor
install -Dm0644 res/dev.DBrox.CosmicSystemMonitor.desktop       %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/dev.DBrox.CosmicSystemMonitor.metainfo.xml  %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/dev.DBrox.CosmicSystemMonitor.svg           %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md docs/*
%license LICENSE
%{_bindir}/cosmic-ext-applet-system-monitor
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com> - 0.2.10-1
- Initial commit
