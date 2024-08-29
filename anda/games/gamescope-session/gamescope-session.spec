%define debug_package %nil

%global commit aa57bda3f17f660064c1e63f9497fa0a46df1e86
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240821

Name:           gamescope-session
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        ChimeraOS session on Gamescope
License:        MIT
URL:            https://github.com/ChimeraOS/gamescope-session
Source0:        %url/archive/%commit.tar.gz
BuildRequires:  systemd-rpm-macros

%description
Gamescope session plus based on Valve's gamescope.

%prep
%autosetup -n gamescope-session-%commit

%build

%install
mkdir -p %buildroot
cp -r usr %buildroot/

%files
%doc README.md
%license LICENSE
%_bindir/export-gpu
%_bindir/gamescope-session-plus
%_libexecdir/gamescope-sdl-workaround
%_userunitdir/gamescope-session-plus@.service
%_datadir/gamescope-session-plus/device-quirks
%_datadir/gamescope-session-plus/gamescope-session-plus
