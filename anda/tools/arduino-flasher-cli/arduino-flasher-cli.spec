%global goipath         github.com/arduino/arduino-flasher-cli
Version:                0.3.0

%gometa -f

%global common_description %{expand:
CLI tool to flash UNO Q boards with the latest Arduino Linux image.}

%global golicenses      LICENSE license_header.tpl
%global godocs          README.md

Name:           arduino-flasher-cli
Release:        1%?dist
Summary:        CLI tool to flash UNO Q boards with the latest Arduino Linux image
License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}
BuildRequires:  anda-srpm-macros

%description %{common_description}

%gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-cli %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduino-flasher-cli -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/arduino-flasher-cli

%gopkgfiles

%changelog
* Fri Nov 14 2025 Jaiden Riordan <jade@fyralabs.com>
- Package Arduino Flasher :3
