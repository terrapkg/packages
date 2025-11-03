%global commit a1ace571823be5979c135e9cb8e9ae103c7641ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250715

Name:          udev-joystick-blacklist
Version:       0^%{commit_date}git%{shortcommit}
Release:       1%{?dist}
Summary:       Fix for keyboard/mouse/tablet being detected as joysticks in Linux
License:       Public Domain
URL:           https://github.com/denilsonsa/udev-joystick-blacklist
Source0:       %{url}/archive/%{commit}.tar.gz
BuildRequires: systemd-rpm-macros
BuildArch:     noarch

%description
There are several devices that, although recognized by kernel as joysticks, are not joysticks.

This package contains rules which will prevent those devices from being recognized as joysticks.

%prep
%autosetup -n %{name}-%{commit}

%package       rm
Summary:       Fix for keyboard/mouse/tablet being detected as joysticks in Linux
Obsoletes:     steam-device-rules <= 1.0.0.85-1

%description   rm
There are several devices that, although recognized by kernel as joysticks, are not joysticks.

This package contains rules which will prevent those devices from being recognized as joysticks by removing the devices.

mkdir -p %{buildroot}%{_udevrulesdir}
install -Dpm644 after_kernel_4_9/51-these-are-not-joysticks.rules -t %{buildroot}%{_udevrulesdir}
install -Dpm644 after_kernel_4_9/51-these-are-not-joysticks-rm.rules -t %{buildroot}%{_udevrulesdir}

%files
%doc README.md
%{_udevrulesdir}/51-these-are-not-joysticks.rules

%files rm
%doc README.md
%{_udevrulesdir}/51-these-are-not-joysticks-rm.rules
