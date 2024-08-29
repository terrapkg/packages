%global commit_date 20240824
%global commit d22b585a81b8645f1d660b4db22c95231c4301cf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           duet-quirks
Version:        %commit_date.%shortcommit
Release:        1%?dist

License:        CC-BY-SA-4.0
Summary:        Quirks for the Lenovo Duet Chromebooks on Ultramarine Linux
URL:            https://github.com/Ultramarine-Linux/duet-quirks
Source0:        https://github.com/Ultramarine-Linux/duet-quirks/archive/%{commit}/duet-quirks-%{commit}.tar.gz

Requires:       udev libinput

BuildArch:      noarch

%description
Quirks for the Lenovo Duet Chromebooks on Ultramarine Linux.
Including a libinput rule for trackpad configuration and a udev rule for display rotation.

%prep
%autosetup -n duet-quirks-%commit

%install
install -Dm644 udev/61-cros-ec-accel.rules %buildroot%{_sysconfdir}/udev/61-cros-ec-accel.rules
install -Dm644 libinput/local-overrides.quirks %buildroot%{_sysconfdir}/libinput/local-overrides.quirks

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/udev/61-cros-ec-accel.rules
%{_sysconfdir}/libinput/local-overrides.quirks

%changelog
* Sat Aug 25 2024 junefish <june@fyralabs.com>
- Initial package
