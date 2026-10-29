%global appid io.github.k33wee.clippy-land

Name:           cosmic-applet-clippy-land
Version:        2.0.0
Release:        1%{?dist}
Summary:        A minimal COSMIC panel applet that keeps a history of the latest copied text and images entries
URL:            https://github.com/k33wee/clippy-land
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  GPL-3.0-or-later
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0-or-later AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm0755 target/rpm/cosmic-applet-clippy-land            %{buildroot}%{_bindir}/cosmic-applet-clippy-land
install -Dm0755 resources/cosmic-applet-clippy-land.sh          %{buildroot}%{_bindir}/cosmic-applet-clippy-land.sh
install -Dm0644 resources/%{appid}.desktop                      %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 resources/%{appid}.metainfo.xml                 %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 resources/icon.svg                              %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/cosmic-applet-clippy-land
%{_bindir}/cosmic-applet-clippy-land.sh
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Thu Oct 15 2026 Owen Zimmerman <owen@fyralabs.com> - 1.1.1-1
- Initial commit
