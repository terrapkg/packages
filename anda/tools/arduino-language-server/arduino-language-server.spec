%define debug_package %nil

Name:          arduino-language-server
Version:       0.7.6
Release:       1%?dist
Summary:       Arduino command line tool.
License:       AGPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/arduino-language-server
Source0:       %url/archive/refs/tags/%version.tar.gz
BuildRequires: golang git go-rpm-macros anda-srpm-macros clang arduino-cli

%description
%summary

%prep
%autosetup -n arduino-language-server-%version

%build
mkdir -p bin
%go_build_online

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 build/bin/arduino-language-server %buildroot%{_bindir}/arduino-language-server

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-language-server

%changelog
* Fri Dec 27 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-language-server
