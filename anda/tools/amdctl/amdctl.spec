Name: amdctl
Summary: Set P-State voltages and clock speeds on recent AMD CPUs on Linux
License: GPLv3
URL: https://github.com/kevinlekiller/%{name}

Version: 0.11
Release: 2%{?dist}
Source0: https://github.com/kevinlekiller/%{name}/archive/refs/tags/v%{version}.tar.gz
# Remove hardcoded CFLAGS and CC
Patch0: 0001-RPM-makefile-Remove-unused-Makefile-variables.patch

# `msr` is a builtin kernel module
Requires: kernel-core systemd-udev coreutils
BuildRequires: make gcc kernel-headers glibc-headers

%description
Tool for changing voltages and clock speeds for AMD processors with
control over every power state and CPU core.

%prep
%setup -qn %{name}-%{version}
patch -p1 -i %{PATCH0}

%build
%set_build_flags
%make_build

%install
# install the 'amdctl' binary
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ./%{name} %{buildroot}/%{_bindir}/

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
/%{_bindir}/%{name}
/%{_libexecdir}/%{name}
/%{_modulesloaddir}/%{name}.conf
/%{_udevrulesdir}/99-%{name}.rules

%changelog
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