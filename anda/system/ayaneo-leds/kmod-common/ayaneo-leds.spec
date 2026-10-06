%global commit 0be120d0d580363f386a9e51ebf0370d6367f45c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20261006
%global ver 0.2.1

Name:           ayaneo-leds
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        LED RGB control for Ayaneo legacy devices
License:        GPL-2.0-or-later
URL:            https://github.com/TiPSilva/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

Conflicts:      ayaneo-platform
Conflicts:      dkms-ayaneo-platform
Packager:       Tiago Silva <tiago.paulo@live.com>

%description
Linux kernel module to control the RGB rings on legacy AYANEO
devices with the old EC interface.
AYANEO 2S confirmed.
with the same interface waiting confirmation:
AYANEO 2, GEEK, GEEK 1S, AIR, AIR Pro, AIR 1S,
AIR 1S Limited, AIR Plus (Mendocino), SuiPlay0X1.
This package contains common files for the akmod.

%prep
%autosetup -p1 -n %{name}-%{commit}

%files
%license LICENSE
%doc README.md TESTING.md

%changelog
* Wed Sep 30 2026 Tiago Silva <tiago.paulo@live.com> - 0.2.1^20260930git.11e5e4c-1
- Initial package
