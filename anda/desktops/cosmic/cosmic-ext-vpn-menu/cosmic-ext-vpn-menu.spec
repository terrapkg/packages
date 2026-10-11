%global commit 5274a17ffcb75b3a034daf453078b7bd64dcee1e
%global commit_date 20260805
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global appid com.github.takilazy.CosmicExtVpnMenu

Name:           cosmic-ext-vpn-menu
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
SourceLicense:  MPL-2.0
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A COSMIC™ panel applet for managing VPN connections via NetworkManager
URL:            https://github.com/takilazy/cosmic-ext-vpn-menu
Source0:        %{url}/archive/%{commit}/server-%{commit}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name}          %{buildroot}%{_bindir}/%{name}
install -Dm 644 resources/app.desktop       %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm 644 resources/app.metainfo.xml  %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm 644 resources/icon.svg          %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Fri Oct 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
