%define debug_package %nil

Name:          arduino-lint
Version:       1.3.0
Release:       1%?dist
Summary:       Tool to check for problems with Arduino projects.
License:       GPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/arduino-lint
Source0:       %url/archive/refs/tags/%version.tar.gz
BuildRequires: golang git go-rpm-macros anda-srpm-macros

%description
%summary

%prep
%autosetup -n arduino-lint-%version

%build
go build

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 arduino-lint %buildroot%{_bindir}/arduino-lint

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-lint

%changelog
* Thu Dec 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-lint