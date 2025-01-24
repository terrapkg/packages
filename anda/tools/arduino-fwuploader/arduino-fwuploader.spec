%define debug_package %nil

Name:          arduino-fwuploader
Version:       2.4.1
Release:       1%?dist
Summary:       A Command Line Tool made to update the firmware and/or add SSL certificates for any Arduino board equipped with WINC or NINA Wi-Fi module.
License:       AGPLv3
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/arduino/arduino-fwuploader
Source0:       %url/archive/refs/tags/%version.tar.gz
BuildRequires: golang git go-rpm-macros anda-srpm-macros python3 go-task

%description
%summary

%prep
%autosetup -n arduino-fwuploader-%version

%build
mkdir -p bin
%go_build_online

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 build/bin/arduino-fwuploader %buildroot%{_bindir}/arduino-fwuploader

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/arduino-fwuploader

%changelog
* Sat Dec 28 2024 Owen Zimmerman <owen@fyralabs.com>
- Package arduino-fwuploader