%define _build_shell /bin/bash
%define debug_package %nil

Name:          arduino-cli
Version:       1.1.1
Release:       1%?dist
Summary:       Arduino command line tool.
License:       GPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/arduino-cli
Source0:       %url/archive/refs/tags/v%version.tar.gz
BuildRequires: golang git go-rpm-macros anda-srpm-macros

%description
%summary

%prep
%autosetup -n arduino-cli-%version

%build
mkdir -p bin
%go_build_online

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 build/bin/arduino-cli %buildroot%{_bindir}/arduino-cli

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-cli

%changelog
* Thu Dec 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-cli