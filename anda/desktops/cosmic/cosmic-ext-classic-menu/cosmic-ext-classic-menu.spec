%global appid com.championpeak87.cosmic-ext-classic-menu

Name:           cosmic-ext-classic-menu
Version:        0.0.14
Release:        1%{?dist}
SourceLicense:  GPL-3.0-or-later
License:        GPL-3.0-or-later (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A menu applet for COSMIC Desktop
URL:            https://github.com/championpeak87/cosmic-ext-classic-menu
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  just
Requires:       cosmic-osd
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
just rootdir=%{buildroot} install
%terra_appstream %{S:1}

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}-applet
%{_bindir}/%{name}-settings
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg
%{_datadir}/cosmic/%{appid}/applet-buttons/*
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Jul 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
