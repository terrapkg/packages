Name:           hid-hori
Version:        0.0.8
Release:        1%{?dist}
Summary:        HORI Truck Control System driver common files
License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Requires:       (%{name}-akmod-modules = %{?epoch:%{epoch}:}%{version} if akmod-%{name})
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Experimental Linux kernel module for the HORI Truck Control System wheel
and shifter, including force feedback and wheel settings via sysfs.
This package contains the udev rules and documentation shared between the
akmod and DKMS variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      %{name}-kmod = %{?epoch:%{epoch}:}%{version}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -n hori_control_systems-%{version}
echo hid-hori > %{name}.conf

%install
install -Dpm644 udev/99-hori-wheel.rules \
    %{buildroot}%{_udevrulesdir}/99-hori-wheel.rules
install -Dpm644 %{name}.conf %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/99-hori-wheel.rules

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Fri Nov 20 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.0.7staging-1
- Initial package
