%global debug_package %{nil}
%global modulename hid-hori

Name:           dkms-%{modulename}
Version:        0.0.8
Release:        1%{?dist}
Summary:        HORI Truck Control System kernel module (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
BuildArch:      noarch
BuildRequires:  sed
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Requires:       gcc
Requires:       make
Requires:       kernel-devel >= 6.12
Requires(post): dkms
Requires(preun): dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod = %{?epoch:%{epoch}:}%{version}

%description
Experimental Linux kernel module for the HORI Truck Control System wheel
and shifter, including force feedback and wheel settings via sysfs.
DKMS rebuilds the module on kernel upgrades. Requires Linux 6.12 or newer.

%prep
%autosetup -n hori_control_systems-%{version}
cp %{SOURCE1} dkms.conf
sed -i 's/__VERSION_STRING/%{version}/g' dkms.conf

%install
install -d %{buildroot}%{_usrsrc}/%{modulename}-%{version}
cp -a Kbuild Makefile *.c *.h usbhid dkms.conf \
    %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} --rpm_safe_upgrade || exit $?
dkms build -m %{modulename} -v %{version} || exit $?
dkms install -m %{modulename} -v %{version} --force

%preun
dkms remove -m %{modulename} -v %{version} --all --rpm_safe_upgrade

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{modulename}-%{version}/
%if 0%{?fedora}
%config(noreplace) %{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Fri Nov 20 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.0.7staging-1
- Initial package
