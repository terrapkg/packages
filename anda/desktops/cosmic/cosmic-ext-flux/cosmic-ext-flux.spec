%global appid io.github.franz_net.CosmicExtAppletFlux

Name:           cosmic-ext-flux
Version:        3.1.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
Summary:        Animated desktop wallpapers for COSMIC — play any video or GIF as your background
URL:            https://www.franz-e.net/cosmic-ext-flux/
Source0:        https://github.com/franz-net/cosmic-ext-flux/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/cosmic-ext-flux-daemon %{buildroot}%{_bindir}/cosmic-ext-flux-daemon
install -Dm755 target/rpm/cosmic-ext-applet-flux %{buildroot}%{_bindir}/cosmic-ext-applet-flux
install -Dm644 applet/resources/app.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 applet/resources/icon.svg %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 applet/resources/icon-stopped.svg %{buildroot}%{_scalableiconsdir}/%{appid}-stopped.svg
install -Dm644 data/cosmic-ext-flux-daemon.service %{buildroot}%{_userunitdir}/cosmic-ext-flux-daemon.service

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

%changelog
* Wed Jul 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
