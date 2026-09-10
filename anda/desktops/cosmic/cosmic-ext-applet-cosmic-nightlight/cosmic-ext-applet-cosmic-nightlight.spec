%global appid io.github.cosmic_nightlight

Name:           cosmic-ext-applet-cosmic-nightlight
Version:        0.5.0
Release:        1%{?dist}
SourceLicense:  MPL-2.0
License:	%{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        Night-light / gamma utility for the COSMIC desktop (Pop!_OS), via DRM/KMS + polkit helper
URL:            https://github.com/cosmic-nightlight/cosmic-nightlight
Source0:       	%{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Provides:	cosmic-nightlight
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/cosmic-nightlight	 					%{buildroot}%{_bindir}/cosmic-nightlight
install -Dm644 data/io.github.cosmic_nightlight.desktop					%{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 data/io.github.cosmic_nightlight.settings.desktop			%{buildroot}%{_appsdir}/%{appid}.settings.desktop
install -Dm644 data/io.github.cosmic_nightlight.metainfo.xml				%{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm644 data/icons/hicolor/scalable/apps/io.github.cosmic_nightlight.svg		%{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 data/icons/hicolor/128x128/apps/io.github.cosmic_nightlight.png		%{buildroot}%{_hicolordir}/128x128/apps/%{appid}.png

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-nightlight
%{_appsdir}/%{appid}.desktop
%{_appsdir}/%{appid}.settings.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg
%{_hicolordir}/128x128/apps/%{appid}.png

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com> - 0.5.0-1
- Initial commit
