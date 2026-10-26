Name:           game-devices-udev
Version:        1.1
Release:        1%{?dist}
Summary:        Udev rules for game controllers and other gaming devices
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

License:        MIT
URL:            https://codeberg.org/fabiscafe/game-devices-udev
Source0:        %{url}/archive/%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch
BuildRequires:  meson >= 1.0
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
Udev rules to make supported game controllers and other gaming devices
accessible with user-level permissions.

%prep
%autosetup -n %{name}

%conf
%meson

%build
%meson_build

%install
%meson_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%license LICENSE
%doc README.md NEWS.md
%{_udevrulesdir}/71-*-gdu.rules
%{_udevrulesdir}/71-uinput-dev-early-creation.rules
%{_modulesloaddir}/%{name}.conf

%changelog
* Mon Oct 26 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.1-1
- Initial package
