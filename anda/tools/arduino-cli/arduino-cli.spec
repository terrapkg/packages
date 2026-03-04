# https://github.com/arduino/arduino-cli
%global goipath github.com/arduino/arduino-cli
Version:        1.4.1

%gometa -f


%global common_description %{expand:
Arduino CLI is an all-in-one solution that provides Boards/Library Managers, sketch builder, board detection, uploader, and many other tools needed to use any Arduino compatible board and platform from command line or machine interfaces.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           arduino-cli
Release:        1%?dist
Summary:        Arduino command line tool
License:        GPL-3.0
Packager:       Owen Zimmerman <owen@fyralabs.com>

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
install -Dm755 %{gobuilddir}/bin/arduino-cli -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/arduino-cli

%changelog
* Thu Dec 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-cli

