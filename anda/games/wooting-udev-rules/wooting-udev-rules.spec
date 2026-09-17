%global appid io.wooting.Udev


Name:           wooting-udev-rules
Version:        1
Release:        1%{?dist}
Summary:        Udev rules for wooting keyboards
Provides:       wooting-udev = %{version}-%{release}
License:        Unlicense
Source0:        70-wooting.rules
BuildArch:      noarch
BuildRequires:  systemd
BuildRequires:  anda-srpm-macros
Requires:       systemd-udev

%global udev_order 70

%description
Udev rules for Wooting keyboards to enable device access for use with the Wootility AppImage on Linux systems.

%prep

%build

%install
install -D -p -m 644 %SOURCE0 %{buildroot}%{_udevrulesdir}/%{udev_order}-wooting.rules
#
%post
%udev_rules_update

%postun
%udev_rules_update

%files
%_udevrulesdir/%{udev_order}-wooting.rules


%changelog
* Mon Jan 05 2026 Roice Young <dekodx@proton.me>
- Initial release
