%define debug_package %{nil}

%global commit 10a173b5536fc75cd93f8a3868349dad963542ef
%global commit_date 20260607
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ver 1.1

Name:           melonds
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        DS emulator, sorta
License:        GPL-3.0-or-later
URL:            https://melonds.kuribo64.net/
Source0:        https://github.com/melonDS-emu/melonDS/archive/%{commit}/melonDS-%{commit}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6)
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(libenet)
BuildSystem:    cmake

Provides:       melonDS-nightly

%description
%{summary}.

%files
%doc README.md
%license LICENSE
%{_bindir}/melonDS
%{_appsdir}/net.kuribo64.melonDS.desktop
%{_hicolordir}/128x128/apps/net.kuribo64.melonDS.png
%{_hicolordir}/16x16/apps/net.kuribo64.melonDS.png
%{_hicolordir}/256x256/apps/net.kuribo64.melonDS.png
%{_hicolordir}/32x32/apps/net.kuribo64.melonDS.png
%{_hicolordir}/48x48/apps/net.kuribo64.melonDS.png
%{_hicolordir}/64x64/apps/net.kuribo64.melonDS.png

%changelog
* Sat Jun 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
