%global ver 0.1.1
%global commitdate 20260509
%global commit cd3b97c256bbfb04b6fee0500677b1ee57b39e1c
%global shortcommit %{sub %{commit} 0 7}
%global appid dev.heppen.ollama

Name:           cosmic-ext-applet-ollama
Version:        %{ver}^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        Ollama applet for COSMIC Desktop

SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-ollama
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  /usr/bin/just
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(openssl)
Requires:       cosmic-osd

Packager:       Olivia <git@olivia.sh>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
just --set target rpm --set rootdir %buildroot install

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_scalableiconsdir}/%{appid}-symbolic.svg
%{_appsdir}/%{appid}.desktop

%changelog
* Wed Sep 2 2026 Olivia <git@olivia.sh>
- Initial package
