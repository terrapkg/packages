# https://github.com/arduino/arduino-create-agent
%global goipath github.com/arduino/arduino-create-agent
Version:        1.7.0

%gometa -f


%global common_description %{expand:
The Arduino Cloud Agent is a single binary that will sit on the traybar and work in the background.
It allows you to use the Arduino Cloud to seamlessly upload code to any USB connected Arduino board (or Yún in LAN) directly from the browser.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           arduino-create-agent
Release:        1%?dist
Summary:        Arduino Cloud Agent
License:        AGPL-3.0
Packager:       Owen Zimmerman <owen@fyralabs.com>

URL:            %{gourl}
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  anda-srpm-macros

%description %{common_description}

%gopkg

%prep
%goprep
%go_prep_online
sed -iE '/^func Start(/,/^}$/s@return start\(src\)@return ""@' updater/update.go
cat updater/update.go
sed -iE '/r.POST("/update", updateHandler)/d' main.go
cat main.go

%build
sed -iE '/^func Start(/,/^}$/s@return start\(src\)@return ""@' src/updater/update.go
cat src/updater/update.go
sed -iE '/r.POST("/update", updateHandler)/d' src/main.go
cat src/main.go
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-create-agent %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/arduino-create-agent -t %buildroot%{_bindir}

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-create-agent

%changelog
* Sat Jan 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-create-agent

