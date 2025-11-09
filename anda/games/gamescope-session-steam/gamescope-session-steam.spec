%define debug_package %nil

%global commit ba967fd8c5de7dc6c623b614296b3872255996b0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250904

Name:           gamescope-session-steam
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        gamescope-session-steam
License:        MIT
URL:            https://github.com/bazzite-org/gamescope-session-steam
Source0:        %url/archive/%commit.tar.gz

%description
%summary.

%prep
%autosetup -n %name-%commit

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
rm -rf %{buildroot}%{_bindir}/steamos-polkit-helpers
rm %{buildroot}%{_bindir}/jupiter-biosupdate
# We want to actually keep this for drop-in scripts
# rm %{buildroot}%{_bindir}/steamos-session-select
rm %{buildroot}%{_bindir}/steamos-update


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