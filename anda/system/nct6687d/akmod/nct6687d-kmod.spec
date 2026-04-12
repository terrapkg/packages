# The reason why this package is a separate from the main one despite using the same sources
# is because akmods use the srpm to build the kmod package, and if the kmod package is included
# in the main package, akmods will reinstall the userspace package every time the kernel is updated.

%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%global commit cedda8bff09a4083e07414fb80fdc3901e7ab544
%global commitdate 20260411
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global modulename nct6687d

Name:           %{modulename}-kmod
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the NCT6687D hardware monitoring chip
License:        GPL-2.0-or-later
URL:            https://github.com/Fred78290/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
BuildArch:      x86_64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel driver for the NCT6687D hardware monitoring chip.
This kernel module permit to recognize the chipset Nuvoton NCT6687-R in lm-sensors package. This sensor is present on some B550 motherboard such as MSI or ASUS.
The implementation is minimalist and was done by reverse coding of Windows 10 source code from LibreHardwareMonitor

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -n %{modulename}-%{commit}

for kernel_version in %{?kernel_versions} ; do
  cp -a %{modulename}-%{commit} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
  make V=0 %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*}
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

%changelog
* Sat Apr 11 2026 Luan Oliveira <luanv.oliveira@outlook.com> - 1.0^20260411git.cedda8b-1
- Initial package
