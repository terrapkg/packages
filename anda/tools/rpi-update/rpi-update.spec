%define debug_package %nil

%global commit bb117f13b1a39b646f6ebebdbb5193bee4a24855
%global commit_date 20250326
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rpi-update
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        An easier way to update the firmware of your Raspberry Pi. 
License:        MIT
URL:            https://github.com/raspberrypi/rpi-update
Source0:        %url/archive/%commit.tar.gz
Requires:       bash
ExclusiveArch:  aarch64

%description
%summary

%prep
%autosetup -n rpi-update-%commit

%build

%install
install -Dm755 rpi-update          %buildroot%_bindir/rpi-update

%files
%doc README.md
%license LICENSE
%_bindir/rpi-update

%changelog
* Sat Dec 14 2024 Owen Zimmerman <owen@fyralabs.com>
- Package rpi-update
