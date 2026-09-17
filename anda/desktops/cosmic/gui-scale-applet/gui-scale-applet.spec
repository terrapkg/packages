%global appid com.bhh32.gui-scale-applet

Name:           gui-scale-applet
Version:        3.10.2
Release:        1%{?dist}
SourceLicense:  BSD-3-Clause
License:        GPL-3.0-only
Summary:        COSMIC applet for Tailscale
URL:            https://github.com/cosmic-utils/gui-scale-applet
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/%{name}                                          %{buildroot}%{_bindir}/%{name}
install -Dm0644 data/com.bhh32.gui-scale-applet.desktop                     %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 data/com.bhh32.gui-scale-applet.metainfo.xml                %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 data/icons/scalable/apps/com.bhh32.gui-scale-applet.png     %{buildroot}%{_hicolordir}/256x256/apps/%{appid}.png

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/256x256/apps/%{appid}.png

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
