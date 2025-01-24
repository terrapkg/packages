%global commit0 aecec2aaef069fea56aa921cf5d7e449bb7a0b82
%global date 20240624
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 a6dccbbf5a955489d20d996234b6ebb481183ed7
%global date 20240416
%global shortcommit1 %(c=%{commit0}; echo ${c:0:7})
%define buildforkernels akmod
%global debug_package %{nil}
%global realname intel-ipu6

Name:           %{realname}-kmod
Version:        %{date}.%{shortcommit0}
Release:        1%{?dist}
Summary:        Kernel drivers for the IPU 6 and sensors
License:        GPL-3.0-only
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{commit0}.tar.gz#/ipu6-drivers-%{shortcommit0}.tar.gz
Source1:        https://github.com/intel/ivsc-driver/archive/%{commit1}.tar.gz#/ivsc-driver-%{shortcommit1}.tar.gz
### intel/ipu6-drivers | PR #214 | Ipu6-isys probe improvements
## https://github.com/intel/ipu6-drivers/pull/214
Patch0:         0000-probe-improvements.patch
### intel/ipu6-drivers | PR #239 | gc5035: Fix compilation with kernels >= 6.8
## https://github.com/intel/ipu6-drivers/pull/239
Patch1:         0001-fix-compilation-6.8.patch
### intel/ipu6-drivers | PR #242 | media: ipu6: Fix compilation with kernels >= 6.10
## https://github.com/intel/ipu6-drivers/pull/242
Patch2:         0002-fix-compilation-6.10.patch
### intel-ipu6-drivers | PR #243 | Rename ipu6 .ko files to avoid conflict with upstream ipu6 isys support
## https://github.com/intel/ipu6-drivers/pull/243
Patch3:         0003-prefix-modules.patch
### intel/ipu6-drivers | PR #261 | media: ipu6: Fix compilation with kernels >= 6.11
## https://github.com/intel/ipu6-drivers/pull/261
Patch4:         0004-fix-compilation-6.11.patch
### intel/ipu6-drivers | PR #283 | media: ipu6: Fix compilation with kernels >= 6.12
## https://github.com/intel/ipu6-drivers/pull/283
Patch5:         0005-fix-compilation-6.12.patch
Patch6:         0006-fix-compilation-6.12-no-no_llseek.patch
### jwrdegoede/ipu6-drivers | Commit 2c4ad13 | Makefile: Adjust which modules to build for which kernel-versions for Fedora
## https://github.com/jwrdegoede/ipu6-drivers/commit/2c4ad1398dddfb307e8a40a714a6d5f70d6d14cb
Patch7:         0007-modules-per-kernel.patch
BuildRequires:  gcc
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kmodtool

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{realname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"}) }

%description
Kernel drivers for Intel iVSC, IPU 6, and sensors.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu} --repo terra --kmodname %{realname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"}

%autosetup -p1 -n ipu6-drivers-%{commit0} -a 1

cp -av ivsc-driver-%{commit1}/{backport-include,drivers,include} .
rm -fr intel-vsc-%{commit1}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr backport-include drivers include Makefile _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) VERSION="v%{version}" modules
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 \
        _kmod_build_${kernel_version%%___*}/*.ko \
        _kmod_build_${kernel_version%%___*}/drivers/media/i2c/*.ko \
        _kmod_build_${kernel_version%%___*}/drivers/media/pci/intel/ipu6/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

### Reloading the modules is needed for %{PATCH0} to take effect properly on some kernels, as well for the changes to be properly reverted on uninstall.
## See: https://github.com/intel/ipu6-drivers/pull/214#issuecomment-1986110818
%post
/usr/sbin/rmmod -f intel_ipu6_psys intel_ipu6_isys intel_ipu6
/usr/sbin/modprobe -a intel_ipu6 intel_ipu6_isys intel_ipu6_psys

%postun
/usr/sbin/rmmod -f intel_ipu6_psys intel_ipu6_isys intel_ipu6
/usr/sbin/modprobe -a intel_ipu6 intel_ipu6_isys intel_ipu6_psys

%changelog
%autochangelog
