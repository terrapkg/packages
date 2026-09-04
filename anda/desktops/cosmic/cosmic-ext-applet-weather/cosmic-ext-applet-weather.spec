%global commit_date 20260903
%global commit 52a9e3a4ac6de8d8476a3b609dcea32feae490a6
%global shortcommit %{sub %{commit} 0 7}
%global appid io.github.cosmic_utils.weather-applet

Name:           cosmic-ext-applet-weather
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Weather applet for the COSMIC desktop

SourceLicense:  GPL-3.0-only
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND Unlicense
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-weather
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd

Packager:       ammix <maxim@ammix.dev>

%description
An applet that displays weather information in the COSMIC desktop panel. It
supports automatic location detection, manually configured coordinates, and
Celsius or Fahrenheit temperature units.

%prep
%autosetup -n %{name}-%{commit}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
%desktop_file_install -k Categories -v Utility; data/%{appid}.desktop
install -Dm0644 data/%{appid}.metainfo.xml %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 data/%{appid}-symbolic.svg %{buildroot}%{_scalableiconsdir}/%{appid}-symbolic.svg

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}-symbolic.svg

%changelog
* Thu Sep 03 2026 ammix <maxim@ammix.dev>
- Initial package
