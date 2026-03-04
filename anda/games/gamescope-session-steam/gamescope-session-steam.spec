%define debug_package %nil

%global commit 1a3fdb7fa15a4bba7204bef69702b7a10a297828
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241205

Name:           gamescope-session-steam
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        gamescope-session-steam
License:        MIT
URL:            https://github.com/OpenGamingCollective/gamescope-session-steam
Source0:        %url/archive/%commit.tar.gz
Packager:       Tulip Blossom <tulilirockz@outlook.com>
BuildArch:      noarch

%description
%summary.

%prep
%autosetup -n %name-%commit

%build

%install
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/steam-http-loader"
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/steamos-select-branch"
install -Dpm0755 -t "%buildroot%_bindir/" ".%_bindir/steamos-session-select"
install -Dpm0644 -t "%buildroot%_datadir/applications/" ".%_datadir/applications/steam_http_loader.desktop"
install -Dpm0644 -t "%buildroot%_datadir/applications/" ".%_datadir/applications/gamescope-mimeapps.list"
install -Dpm0755 -t "%buildroot%_datadir/gamescope-session-plus/sessions.d/" ".%_datadir/gamescope-session-plus/sessions.d/steam"
install -Dpm0644 -t "%buildroot%_datadir/polkit-1/actions/" ".%_datadir/polkit-1/actions/org.chimeraos.update.policy"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/gamescope-session-steam.desktop"
install -Dpm0644 -t "%buildroot%_datadir/wayland-sessions/" ".%_datadir/wayland-sessions/gamescope-session.desktop"

%files
%license LICENSE
%{_bindir}/steam-http-loader
%{_bindir}/steamos-select-branch
%{_bindir}/steamos-session-select
%{_datadir}/applications/gamescope-mimeapps.list
%{_datadir}/applications/steam_http_loader.desktop
%{_datadir}/gamescope-session-plus/sessions.d/steam
%{_datadir}/polkit-1/actions/org.chimeraos.update.policy
%{_datadir}/wayland-sessions/gamescope-session-steam.desktop
%{_datadir}/wayland-sessions/gamescope-session.desktop

%changelog
* Mon Feb 03 2026 Tulip Blossom <tulilirockz@outlook.com> - 20241205.1a3fdb7f-1
- Move to OGC source and clean up
