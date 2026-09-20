%global appid com.bhh32.gui-scale-applet

Name:           cosmic-ext-applet-tailscale
Version:        3.10.2
Release:        1%{?dist}
SourceLicense:  BSD-3-Clause
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        COSMIC applet for Tailscale
URL:            https://github.com/cosmic-utils/gui-scale-applet
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
BuildRequires:  systemd-devel
BuildRequires:  desktop-file-utils
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
%desktop_file_install data/com.bhh32.gui-scale-applet.desktop
install -Dm0644 data/com.bhh32.gui-scale-applet.metainfo.xml            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 data/icons/scalable/apps/com.bhh32.gui-scale-applet.png %{buildroot}%{_hicolordir}/256x256/apps/%{appid}.png

%terra_appstream

%files
%doc README.md
%license LICENSE
%{_bindir}/gui-scale-applet
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/256x256/apps/%{appid}.png

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com> - 3.10.2-1
- Initial commit
