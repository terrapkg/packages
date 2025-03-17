%global commit 33b49684edb7a8ac65bbca4d7378959208fbe604
%global commit_date 20250317
%global shortcommit %{sub %{commit} 1 7 }
%global ver 0.1.3

Name:           mwc
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Tiling Wayland compositor based on wlroots and scenefx

License:        MIT
URL:            https://github.com/dqrk0jeste/mwc
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(scenefx-0.2)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  wayland-devel

Requires:       libdrm
Requires:       libinput
Requires:       libxkbcommon
Requires:       pixman
Requires:       wayland-devel
Requires:       wlroots
Requires:       xdg-desktop-portal-wlr

Recommends:     waybar kitty rofi-wayland

Packager:       sadlerm <lerm@chromebooks.lol>

Provides:       owl = %{version}-%{release}
Obsoletes:      owl < 0^20250124.9999999

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 examples/example.conf %{buildroot}%{_datadir}/%{name}/example.conf

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-ipc
%{_datadir}/%{name}/default.conf
%{_datadir}/%{name}/example.conf
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf


%changelog
* Thu Feb 27 2025 sadlerm <lerm@chromebooks.lol>
- New upstream name
- Package is now built with meson
* Fri Jan 31 2025 sadlerm <lerm@chromebooks.lol>
- Initial package
