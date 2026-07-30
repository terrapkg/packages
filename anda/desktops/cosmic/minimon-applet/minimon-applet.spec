%global appid io.github.cosmic_utils.minimon-applet

Name:           minimon-applet
Version:        1.1.2
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (GPL-3.0+ OR BSD-3-Clause) AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A COSMIC applet for displaying CPU/Memory/Network/Disk/GPU usage in the Panel or Dock
URL:            https://github.com/cosmic-utils/minimon-applet
Source0:        %{url}/archive/refs/tags/v1.1.2.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
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
install -Dm0755 target/rpm/cosmic-ext-applet-minimon    %{buildroot}%{_bindir}/cosmic-ext-applet-minimon
install -Dm0644 res/%{appid}.desktop                    %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml               %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
for svg in res/icons/apps/*.svg; do \
    install -D "$svg" "%{buildroot}%{_scalableiconsdir}/$(basename $svg)"; \
done

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-applet-minimon
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/*.svg

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
