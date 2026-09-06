%global goipath github.com/arduino/serial-monitor
Version:        0.15.0

%gometa -f

Name:           arduino-serial-monitor
Release:        1%{?dist}
Summary:        Arduino pluggable monitor for serial ports
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
%gobuild -o %{gobuilddir}/bin/serial-monitor %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/serial-monitor -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/serial-monitor

%changelog
* Thu Jul 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
