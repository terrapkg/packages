%global buildforkernels akmod
%global debug_package %{nil}
%global commit e89983c628d046b2f77af3b6678cc49c2dd58332
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250521
%global modulename intel-ipu6
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
%global ver 1.0.1

Name:           %{modulename}-kmod
Summary:        Akmods module for %{modulename}
Version:        0^%{commit_date}git.%{shortcommit}
Release:        2%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{commit}/ipu6-drivers-%{shortcommit}.tar.gz
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  kmodtool
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Requires:       akmod-intel-usbio
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name} = %{commitdate}.%{shortcommit}-%{release}
Provides:       akmod-%{modulename} = %{commitdate}.%{shortcommit}-%{release}
%endif

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
This package enables the Intel IPU6 image processor.

%prep
# Error out if there was something wrong with kmodtool:
%{?kmodtool_check}
# Print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo terra --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n ipu6-drivers-%{commit}
patch -p1 -i patches/*.patch
rm -fr dkms.conf .github

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr drivers include Makefile _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) VERSION="v%{version}" modules
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    # Print out modules that are getting built:
    find _kmod_build_${kernel_version%%___*} -name "*.ko"
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 \
        _kmod_build_${kernel_version%%___*}/drivers/media/i2c/*.ko \
        _kmod_build_${kernel_version%%___*}/drivers/media/pci/intel/ipu6/psys/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
%autochangelog
