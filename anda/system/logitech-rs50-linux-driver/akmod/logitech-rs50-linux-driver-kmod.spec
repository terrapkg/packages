# The reason why this package is a separate from the main one despite using the same sources
# is because akmods use the srpm to build the kmod package, and if the kmod package is included
# in the main package, akmods will reinstall the userspace package every time the kernel is updated.

%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

%global commit 34eb21e66a687ea8961f185ecd54bc7e7edae0f8
%global commitdate 20260407
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global modulename logitech-rs50-linux-driver

Name:           %{modulename}-kmod
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276)
License:        GPL-2.0-only
URL:            https://github.com/mescon/logitech-rs50-linux-driver
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
BuildArch:      x86_64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276).
This is a patched version of the hid-logitech-hidpp driver that adds RS50 support with force feedback (FF_CONSTANT) and exposes all G Hub settings via sysfs for runtime configuration.
Note: This driver replaces the in-kernel hid-logitech-hidpp module and continues to support all other Logitech HID++ devices (mice, keyboards, other racing wheels like the G29, G920, G923, etc.).

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -n %{modulename}-%{commit}

mv %{modulename}-%{commit}/mainline/* %{modulename}-%{commit}/

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
 install -D -m 755 _kmod_build_${kernel_version%%___*}/hid-logitech-hidpp.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/hid-logitech-hidpp.ko
done
%{?akmod_install}

%changelog
%autochangelog
