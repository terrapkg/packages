%global appid io.github.hasmolam.cosmic-ext-applet-calendar

Name:           cosmic-ext-applet-calendar
Version:        1.1.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        %{sourcelicense} AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0 AND Unlicense AND Zlib AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR LGPL-3.0-or-later) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
Summary:        COSMIC desktop calendar applet with Google Calendar, CalDAV sync, and agenda view
URL:            https://github.com/Hasmolam/cosmic-ext-applet-calendar
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
BuildRequires:  cargo-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  terra-appstream-helper
Requires:       cosmic-osd
Recommends:     evolution-data-server
Packager:       Leo Douglas <douglarek@gmail.com>

%description
A standalone calendar and agenda applet for the COSMIC desktop. It fetches
events from Evolution Data Server (Google Calendar, Nextcloud, CalDAV) and
local .ics files, marks days with events on the monthly calendar grid, and
shows a chronological agenda for the selected day.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 data/%{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 data/icons/scalable/apps/%{appid}-symbolic.svg %{buildroot}%{_scalableiconsdir}/%{appid}-symbolic.svg
%terra_appstream %{S:1}

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}-symbolic.svg

%changelog
* Sat Sep 26 2026 Leo Douglas <douglarek@gmail.com> - 1.1.1-1
- Initial package
