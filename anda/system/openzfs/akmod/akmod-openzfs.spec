%global buildforkernels akmod
%global debug_package %{nil}
%global modulename zfs

Name:           akmod-openzfs
Summary:        Kernel module (kmod) for OpenZFS filesystem
Version:        2.4.3
Release:        1%?dist
License:        CDDL-1.0
URL:            https://github.com/openzfs/zfs
Source0:        https://github.com/openzfs/zfs/releases/download/zfs-%{version}/zfs-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtirpc-devel
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libffi-devel
BuildRequires:  elfutils-libelf-devel

Requires:       akmods
Requires:       kernel-devel
Requires:       openzfs = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{modulename}-dkms
Conflicts:      dkms-zfs
Provides:       akmod-%{modulename} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       akmod-openzfs = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}-%{release}

Packager:       Willow Reed <willow@willowidk.dev>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
This package contains the OpenZFS kernel modules built using akmods.

%prep
%{?kmodtool_check}

kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup
for kernel_version in %{?kernel_versions} ; do
  cp -a zfs-%{version} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions} ; do
  cd _kmod_build_${kernel_version%%___*}

  ./autogen.sh

  %configure \
    --with-config=kernel \
    --with-linux=${kernel_version##*___} \
    --with-linux-obj=${kernel_version##*___}

  make %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/module modules

  cd ..
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/

 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/avl/zavl.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/nvpair/znvpair.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/unicode/zunicode.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/zcommon/zcommon.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/zstd/zzstd.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/icp/icp.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/spl/spl.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/module/zfs/zfs.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/

 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

%changelog
* Thu Jan 01 2026 Willow Reed <willow@willowidk.dev> - 2.4.0-1
- Initial package
