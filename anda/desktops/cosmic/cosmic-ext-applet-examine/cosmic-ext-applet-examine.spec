%global appid io.github.cosmic_utils.Examine

Name:           cosmic-ext-applet-examine
Version:        2.0.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        %{sourcelicense AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A system information viewer for the COSMIC™ Desktop
URL:            https://github.com/cosmic-utils/examine
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
Requires:       cosmic-osd
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
install -Dm0755 target/rpm/examine							%{buildroot}%{_bindir}/examine
install -Dm0644 res/io.github.cosmic_utils.Examine.desktop				%{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/io.github.cosmic_utils.Examine.metainfo.xml				%{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/scalable/apps/io.github.cosmic_utils.Examine.svg	%{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/examine
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com> - 2.0.0-1
- Initial commit

