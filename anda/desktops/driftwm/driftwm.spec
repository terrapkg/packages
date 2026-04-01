Name:           driftwm
Version:        0.1.3
Release:        1%{?dist}
Summary:        A trackpad-first infinite canvas Wayland compositor
License:        GPL-3.0-or-later
URL:            https://github.com/malbiruk/driftwm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libgbm-devel

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
export PREFIX=/usr
%make_install

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/driftwm
%{_bindir}/driftwm-session
%{_datadir}/wayland-sessions/driftwm.desktop
%{_datadir}/xdg-desktop-portal/driftwm-portals.conf
%{_sysconfdir}/driftwm/config.toml
%{_datadir}/driftwm/wallpapers/*.glsl

%changelog
* Tue Mar 17 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
