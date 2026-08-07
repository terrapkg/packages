Name:       amdctl
Summary:    Set P-State voltages and clock speeds on recent AMD CPUs on Linux
License:    GPL-3.0-or-later
URL:        https://github.com/kevinlekiller/%{name}
Version:    0.11
Release:    2%{?dist}
Source0:    https://github.com/kevinlekiller/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: kernel-headers
BuildRequires: glibc-headers
BuildRequires: cmake-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: systemd-rpm-macros
Requires: kernel-core
Requires: systemd-udev
Requires: coreutils

%description
Tool for changing voltages and clock speeds for AMD processors with
control over every power state and CPU core.

%prep
%autosetup

%conf
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%build
%cmake_build

%install
# install the 'amdctl' binary
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 redhat-linux-build/%{name} %{buildroot}/%{_bindir}/

# add modules.load.d entry
mkdir -p %{buildroot}/%{_modulesloaddir}/
echo 'msr' > %{buildroot}/%{_modulesloaddir}/%{name}.conf

# write the udev helper script
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/
cat << 'EOF' > %{buildroot}/%{_libexecdir}/%{name}/udev-helper.sh
#!/bin/sh
echo 'on' > /sys/module/msr/parameters/allow_writes
EOF
chmod 0755 %{buildroot}/%{_libexecdir}/%{name}/udev-helper.sh

# add udev rules to enable msr writes
mkdir -p %{buildroot}/%{_udevrulesdir}/
cat << 'EOF' > %{buildroot}/%{_udevrulesdir}/99-%{name}.rules
DRIVER=="msr", RUN+="%{_libexecdir}/%{name}/udev-helper.sh"
EOF

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_modulesloaddir}/%{name}.conf
%{_udevrulesdir}/99-%{name}.rules

%changelog
* Tue Jun 16 2026 Owen-sz <owen@fyralabs.com> - 0.11-2
- Clean up spec

* Sat Nov 4 2023 <rmnscnce@ya.ru> - 0.11-1
- Track upstream to 0.11

* Fri Mar 18 2022 <rmnscnce@ya.ru> - 0.8-2
- Clean up RPM spec file

* Fri Mar 18 2022 <rmnscnce@ya.ru> - 0.8-1
- Track upstream to 0.8

* Mon Sep 13 2021 rmnscnce <rmnscnce@ya.ru> - 0.6.1-3
- Wrap %%description

* Mon Sep 13 2021 rmnscnce <rmnscnce@ya.ru> - 0.6.1-2
- Fix missing executable bit for udev-helper.sh

* Mon Sep 13 2021 rmnscnce <rmnscnce@ya.ru> - 0.6.1-1
- Track upstream to 0.6.1

* Mon May 24 2021 rmnscnce <rmnscnce@ya.ru> - 0.2-2.git+gb0ffbad
- Initial packaging
