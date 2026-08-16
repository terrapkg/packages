%global commit 28fdcccfe8fa25122a33bcb6d49c9df3f05f3d8f
%global commit_date 20251014
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global appid com.github.cosmic_ext.PackageUpdater

Name:           cosmic-applet-package-updater
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Package update notifier applet for the COSMIC desktop
URL:            https://github.com/Ebbo/cosmic-applet-package-updater
Source0:        %{url}/archive/%{commit}/cosmic-applet-package-updater-%{commit}.tar.gz
SourceLicense:  GPL-3.0-or-later
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND GPL-3.0-or-later AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND BSL-1.0 AND ISC AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
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
install -Dm0755 target/rpm/cosmic-ext-applet-package-updater    %{buildroot}%{_bindir}/cosmic-ext-applet-package-updater
install -Dm0644 res/%{appid}.desktop                            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml                       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/256x256/apps/%{appid}.svg     %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/cosmic-ext-applet-package-updater
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Sun Aug 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
