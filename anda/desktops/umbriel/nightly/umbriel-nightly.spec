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
Source0:	https://github.com/noctalia-dev/umbriel/archive/%{commit}/umbriel-%{commit}.tar.gz

BuildRequires:  wlroots-devel >= 0.20
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  sdbus-cpp-devel
BuildRequires:  tomlplusplus-devel
BuildRequires:  json-devel
BuildRequires:  md4c-devel
BuildRequires:  stb-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(scenefx-0.5)
BuildRequires:  pkgconfig(cairo)

Requires:       xwayland-satellite
Requires:       xdg-desktop-portal-nightly

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{Summary}.

%prep
%autosetup -n umbriel-%{commit}

%conf
%meson

%build
%meson_build

%install
%meson_install --skip-subprojects

%post
%systemd_user_post umbriel.service
%systemd_user_post umbriel-session.target
%systemd_user_post umbriel-shutdown.target

%preun
%systemd_user_preun umbriel.service
%systemd_user_preun umbriel-session.target
%systemd_user_preun umbriel-shutdown.target

%postun
%systemd_user_postun umbriel.service
%systemd_user_postun umbriel-session.target
%systemd_user_postun umbriel-shutdown.target

%files
%doc README.md
%license LICENSE
%{_bindir}/umbriel
%{_bindir}/start-umbriel
%{_datadir}/umbriel/config.toml
%{_datadir}/wayland-sessions/umbriel.desktop
%{_userunitdir}/umbriel.service
%{_userunitdir}/umbriel-session.target
%{_userunitdir}/umbriel-shutdown.target

%changelog
* Mon Aug 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
