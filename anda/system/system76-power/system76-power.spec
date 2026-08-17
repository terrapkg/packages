%global appid com.system76.PowerDaemon

Name:           system76-power
Version:        1.2.8
Release:        1%{?dist}
Summary:        Power Profiles and dGPU Hotplug for System76 Laptops
License:        GPL-3.0-only

Packager:       Jaiden Riordan <jade@fyralabs.com>
URL:            https://github.com/pop-os/system76-power
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  dbus-devel 
BuildRequires:  systemd-rpm-macros 
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold

%description
%summary.

%prep
%autosetup 
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 644 data/%{appid}.conf %{buildroot}%{_datadir}/dbus-1/system.d/%{appid}.conf
install -Dm 644 data/%{appid}.policy %{buildroot}%{_datadir}/polkit-1/actions/%{appid}.policy
install -Dm 644 data/%{appid}.service %{buildroot}%{_unitdir}/%{appid}.service
install -Dm 644 data/%{appid}.xml %{buildroot}%{_datadir}/dbus-1/interfaces/%{appid}.xml
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}

%post
%systemd_post com.system76.PowerDaemon.service

%preun
%systemd_preun com.system76.PowerDaemon.service

%postun
%systemd_postun_with_restart com.system76.PowerDaemon.service

%files
%doc README.md TESTING.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{appid}.service
%{_datadir}/dbus-1/interfaces/%{appid}.xml
%{_datadir}/dbus-1/system.d/%{appid}.conf
%{_datadir}/polkit-1/actions/%{appid}.policy

%changelog
* Fri Jan 9 2026 Jaiden Riordan <jade@fyralabs.com>
- Port to Terra

