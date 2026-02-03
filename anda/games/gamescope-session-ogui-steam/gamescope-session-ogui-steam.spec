%define debug_package %nil

%global commit 6835776876a2b9e5fc819bd8d98f06ae51fa6394
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20231030

Name:           gamescope-session-ogui-steam
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        gamescope-session-steam
License:        GPL-3.0-only
URL:            https://github.com/OpenGamingCollective/gamescope-session-ogui-steam
Source0:        %url/archive/%commit.tar.gz
Requires:       gamescope-session-steam
Requires:       opengamepadui
Packager:       Tulip Blossom <tulilirockz@outlook.com>
BuildArch:      noarch

%description
Gamescope Session for OpenGamepadUI in overlay mode with Steam

%prep
%autosetup -n %name-%commit

%build

%install
install -Dpm0755 -t "%buildroot%_datadir/gamescope-session-plus/sessions.d/" ".%_datadir/gamescope-session-plus/sessions.d/steam-plus"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/gamescope-session-steam-plus.desktop"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/gamepadui-with-qam-session.desktop"

%files
%doc README.md
%license LICENSE
%{_datadir}/gamescope-session-plus/sessions.d/steam-plus
%{_datadir}/wayland-sessions/gamescope-session-steam-plus.desktop
%{_datadir}/wayland-sessions/gamepadui-with-qam-session.desktop

%changelog
* Mon Feb 02 2026 Tulip Blossom <tulilirockz@outlook.com> - 20231030.6835776-1
- Initial package
