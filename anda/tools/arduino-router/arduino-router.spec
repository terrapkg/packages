%global goipath github.com/arduino/arduino-router
Version:        0.10.0

%gometa -f

Name:           arduino-router
Release:        1%{?dist}
Summary:        The UNO Q router/bridge communication service (Python / Sketch)
License:        GPL-3.0-or-later
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/v%{version}.tar.gz
BuildRequires:  golang

%description
%{summary}.

%gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/arduino-router-cli %{goipath}

%install
install -Dm755 %{gobuilddir}/cmd/arduino-router-cli -t %{buildroot}%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/arduino-router-cli

%changelog
* Wed Oct 07 2026 Owen Zimmerman <owen@fyralabs.com> - 0.10.0-1
- Initial commit
