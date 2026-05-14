%global _udevrulesdir /usr/lib/udev/rules.d

%global commit      a35119a57dc4c9c3833778db369413c82069c9c2
%global commitdate  20251121
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           HeadsetControl-nightly
Version:        0^%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
URL:            https://github.com/Sapd/HeadsetControl
Source:         %{url}/archive/%{commit}.tar.gz
Patch0:         CMAKE_INSTALL_LIBDIR.patch
License:        GPL-3.0-or-later
Provides:       headsetcontrol-nightly
Conflicts:      headsetcontrol

BuildRequires:  cmake gcc gcc-c++ hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux.
Currently, support is provided for adjusting sidetone, getting battery
state, controlling LEDs, and setting the inactive time.

%package devel
%pkg_devel_files

%package static
%pkg_static_files

%prep
%autosetup -n HeadsetControl-%{commit} -p1

%conf
%cmake \
     -DCMAKE_INSTALL_LIBDIR=%{_lib}

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license license
%{_bindir}/headsetcontrol
%{_udevrulesdir}/70-headsets.rules

%changelog
* Wed May 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Add devel and static subpackages, add patch, fix license

* Wed Nov 26 2025 metcya <metcya@gmail.com>
- package HeadsetControl
