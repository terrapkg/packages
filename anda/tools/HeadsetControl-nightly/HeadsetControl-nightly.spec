%global _udevrulesdir /usr/lib/udev/rules.d

%global commit      b7ecf68181dd4ff85f3b86d735145c76744db988
%global commitdate  20251121
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           HeadsetControl-nightly
Version:        0^%{commitdate}.%{shortcommit}
Release:        1%?dist
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
URL:            https://github.com/Sapd/HeadsetControl
Source:         %{url}/archive/%{commit}.tar.gz
License:        GPL-3.0
Provides:       headsetcontrol-nightly
Conflicts:      headsetcontrol

BuildRequires:  cmake gcc hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux.
Currently, support is provided for adjusting sidetone, getting battery
state, controlling LEDs, and setting the inactive time.

%prep
%autosetup -n HeadsetControl-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license license
%{_bindir}/headsetcontrol
%{_udevrulesdir}/70-headsets.rules

%changelog
* Wed Nov 26 2025 metcya <metcya@gmail.com>
- package HeadsetControl
