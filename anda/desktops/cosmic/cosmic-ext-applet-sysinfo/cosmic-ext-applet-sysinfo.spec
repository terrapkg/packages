%global ver 0.4.0
%global commitdate 20260814
%global commit f66e0c7b133bf4249d23ab7483693cedca46ad19
%global shortcommit %{sub %{commit} 0 7}
%global appid io.github.cosmic_utils.sysinfo-applet

Name:           
Version:        %{ver}^%{commitdate}.git%{shortcommit}
Release:        2%{?dist}
Summary:        Simple system info applet for cosmic

SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (Zlib OR Apache-2.0 OR M) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-sysinfo
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd

Packager:       Olivia <git@olivia.sh>

%description
Simple system info applet for cosmic.

%prep
%autosetup -n %{name}-%{commit}
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
%__install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
%__install -Dm 644 data/%{appid}-symbolic.svg %{buildroot}%{_scalableiconsdir}/%{appid}-symbolic.svg
%__install -Dm 644 data/%{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_scalableiconsdir}/%{appid}-symbolic.svg
%{_appsdir}/%{appid}.desktop

%changelog
* Mon Aug 17 2026 Olivia <git@olivia.sh>
- Initial package
