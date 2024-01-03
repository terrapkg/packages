%global forgeurl https://gitlab.com/ubports/development/core/lomiri-session
%global commit d33d5b666d5c18150ce216cc838713f18d84385c
%forgemeta

Name:       lomiri-session
Version:    0.2
Release:    %autorelease
Summary:    Configuration schemas for lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-session
Source0:    %{url}/-/archive/%commit/lomiri-desktop-session-%commit.tar.gz
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libsystemd)
BuildRequires: inotify-tools
BuildRequires: lomiri
BuildRequires: systemd-rpm-macros
Recommends:    libayatana-common
Requires:      dbus-common
Requires:      inotify-tools
Requires:      lomiri

%description
Configuration schemas for lomiri.

%prep
%autosetup -n %{name}-%commit

%build
%cmake -DENABLE_TOUCH_SESSION=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/dm-lomiri-session
%{_bindir}/lomiri-*
%dir %{_prefix}/lib/lomiri-session
%{_prefix}/lib/lomiri-session/run-systemd-session
%{_userunitdir}/lomiri.service
# Touch session, needs lomiri-system-compositor
#{_datadir}/lightdm/lightdm.conf.d/52-lomiri-touch.conf
#{_datadir}/lightdm/sessions/lomiri-touch.desktop
#dir {_datadir}/lomiri-session
#{_datadir}/lomiri-session/lsc-wrapper
%{_datadir}/wayland-sessions/lomiri.desktop

%changelog
%autochangelog
