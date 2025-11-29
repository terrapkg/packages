# https://github.com/arduino/arduino-fwuploader
%global goipath github.com/arduino/arduino-fwuploader
Version:        2.4.1

%gometa -f


%global common_description %{expand:
The Arduino Firmware Uploader is a tool made to update the firmware and/or add SSL certificates for any Arduino board equipped with ESP32-S3 or NINA Wi-Fi module.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           arduino-fwuploader
Release:        3%?dist
Summary:        Update the firmware and/or add SSL certificates for any Arduino board equipped with WINC or NINA Wi-Fi module
License:        AGPL-3.0
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  anda-srpm-macros python3-devel go-task

%description
%{common_description}

%gopkg

%prep
%goprep -A

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-fwuploader %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduino-fwuploader -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-fwuploader

%changelog
* Sat Dec 28 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-fwuploader
