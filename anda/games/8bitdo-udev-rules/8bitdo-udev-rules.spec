
Name:           8bitdo-udev-rules
Version:        1.0
Release:        1%{?dist}
Summary:        Udev rules for 8Bitdo controllers
Provides: 8bitdo-udev = %{version}-%{release}
License:        Unlicense
Source0:        71-8bitdo.rules
BuildArch:      noarch
BuildRequires:  systemd
Requires:       systemd-udev

%global udev_order 71

%description
Udev rules for 8Bitdo controllers, for use with Steam Input
and generic gamepad support in Linux.

%prep

%build

%install
install -D -p -m 644 %SOURCE0 %{buildroot}%{_udevrulesdir}/%{udev_order}-8bitdo.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%_udevrulesdir/%{udev_order}-8bitdo.rules



%changelog
* Thu Sep 04 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
