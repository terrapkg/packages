%global appid dev.edfloreshz.CosmicTweaks

Name:           cosmic-ext-tweaks
Version:        0.2.5
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A tweaking tool for the COSMIC desktop
URL:            https://github.com/cosmic-utils/tweaks
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       hicolor-icon-theme
Provides:       cosmic-tweaks
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
# aws-lc-sys runs compiler feature probes that intentionally use non-PIE objects for some reason
export LDFLAGS="%{build_ldflags} -fPIE"
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/cosmic-ext-tweaks                %{buildroot}%{_bindir}/cosmic-ext-tweaks
install -Dm0644 res/app.desktop                             %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/icons/hicolor/scalable/apps/icon.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm0644 res/metainfo.xml                            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-tweaks
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
