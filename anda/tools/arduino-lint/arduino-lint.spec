# https://github.com/arduino/arduino-lint
%global goipath github.com/arduino/arduino-lint
Version:        1.3.0

%gometa -f


%global common_description %{expand:
Arduino Lint is a command line tool that checks for common problems in Arduino projects:
 Sketches
 Libraries
 Boards platforms}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           arduino-lint
Release:        3%?dist
Summary:        Tool to check for problems with Arduino projects
License:        GPL-3.0
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  anda-srpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-lint %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduino-lint -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-lint

%changelog
* Thu Dec 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-lint

