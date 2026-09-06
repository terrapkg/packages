%global appid io.github.franz_net.CosmicExtAppletFlux

Name:           cosmic-ext-flux
Version:        3.1.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

Summary:        Animated desktop wallpapers for COSMIC — play any video or GIF as your background
URL:            https://www.franz-e.net/cosmic-ext-flux/
Source0:        https://github.com/franz-net/cosmic-ext-flux/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
BuildRequires:  cargo-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad
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
install -Dm755 target/rpm/cosmic-ext-flux-daemon %{buildroot}%{_bindir}/cosmic-ext-flux-daemon
install -Dm755 target/rpm/cosmic-ext-applet-flux %{buildroot}%{_bindir}/cosmic-ext-applet-flux
install -Dm644 applet/resources/app.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 applet/resources/icon.svg %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 applet/resources/icon-stopped.svg %{buildroot}%{_scalableiconsdir}/%{appid}-stopped.svg
install -Dm644 data/cosmic-ext-flux-daemon.service %{buildroot}%{_userunitdir}/cosmic-ext-flux-daemon.service

%terra_appstream -o %{S:1}

%post
%systemd_user_post cosmic-ext-flux-daemon.service

%preun
%systemd_user_preun cosmic-ext-flux-daemon.service

%postun
%systemd_user_postun_with_restart cosmic-ext-flux-daemon.service

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-flux-daemon
%{_bindir}/cosmic-ext-applet-flux
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_scalableiconsdir}/%{appid}-stopped.svg
%{_userunitdir}/cosmic-ext-flux-daemon.service
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Jul 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
