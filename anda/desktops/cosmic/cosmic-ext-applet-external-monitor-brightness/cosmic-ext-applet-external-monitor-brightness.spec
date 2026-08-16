%global appid io.github.cosmic_utils.cosmic-ext-applet-external-monitor-brightness

Name:           cosmic-ext-applet-external-monitor-brightness
Version:        0.0.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only
Summary:        Applet to control the brightness of external monitors
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-external-monitor-brightness
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
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
install -Dm0755 target/rpm/cosmic-ext-applet-external-monitor-brightness    %{buildroot}%{_bindir}/cosmic-ext-applet-external-monitor-brightness
install -Dm0644 res/desktop_entry.desktop                                   %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/icons/display-symbolic.svg                              %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm0644 res/metainfo.xml                                            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/cosmic-ext-applet-external-monitor-brightness
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Aug 16 2026 Owen Zimmerman <owen@fyralabs.com> - 0.0.1-1
- Initial commit
