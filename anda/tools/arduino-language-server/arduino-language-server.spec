# https://github.com/arduino/arduino-language-server
%global goipath github.com/arduino/arduino-language-server
Version:        0.7.7

%gometa -f


%global common_description %{expand:
The Arduino Language Server is the tool that powers the autocompletion of the new Arduino IDE 2. It implements the standard Language Server Protocol so it can be used with other IDEs as well.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           arduino-language-server
Release:        1%?dist
Summary:        An Arduino Language Server based on Clangd for Arduino code autocompletion
License:        AGPL-3.0
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  anda-srpm-macros clang

%description
%{common_description}

%gopkg

%prep
%goprep
%go_prep_online

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-language-server %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduino-language-server -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-language-server

%changelog
* Fri Dec 27 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-language-server

