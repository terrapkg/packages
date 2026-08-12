%global appid io.github.cosmic_utils.camera

Name:           cosmic-ext-camera
Version:        1.2.2
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND NCSA) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND AGPL-3.0 AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND ((MIT OR Apache-2.0) AND ISC) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        Camera application for the COSMIC™ desktop environment
URL:            https://github.com/cosmic-utils/cosmic-ext-camera
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libcamera)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  clang-libs
BuildRequires:  llvm-devel
Requires:       cosmic-osd
Requires:       hicolor-icon-theme
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
install -Dm0755 target/rpm/camera                                   %{buildroot}%{_bindir}/camera
install -Dm0644 resources/%{appid}.desktop                          %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 resources/%{appid}.metainfo.xml                     %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 resources/icons/hicolor/scalable/apps/%{appid}.svg  %{buildroot}%{_scalableiconsdir}/%{appid}.svg
for size in 16x16 24x24 32x32 48x48 64x64 128x128 256x256 512x512 1024x1024; do \
    install -Dm0644 "resources/icons/hicolor/$size/apps/%{appid}.png" "%{buildroot}%{_hicolordir}/$size/apps/%{appid}.png"; \
done

%files
%doc README.md
%license LICENSE.md LICENSE.dependencies
%{_bindir}/camera
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg
%{_hicolordir}/*x*/apps/%{appid}.png

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
