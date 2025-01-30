%global commit 2456a0ac3e4722eb1087727cc7f7ca8392d60a99
%global commit_date 20250124
%global shortcommit %{sub %{commit} 1 7 }

Name:           owl
Version:        0^%{commit_date}.%{shortcommit}
Release:        1%{?dist}
Summary:        Tiling Wayland compositor based on wlroots

License:        MIT
URL:            https://github.com/dqrk0jeste/owl
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  make gcc
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  wayland-devel
BuildRequires:  wlroots-devel

Requires:       libdrm
Requires:       libinput
Requires:       libxkbcommon
Requires:       pixman
Requires:       wayland-devel
Requires:       wlroots
Requires:       xdg-desktop-portal-wlr

Recommends:     waybar kitty rofi-wayland

Packager:       sadlerm <lerm@chromebooks.lol>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build all

%install
install -Dm755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 build/%{name}-ipc %{buildroot}%{_bindir}/%{name}-ipc
install -Dm644 default.conf %{buildroot}%{_datadir}/%{name}/default.conf
install -Dm644 examples/example.conf %{buildroot}%{_datadir}/%{name}/example.conf
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
install -Dm644 %{name}-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/%{name}-portals.conf

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
* Fri Jan 31 2025 sadlerm <lerm@chromebooks.lol>
- Initial package
