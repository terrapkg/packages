%define sdk_version 2.2.0
%global ver 2.2.0-a4
%global sanitized_ver %(echo %{ver} | sed 's/-//g')

Name:           picotool
Version:        %sanitized_ver
Release:        3%?dist
Summary:        Tool to inspect RP2040 binaries
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi/picotool
Source0:        https://github.com/raspberrypi/picotool/archive/refs/tags/%ver.tar.gz
Source1:        https://github.com/raspberrypi/pico-sdk/archive/%sdk_version.tar.gz#/pico-sdk-%sdk_version.tar.gz
BuildRequires:  cmake g++ libusb1-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Picotool is a tool for inspecting RP2040 binaries, and interacting with RP2040 devices when they are in BOOTSEL mode.

%prep
%autosetup -a 1 -n %name-%ver

%build
%cmake -DPICO_SDK_PATH="../pico-sdk-%sdk_version"
%cmake_build

%install
%cmake_install

mv %buildroot{%_prefix/lib,%_libdir}

%files
%doc README.md
%license LICENSE.TXT
%_bindir/picotool
%_libdir/cmake/picotool/*
%_datadir/picotool/*

%changelog
* Mon Nov 18 2024 Owen-sz <owen@fyralabs.com>
- Package Raspberry Pi Picotools
