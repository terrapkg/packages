%define debug_package %nil

%global commit f9aafe5fd7ec7adedf7e7cd06d03709e5ec601ef
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240606

Name:           gamescope-session-opengamepadui
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Gamescope session for OpenGamepadUI
License:        GPL-3.0-only
URL:            https://github.com/OpenGamingCollective/gamescope-session-opengamepadui
Source0:        %url/archive/%commit.tar.gz
Packager:       Tulip Blossom <tulilirockz@outlook.com>
Requires:       opengamepadui
BuildArch:      noarch

%description
%summary.

%prep
%autosetup -n %name-%commit

%build

%install
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/opengamepadui-session-select"
install -Dpm0755 -t "%buildroot%_datadir/gamescope-session-plus/sessions.d/" ".%_datadir/gamescope-session-plus/sessions.d/opengamepadui"
install -Dpm0644 -t "%buildroot%_datadir/polkit-1/actions/" ".%_datadir/polkit-1/actions/org.shadowblip.opengamepadui-session.policy"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/gamescope-session-opengamepadui.desktop"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/opengamepadui-session.desktop"

%files
%doc README.md
%{_bindir}/opengamepadui-session-select
%{_datadir}/gamescope-session-plus/sessions.d/opengamepadui
%{_datadir}/polkit-1/actions/org.shadowblip.opengamepadui-session.policy
%{_datadir}/wayland-sessions/gamescope-session-opengamepadui.desktop
%{_datadir}/wayland-sessions/opengamepadui-session.desktop

%changelog
* Mon Feb 03 2026 Tulip Blossom <tulilirockz@outlook.com> - 20240606.f9aafe5f-1
- Initial package
