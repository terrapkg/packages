# The reason why this package is a separate from the main one despite using the same sources
# is because akmods use the srpm to build the kmod package, and if the kmod package is included
# in the main package, akmods will reinstall the userspace package every time the kernel is updated.

%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%global commit 1be4fb1cd9d60b5ddefc2a4201a898766a731400
%global commitdate 20260626
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global modulename ryzen_smu

Name:           %{modulename}-kmod
Version:        0.1.7^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver that exposes access to the SMU (System Management Unit) for certain AMD Ryzen processors
License:        GPL-2.0-only
URL:            https://github.com/amkillam/ryzen_smu
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Ryzen SMU is a Linux kernel driver that exposes access to the SMU (System
Management Unit) for certain AMD Ryzen processors. It allows reading and writing
SMU mailbox commands and exposes the power metrics (PM) table via sysfs.
Use at your own risk.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -n %{modulename}-%{commit}

for kernel_version  in %{?kernel_versions} ; do
  cp -a %{modulename}-%{commit} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/%{modulename}.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modulename}.ko
done
%{?akmod_install}

%changelog
* Thu Jun 04 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package release