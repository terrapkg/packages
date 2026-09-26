%global appid com.system76.CosmicViewer
%undefine __brp_mangle_shebangs

Name:           cosmic-viewer
Version:        1.9.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND NCSA) AND Unlicense AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND ((MIT OR Apache-2.0) AND IJG) AND (BSD-3-Clause OR MIT) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        COSMIC Image Viewer
URL:            https://github.com/pop-os/cosmic-viewer
Source0:        %{url}/archive/refs/tags/epoch-%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake
BuildRequires:  gcc-c++
%ifarch x86_64
BuildRequires:  nasm
%endif
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
install -Dm0755 target/rpm/cosmic-viewer                        %{buildroot}%{_bindir}/cosmic-viewer
install -Dm0644 res/%{appid}.desktop                            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml                       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/128x128/apps/%{appid}.svg     %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%terra_appstream

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-viewer
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Thu Sep 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
