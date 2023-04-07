%global forgeurl https://gitlab.com/ubports/development/core/lomiri-session
%global commit 94a0d8d12e63fd4a298fb4cdce5f11e0a20bdb8c
%forgemeta

Name:       lomiri-session
Version:    0.2
Release:    %autorelease
Summary:    Configuration schemas for lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-session
Source0:    %{url}/-/archive/%commit/lomiri-desktop-session-%commit.tar.gz
Patch0:     https://sources.debian.org/data/main/l/lomiri-session/0.2-3/debian/patches/0001_desktop-dm-lomiri-session-Drop-old-wizard-has-run-ch.patch
Patch1:     https://sources.debian.org/data/main/l/lomiri-session/0.2-3/debian/patches/0002_lomiri-session-Put-evaluation-of-ps-call-in-quotes.patch
Patch2:     https://sources.debian.org/data/main/l/lomiri-session/0.2-3/debian/patches/0003_lomiri-session-Properly-differentiate-between-Ubuntu.patch
Patch3:     https://sources.debian.org/data/main/l/lomiri-session/0.2-3/debian/patches/0004_lomiri-session-Check-for-presence-of-Xwayland-use-th.patch
Patch4:     https://sources.debian.org/data/main/l/lomiri-session/0.2-3/debian/patches/0005_systemd-lomiri.service-Drop-Before-and-Wants-for-ind.patch
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
%autosetup -n %{name}-%commit -p1

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
