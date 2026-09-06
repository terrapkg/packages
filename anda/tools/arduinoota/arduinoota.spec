%global goipath github.com/arduino/arduinoOTA
Version:        1.4.1

%gometa -f

Name:           arduinoota
Release:        1%{?dist}
Summary:        Tool for uploading programs to Arduino boards over a network
License:        GPL-3.0-or-later
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  golang
Provides:       arduinoOTA

%description
%{summary}.

%gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduinoOTA %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduinoOTA -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/arduinoOTA

%changelog
* Thu Jul 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
