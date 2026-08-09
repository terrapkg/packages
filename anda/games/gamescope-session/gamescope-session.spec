%define debug_package %nil

%global commit 4cf5e0e13368f65e7bfd6e8c3c8d1511f089438c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260804

Name:           gamescope-session
Version:        0~%{commit_date}git.%{shortcommit}
Release:        5%?dist
Summary:        Gamescope session based on Valve's gamescope
License:        MIT
URL:            https://github.com/OpenGamingCollective/gamescope-session
Source0:        %url/archive/%commit.tar.gz
Requires:       gamescope
Recommends:     (cardwire or switcheroo-control)
BuildRequires:  systemd-rpm-macros
Packager:       Tulip Blossom <tulilirockz@outlook.com>
BuildArch:      noarch

%description
Gamescope session plus based on Valve's gamescope.

%prep
%autosetup -n gamescope-session-%commit

%build

%install
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/export-gpu"
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/gamescope-session-plus"
install -Dpm0644 -t "%buildroot%_userunitdir/" ".%_userunitdir/gamescope-session-plus@.service"
install -Dpm0644 -t "%buildroot%_userunitdir/" ".%_userunitdir/gamescope-session.target"
install -Dpm0644 -t "%buildroot%_datadir/gamescope-session-plus/" ".%_datadir/gamescope-session-plus/device-quirks"
install -Dpm0755 -t "%buildroot%_datadir/gamescope-session-plus/" ".%_datadir/gamescope-session-plus/gamescope-session-plus"
install -Dpm0644 -t "%buildroot%_datadir/gamescope/scripts/50-custom/50-disable-explicit-sync.lua" ".%_datadir/gamescope/scripts/50-custom/50-disable-explicit-sync.lua"

%files
%doc README.md
%license LICENSE
%{_bindir}/export-gpu
%{_bindir}/gamescope-session-plus
%{_datadir}/gamescope-session-plus/device-quirks
%{_datadir}/gamescope-session-plus/gamescope-session-plus
%{_datadir}/gamescope/scripts/50-custom/50-disable-explicit-sync.lua
%{_userunitdir}/gamescope-session-plus@.service
%{_userunitdir}/gamescope-session.target

%changelog
%autochangelog
