%global goipath github.com/arduino/arduino-app-cli
Version:        0.8.3

%gometa -f

Name:           arduino-app-cli
Release:        1%?dist
Summary:        The CLI and service that manages and runs Arduino Apps on UNO Q
License:        GPL-3.0-only

URL:            https://github.com/arduino/arduino-app-cli
Source:         %{gosource}
BuildRequires:  anda-srpm-macros
BuildRequires:  go-rpm-macros
BuildRequires:  go-task

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%gopkg

%prep
%goprep -A

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/arduino-app-cli %{goipath}/cmd/arduino-app-cli

%install
install -Dm755 %{gobuilddir}/cmd/arduino-app-cli %{buildroot}%{_bindir}/arduino-app-cli

%files
%license LICENSE
%doc README.md
%{_bindir}/arduino-app-cli

%changelog
* Thu Dec 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
