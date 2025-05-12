%define debug_package %nil

%global commit 50304917b71ad220082565c5029e9393e6464a1f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250408

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
%_userunitdir/gamescope-session-plus@.service
%_datadir/gamescope-session-plus/device-quirks
%_datadir/gamescope-session-plus/gamescope-session-plus

%changelog
%autochangelog
