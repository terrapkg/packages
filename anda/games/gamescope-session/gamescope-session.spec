%define debug_package %nil

%global commit 7887b2941dd1ec70bf002e8ea3cd6007859131ec
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251012

Name:           gamescope-session
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Gamescope session based on Valve's gamescope
License:        MIT
URL:            https://github.com/bazzite-org/gamescope-session
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
%{_bindir}/export-gpu
%{_bindir}/gamescope-session-plus
%{_datadir}/gamescope-session-plus/device-quirks
%{_datadir}/gamescope-session-plus/gamescope-session-plus
%{_userunitdir}/gamescope-session-plus@.service
%{_userunitdir}/gamescope-session.target


%changelog
%autochangelog
