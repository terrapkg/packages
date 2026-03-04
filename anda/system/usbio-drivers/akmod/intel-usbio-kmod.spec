%global buildforkernels akmod
%global debug_package %{nil}
%global commit ee221ecae757d43ab3fb39433f389373b2026109
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251031
%global modulename intel-usbio

Name:           %{modulename}-kmod
Summary:        Kernel drivers for the USBIO Extension
Version:        0^%{commit_date}git.%{shortcommit}
Release:        3%{?dist}
License:        GPL-2.0-only
URL:            https://github.com/intel/usbio-drivers
Source0:        %{url}/archive/%{commit}.tar.gz#/usbio-drivers-%{shortcommit}.tar.gz
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  kmodtool
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Requires:       akmod-intel-ipu6
Packager:       Gilver E. <roachy@fyralabs.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
This package enables USBIO Extension drivers on Intel Alder Lake, Raptor Lake, Meteor Lake and Lunar Lake platforms.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n usbio-drivers-%{commit}
rm -fr .github

for kernel_version in %{?kernel_versions} ; do
  cp -a ./* _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions} ; do
  make -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/gpio/
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/i2c/busses/
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/mfd/
  install -m 755 _kmod_build_${kernel_version%%___*}/drivers/gpio/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/gpio/
  install -m 755 _kmod_build_${kernel_version%%___*}/drivers/i2c/busses/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/i2c/busses/
  install -m 755 _kmod_build_${kernel_version%%___*}/drivers/mfd/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/mfd/
  install -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
done
%{?akmod_install}

%changelog
* Mon Jun 16 2025 Gilver E. <rockgrub@disroot.org> - 0^20250312git4fb690c
- Initial package
