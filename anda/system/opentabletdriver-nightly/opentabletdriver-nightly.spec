%global commit 558cac02ce8c47b623dc336b8d5b643987fcfa33
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240917
%global ver v0.6.4.0

# We aren't using Mono but RPM expected Mono
%global __requires_exclude_from ^/usr/lib/opentabletdriver/.*$
%global __os_install_post %{nil}
%define debug_package %nil
%global dotnet_runtime_version 8.0

Name:           opentabletdriver-nightly
Version:        %ver^%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Open source, cross-platform, user-mode tablet driver
License:        LGPL-3.0-or-later
Conflicts:      opentabletdriver

URL:            https://github.com/OpenTabletDriver/OpenTabletDriver
Source:         %url/archive/%commit.tar.gz
Packager:       madonuko <mado@fyralabs.com>

BuildRequires: dotnet-sdk-%{dotnet_runtime_version}
BuildRequires: git-core jq systemd-rpm-macros

Requires: dotnet-runtime-%{dotnet_runtime_version}
Requires: libevdev.so.2()(64bit)
Requires: gtk3
Requires: udev
Suggests: libX11
Suggests: libXrandr

%description
OpenTabletDriver is an open source, cross platform, user mode tablet driver. The goal of OpenTabletDriver is to be cross platform as possible with the highest compatibility in an easily configurable graphical user interface.

%prep
%autosetup -n OpenTabletDriver-%commit

%build
./eng/linux/package.sh --output bin

%install
export DONT_STRIP=1
PREFIX="%{_prefix}" ./eng/linux/package.sh --package Generic --build false
mkdir -p "%{buildroot}"
mv ./dist/files/* "%{buildroot}"/
rm -rf ./dist
mkdir -p "%{buildroot}/%{_prefix}/lib/"
cp -r bin "%{buildroot}/%{_prefix}/lib/opentabletdriver"

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/opentabletdriver
%dir %{_prefix}/share/doc/opentabletdriver
%{_bindir}/otd
%{_bindir}/otd-daemon
%{_bindir}/otd-gui
%{_prefix}/lib/modprobe.d/99-opentabletdriver.conf
%{_prefix}/lib/modules-load.d/opentabletdriver.conf
%{_prefix}/lib/opentabletdriver/*
%{_prefix}/lib/systemd/user/opentabletdriver.service
%{_prefix}/lib/udev/rules.d/70-opentabletdriver.rules
%{_prefix}/share/applications/opentabletdriver.desktop
%{_prefix}/share/man/man8/opentabletdriver.8.gz
%{_prefix}/share/doc/opentabletdriver/LICENSE
%{_prefix}/share/pixmaps/otd.ico
%{_prefix}/share/pixmaps/otd.png
