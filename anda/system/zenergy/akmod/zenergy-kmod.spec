# The reason why this package is a separate from the main one despite using the same sources
# is because akmods use the srpm to build the kmod package, and if the kmod package is included
# in the main package, akmods will reinstall the userspace package every time the kernel is updated.

%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%global commit 58f2fda7184fbde95033f492f7c54990552ef86f
%global commitdate 20250831
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global modulename zenergy

Name:           %{modulename}-kmod
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware monitor (HWMON) sysfs interface.
License:        GPL-2.0
URL:            https://github.com/BoukeHaarsma23/zenergy
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
# AMD only makes x86_64 CPUs, They literally invented x86_64.
BuildArch:      x86_64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Requires:       help2man
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}
Packager:       Cappy Ishihara <cappy@fyralabs.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Based on AMD_ENERGY driver, but with some jiffies added so non-root users can read it safely.
Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs)
via the hardware monitor (HWMON) sysfs interface.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -n %{modulename}-%{commit}

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \+

for kernel_version  in %{?kernel_versions} ; do
  cp -a %{modulename}-%{commit} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/zenergy.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/zenergy.ko
done
%{?akmod_install}

%changelog
%autochangelog
