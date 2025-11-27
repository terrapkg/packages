%global _udevrulesdir /usr/lib/udev/rules.d

Name:           HeadsetControl
Version:        3.1.0
Release:        1%?dist
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
URL:            https://github.com/Sapd/HeadsetControl
Source:         %{url}/releases/download/%{version}/headsetcontrol-%{version}.tar.gz
License:        GPL-3.0
Provides:       headsetcontrol

BuildRequires:  cmake gcc hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux.
Currently, support is provided for adjusting sidetone, getting battery
state, controlling LEDs, and setting the inactive time.

%prep
%autosetup

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
