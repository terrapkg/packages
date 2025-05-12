%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif
%global ipu6_commit 1a884d5124dc149af4a645aa1493873bf796d677
%global ipu6_commitdate 20250509
%global ipu6_shortcommit %(c=%{ipu6_commit}; echo ${c:0:7})
%global usbio_commit 450939ff5f8af733bc89c564603222a4d420acf3
%global usbio_commitdate 20241210
%global usbio_shortcommit %(c=%{usbio_commit}; echo ${c:0:7})
%global modulename intel-ipu6
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
%global ver 1.0.1

Name:           %{modulename}-kmod
Summary:        Akmods module for %{modulename}
Version:        0^%{ipu6_commitdate}git.%{ipu6_shortcommit}
Release:        1%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{ipu6_commit}/ipu6-drivers-%{ipu6_shortcommit}.tar.gz
Source1:        https://github.com/intel/usbio-drivers/archive/%{usbio_commit}/usbio-drivers-%{usbio_shortcommit}.tar.gz
# Patches
# https://github.com/intel/ipu6-drivers/pull/321
Patch0:         0005-media-ipu6-Fix-out-of-tree-builds.patch
Patch20:        0010-usbio-Fix-GPIO-and-I2C-driver-modaliases.patch
# https://github.com/intel/usbio-drivers/pull/34
Patch21:        0011-usbio-Fix-I2C-max-transfer-size.patch
Patch22:        0012-usbio-Use-MAX_PAYLOAD_BSIZE-in-usbio_bulk_write.patch
# Downstream/Fedora specific patches
Patch101:       0101-Fedora-local-mod-integrate-usbio-drivers-within-ipu6.patch
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  kmodtool
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name} = %{ipu6_commitdate}.%{ipu6_shortcommit}-%{release}
Provides:       akmod-%{modulename} = %{ipu6_commitdate}.%{ipu6_shortcommit}-%{release}
%endif

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
This package enables the Intel IPU6 image processor.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu} --repo terra --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -a 1
(cd ipu6-drivers-%{ipu6_commit}
%patch 0 -p1
%patch 101 -p1
patch -p1 < patches/0001-v6.10-IPU6-headers-used-by-PSYS.patch
)
(cd usbio-drivers-%{usbio_commit}
%patch 20 -p1
%patch 21 -p1
%patch 22 -p1
)

cp -Rp usbio-drivers-%{usbio_commit}/drivers ipu6-drivers-%{ipu6_commit}/
cp -Rp usbio-drivers-%{usbio_commit}/include ipu6-drivers-%{ipu6_commit}/

for kernel_version in %{?kernel_versions} ; do
  cp -a ipu6-drivers-%{ipu6_commit}/ _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions} ; do
  make -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/media/i2c/
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/media/pci/intel/ipu6/psys/
  install -m 755 _kmod_build_${kernel_version%%___*}/drivers/media/i2c/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/media/i2c/
  install -m 755 _kmod_build_${kernel_version%%___*}/drivers/media/pci/intel/ipu6/psys/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/drivers/media/pci/intel/ipu6/psys/
  install -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
done
%{?akmod_install}

%changelog
%autochangelog
