%global appid dev.cappsy.CosmicExtAppletLogoMenu

Name:           cosmic-ext-classic-menu
Version:        0.8.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-or-later
License:        GPL-3.0-or-later AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        Logo Menu applet for COSMIC
URL:            https://github.com/cosmic-utils/cosmic-ext-applet-logomenu
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  libxcb-devel
BuildRequires:  just
Requires:       cosmic-osd
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
mkdir -p %{buildroot}%{_metainfodir}
install -Dm0755 target/rpm/cosmic-ext-applet-logomenu           %{buildroot}%{_bindir}/cosmic-ext-applet-logomenu
install -Dm0755 target/rpm/cosmic-ext-logomenu-settings         %{buildroot}%{_bindir}/cosmic-ext-logomenu-settings
install -Dm0644 res/%{appid}.desktop                            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.Settings.desktop                   %{buildroot}%{_appsdir}/%{appid}.Settings.desktop
install -Dm0644 res/%{appid}.metainfo.xml                       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/scalable/apps/%{appid}.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -m0644 -t %{buildroot}%{_scalableiconsdir} res/icons/*.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-applet-logomenu
%{_bindir}/cosmic-ext-logomenu-settings
%{_appsdir}/%{appid}.desktop
%{_appsdir}/%{appid}.Settings.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg
%{_scalableiconsdir}/*.svg

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
