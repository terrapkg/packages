# Based on syzdell's COPR specs and patches, modified for Terra

Name:       system76-power
Version:    %commit_date.%shortcommit
Release:    1%dist
Summary:    Power Profiles and dGPU Hotplug for System76 Laptops
License:    GPLv3
Packager:   Jaiden Riordan <jade@fyralabs.com>
URL:        https://github.com/szydell/system76-power
Source0:     %url/archive/%commit/system76-power-%commit.tar.gz
BuildRequires: cargo systemd-rpm-macros dbus-devel libusb-compat-0.1-devel
Requires: dbus-common libusb libusb-compat-0.1 

%description
%summary.

%prep
%autosetup -n system76-power-%commit
%cargo_prep_online

%install
%cargo_install

install -Dpm 0644 "completion/completion.sh" "%{buildroot}%{_datadir}/bash-completion/completions/%{name}"
install -D -m 0644 "debian/%{name}-wake.service" "%{buildroot}/%{_unitdir}/%{name}-wake.service"
install -D -m 0644 "data/com.system76.PowerDaemon.service" "%{buildroot}/%{_unitdir}/com.system76.PowerDaemon.service"

%post
%systemd_post com.system76.PowerDaemon.service

%preun
%systemd_preun com.system76.PowerDaemon.service

%postun
%systemd_postun_with_restart com.system76.PowerDaemon.service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}-wake.service
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/com.system76.PowerDaemon.service
%{_datadir}/dbus-1/interfaces/com.system76.PowerDaemon.xml
%{_datadir}/dbus-1/system.d/com.system76.PowerDaemon.conf
%{_datadir}/polkit-1/actions/com.system76.PowerDaemon.policy

%ghost %{_sysconfdir}/modprobe.d/%{name}.conf
%ghost %{_sysconfdir}/modules-load.d/%{name}.conf

%changelog
* Fri Jan 9 2026 Jaiden Riordan <jade@fyralabs.com>
- Package System76 Power

