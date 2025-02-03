%define debug_package %nil

Name:          arduino-create-agent
Version:       1.6.1
Release:       1%?dist
Summary:       Arduino Cloud Agent.
License:       AGPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/arduino-create-agent
Source0:       %url/archive/refs/tags/%version.tar.gz
Patch0:        update.patch
BuildRequires: golang git go-rpm-macros anda-srpm-macros 

%description
The Arduino Cloud Agent is a single binary that will sit on the traybar and work in the background.
It allows you to use the Arduino Cloud to seamlessly upload code to any USB connected Arduino board (or Yún in LAN) directly from the browser.

%prep
%autosetup -n arduino-create-agent-%version -p1

%build
%go_build_online

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 build/bin/arduino-create-agent %buildroot%{_bindir}/arduino-create-agent

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-create-agent

%changelog
* Sat Jan 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-create-agent
