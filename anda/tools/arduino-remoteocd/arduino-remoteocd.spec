%global goipath github.com/arduino/remoteocd

%global commit 6e375c835fe319e8eef3f40578bf8de044156ce1
%global commit_date 20251105
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:        0^%commit_date.%shortcommit

%gometa -f

Name:           remoteocd
Release:        1%?dist
Summary:        Flexible firmware flashing for the Arduino UNO Q Microcontroller
License:        GPL-3.0-only

URL:            https://github.com/arduino/remoteocd
Source:         %{gosource}
BuildRequires:  anda-srpm-macros
BuildRequires:  go-rpm-macros
BuildRequires:  go-task

Provides:       arduino-remoteocd

Recommends:     arduino-cli

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
remoteocd is a specialized utility designed to manage firmware deployment for the Arduino UNO Q board. This tool acts as a versatile wrapper for OpenOCD (Open On-Chip Debugger), allowing you to flash a binary onto the MCU using one of three transparently handled modes:

    Local, by flashing from the UNO Q's MPU (Linux) environment.
    ADB over USB.
    SSH over a remote pc.

remoteocd is part of the arduino:zephyr:unoq platform.

%gopkg

%prep
%goprep -A

%build
%define gomodulesmode GO111MODULE=on
%gobuild

%install
install -Dm755 remoteocd %{buildroot}%{_bindir}/remoteocd

%files
%license LICENSE
%doc README.md
%{_bindir}/remoteocd

%changelog
* Mon Dec 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
