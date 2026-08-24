%global debug_package   %{nil}

%global commit          afcae816689b910495941731751a79613c38fe7f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260824

Name:   	umbriel-nightly
Version:	0^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A work-in-progress Wayland compositor designed for daily use, with scrolling and dwindle layouts, per-output workspaces, window rules, blur, shadows, and fluid animations

License:	MIT
URL:		https://github.com/noctalia-dev/umbriel

BuildRequires:  wlroots-devel >= 0.20
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  stb-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(scenefx-0.5)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)

Requires:       xwayland-satellite
Requires:       xdg-desktop-portal-nightly

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{summary}.

%prep
%git_clone %{url}.git %{commit}

%conf
%meson

%build
%meson_build

%install
%meson_install --skip-subprojects

%post
%systemd_user_post umbriel.service

%preun
%systemd_user_preun umbriel.service

%postun
%systemd_user_postun umbriel.service

%files
%doc README.md
%license LICENSE
%{_bindir}/umbriel
%{_bindir}/start-umbriel
%config %{_datadir}/umbriel/config.toml
%{_datadir}/wayland-sessions/umbriel.desktop
%{_userunitdir}/umbriel.service
%{_userunitdir}/umbriel-session.target
%{_userunitdir}/umbriel-shutdown.target

%changelog
* Mon Aug 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
