%global appid io.github.crocodile.cosmic-ext-applet-workspace-icons

Name:           cosmic-ext-applet-workspace-icons
Version:        1.2.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR CC0-1.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR LGPL-3.0-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
Summary:        COSMIC panel applet showing application icons on workspaces
URL:            https://github.com/crocodile/cosmic-ext-applet-workspace-icons
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Packager:       Olivia <git@olivia.sh>

%description
Workspace Icons is a COSMIC panel applet that adds application icons to
numbered workspaces. It helps you see which apps are open on each workspace and
monitor without opening the workspace overview.

%prep
%autosetup
%{cargo_prep_online}

%build
%{cargo_build}
%{cargo_license_online} > LICENSE.dependencies

%install
%__install -Dm0755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
%__install -Dm0644 resources/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
%__install -Dm0644 resources/%{appid}.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml
%__install -Dm0644 resources/%{appid}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Sun Aug 02 00:04:46 -0500 Olivia <git@olivia.sh> - 1.2.0-1
- Initial package

