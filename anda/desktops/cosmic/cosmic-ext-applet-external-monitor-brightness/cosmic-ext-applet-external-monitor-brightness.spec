%global appid io.github.cosmic_utils.cosmic-ext-applet-external-monitor-brightness

Name:           cosmic-ext-applet-external-monitor-brightness
Version:        0.0.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND BSL-1.0 AND ISC AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        Applet to control the brightness of external monitors
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-external-monitor-brightness
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
# Not in release
Source1:        %{url}/blob/master/res/icons/display-symbolic.svg
Source2:        %{url}/blob/master/res/metainfo.xml
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
cp %{S:1} icon.svg
cp %{S:2} metainfo.xml

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/cosmic-ext-applet-external-monitor-brightness    %{buildroot}%{_bindir}/cosmic-ext-applet-external-monitor-brightness
install -Dm0644 res/desktop_entry.desktop                                   %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 icon.svg                                                    %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm0644 metainfo.xml                                                %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/cosmic-ext-applet-external-monitor-brightness
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Aug 16 2026 Owen Zimmerman <owen@fyralabs.com> - 0.0.1-1
- Initial commit
