%global dkmsname dkms-%{name}

%global rpm_dkms_opt 1

# Set up kmod packaging for RHEL
%if 0%{?rhel} >= 8
%global kmodname %{name}-kmod
# Because Red Hat broke this macro by not including kernel-rpm-macros in the base buildroot
%global kernel_module_package_buildreqs kernel-devel kernel-abi-stablelists redhat-rpm-config kernel-rpm-macros elfutils-libelf-devel kmod
%endif

%global _udevdir %{_prefix}/lib/udev

# dracut directory path
%global _dracutdir  %{_prefix}/lib/dracut

# initramfs-tools directory path
%global _initramfstoolsdir %{_datadir}/initramfs-tools

# default _initconfdir
%global _initconfdir %{_sysconfdir}/sysconfig

# Units to manage for systemd configuration
%global zfs_systemd_units zfs-import-cache.service zfs-import-scan.service zfs-mount.service zfs-share.service zfs-zed.service zfs.target zfs-import.target zfs-volume-wait.service zfs-volumes.target

# zfs configure common options
%global zfs_common_configure_opts \\\
	   --with-python=%{__python3} --with-udevdir=%{_udevdir} --with-udevruledir=%{_udevrulesdir} \\\
	   --with-systemdunitdir=%{_unitdir} --with-systemdpresetdir=%{_presetdir} \\\
	   --with-systemdmodulesloaddir=%{_modulesloaddir} --with-systemdgeneratordir=%{_systemdgeneratordir} \\\
	   --with-dracutdir=%{_dracutdir} --with-mounthelperdir=%{_sbindir} --with-pammoduledir=%{_libdir}/security \\\
	   --disable-static --disable-sysvinit --enable-pam --enable-systemd \\\
	   %{nil}

# Set up the correct PAM module name, following proper conventions
%global pamzfs pam_zfs

# library names
%global zfs_sover 4
%global libname_zfs libzfs%{zfs_sover}

# Not a stable library yet
%global zfscore_sover 3
%global libname_zfscore libzfs_core%{zfscore_sover}

%global zpool_sover 6
%global libname_zpool libzpool%{zpool_sover}

%global zfsbootenv_sover 1
%global libname_zfsbootenv libzfsbootenv%{zfsbootenv_sover}

%global spl_sover 3
%global libname_nvpair libnvpair%{spl_sover}
%global libname_uutil libuutil%{spl_sover}

%if "%{_vendor}" == "debbuild"
%global devsuffix dev
%else
%global devsuffix devel
%endif

# development library names
%global devname_zfs libzfs-devel
%global devname_zfsbootenv libzfsbootenv-devel
%global devname_zpool libzpool-devel
%global devname_nvpair libnvpair-devel
%global devname_uutil libuutil-devel

%{!?python3_pkgversion: %global python3_pkgversion 3}

# kmod install path
%define _kmod_src_root %{_usrsrc}/%{name}-%{version}


Name:           zfs
Version:        2.4.3
Release:        1%{?dist}
Summary:        OpenZFS for Linux
License:        CDDL-1.0
URL:            http://zfsonlinux.org/
Source0:        https://github.com/openzfs/zfs/releases/download/zfs-%{version}/zfs-%{version}.tar.gz
# For kmod packaging
Source10:       kmod-%{name}.spec-preamble

ExclusiveArch:  %{ix86} x86_64 aarch64

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  python%{python3_pkgversion}-devel >= 3.6
BuildRequires:  python%{python3_pkgversion}-cffi
BuildRequires:  python%{python3_pkgversion}-packaging

BuildRequires:  libaio-devel
BuildRequires:  libblkid-devel
BuildRequires:  libattr-devel
BuildRequires:  zlib-devel
BuildRequires:  libuuid-devel
BuildRequires:  libudev-devel
BuildRequires:  pam-devel
BuildRequires:  openssl-devel
BuildRequires:  libtirpc-devel

# So that the autofoo can detect systemd properly
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

Requires:       %{libname_zpool}%{?_isa} = %{version}-%{release}
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_uutil}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zfs}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zfsbootenv}%{?_isa} = %{version}-%{release}

# zfs-fuse provides the same commands and man pages that ZoL does. Renaming
# those on either side would conflict with all available documentation.
Conflicts:      zfs-fuse

# For bash completion
Requires:       bash-completion

# SPL has been integrated into the ZoL sources
Obsoletes:        spl < 0.8.0~

%if 0%{?rhel} >= 8
# RHEL kernel build
BuildRequires:  kernel-rpm-macros
BuildRequires:  %kernel_module_package_buildreqs
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{kmodname} = %{version}-%{release}
%{?kernel_module_package:%kernel_module_package -n %{name} -p %{S:10}}
%else
Requires:       %{dkmsname} = %{version}-%{release}
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
ZFS is an advanced file system and volume manager
which was originally developed for Solaris and
is now maintained by the OpenZFS community.

%package kmod-common
Summary:        Kernel module common files for %{name}
# ZFS modules are CDDL and SPL modules are GPLv2+
License:        CDDL-1.0 and GPL-2.0-or-later
BuildArch:      noarch

%description kmod-common
This package contains the common kernel module files
for OpenZFS on Linux.

%package -n %{dkmsname}
Summary:        Kernel module sources for %{name} managed by DKMS
# ZFS modules are CDDL and SPL modules are GPLv2+
License:        CDDL-1.0 and GPL-2.0-or-later
BuildArch:      noarch
# elfutils' libelf is required now for newer kernels
Requires:       elfutils-libelf-devel
Requires:       diffutils
Requires:       dkms >= 2.2.0.3
Requires:       gcc
Requires:       make
Requires:       perl
Requires:       python%{python3_pkgversion}

Provides:       %{name}-kmod = %{version}-%{release}
Requires:       %{name}-kmod-common = %{version}-%{release}
RemovePathPostfixes: .dkms

%description -n %{dkmsname}
This package contains the kernel module sources for
OpenZFS for Linux that is managed by DKMS.

%package -n %{libname_zpool}
Summary:        Native ZFS pool library for Linux
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zfs}%{?_isa} = %{version}-%{release}

%description -n %{libname_zpool}
This package contains the zpool library, which provides support
for managing zpools

%post -n %{libname_zpool}
/sbin/ldconfig

%postun -n %{libname_zpool}
/sbin/ldconfig

%package -n %{libname_zfsbootenv}
Summary:        Native ZFS boot environment library for Linux
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zfs}%{?_isa} = %{version}-%{release}

%description -n %{libname_zfsbootenv}
This package contains the zfsbootenv library, which provides support
for managing zfs boot environments

%post -n %{libname_zfsbootenv}
/sbin/ldconfig

%postun -n %{libname_zfsbootenv}
/sbin/ldconfig

%package -n %{libname_nvpair}
Summary:        Solaris name-value library for Linux

%description -n %{libname_nvpair}
This package contains routines for packing and unpacking name-value
pairs.  This functionality is used to portably transport data across
process boundaries, between kernel and user space, and can be used
to write self describing data structures on disk.

%post -n %{libname_nvpair}
/sbin/ldconfig

%postun -n %{libname_nvpair}
/sbin/ldconfig

%package -n %{libname_uutil}
Summary:        Solaris userland utility library for Linux

%description -n %{libname_uutil}
This library provides a variety of compatibility functions for OpenZFS on Linux:
 * libspl: The Solaris Porting Layer userland library, which provides APIs
   that make it possible to run Solaris user code in a Linux environment
   with relatively minimal modification.
 * libavl: The Adelson-Velskii Landis balanced binary tree manipulation
   library.
 * libefi: The Extensible Firmware Interface library for GUID disk
   partitioning.
 * libshare: NFS, SMB, and iSCSI service integration for ZFS.

%post -n %{libname_uutil}
/sbin/ldconfig

%postun -n %{libname_uutil}
/sbin/ldconfig

%package -n %{libname_zfs}
Summary:        Native ZFS filesystem library for Linux
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_uutil}%{?_isa} = %{version}-%{release}

%description -n %{libname_zfs}
This package provides support for managing ZFS filesystems

%post -n %{libname_zfs}
/sbin/ldconfig

%postun -n %{libname_zfs}
/sbin/ldconfig

%package -n %{devname_zfs}
Summary:        Development headers
Provides:       %{devname_zpool}%{?_isa}
Provides:       %{devname_zfsbootenv}%{?_isa}
Provides:       %{devname_nvpair}%{?_isa}
Provides:       %{devname_uutil}%{?_isa}
Requires:       %{libname_zfs}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zpool}%{?_isa} = %{version}-%{release}
Requires:       %{libname_zfsbootenv}%{?_isa} = %{version}-%{release}
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_uutil}%{?_isa} = %{version}-%{release}

%description -n %{devname_zfs}
This package contains the header files needed for building additional
applications against the ZFS libraries.

%package -n %{pamzfs}
Summary:        PAM module for encrypting/decrypting datasets
Requires:       %{libname_zfs}%{?_isa} = %{version}-%{release}
Requires:       %{libname_nvpair}%{?_isa} = %{version}-%{release}
Requires:       %{libname_uutil}%{?_isa} = %{version}-%{release}

%description -n %{pamzfs}
This package contains the PAM module for encrypting and decrypting
ZFS datasets automatically using user login credentials.

%package test
Summary:        Test infrastructure
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       parted
Requires:       lsscsi
Requires:       mdadm
Requires:       bc
Requires:       ksh
Requires:       fio
Requires:       acl
Requires:       sudo
Requires:       sysstat
Requires:       rng-tools

%description test
This package contains test infrastructure and support scripts for
validating the file system.

%package dracut
Summary:        Dracut module
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dracut
Requires:       gawk
Requires:       grep

%description dracut
This package contains a dracut module used to construct an initramfs
image which is ZFS aware.

%prep
%autosetup


%build
# Embed downstream version in module
sed -e 's/^Version:.*/Version:      %{version}/' -e 's/^Release:.*/Release:      %{release}/' -i.orig META

%if 0%{?rhel} >= 8
# Kernel build for RHEL
for flavor in %{flavors_to_build}; do
	cp -a ../%{name}-%{version} ../%{name}-%{version}-kmodbuild-$flavor
	pushd ../%{name}-%{version}-kmodbuild-$flavor
	autoreconf -fiv
	%configure --with-config=kernel --with-linux="%{kernel_source $flavor}" %{zfs_common_configure_opts}
	%make_build
	popd
done
%endif

scripts/dkms.mkconf -n %{name} -v %{version} -f dkms.conf
autoreconf -fiv
%configure --with-config=user %{zfs_common_configure_opts}
%make_build

%install
INITIAL_ENVDIR=`pwd`

%if 0%{?rhel} >= 8
for flavor in %{flavors_to_build}; do
	pushd ../%{name}-%{version}-kmodbuild-$flavor
	%make_install
	popd
done
# Kill unneeded files installed into /usr/src
rm -rf %{buildroot}%{_usrsrc}/*
%endif

%make_install

# Kill all libtool .la files
find %{buildroot} -name '*.la' -print -delete

# Create source tree
make distdir

# Erase unnecessary bits from sources being installed for dkms module to save space
# Note that 0h25 is percent sign
cd %{name}-%{version}
for file in $(find cmd dracut etc lib man rpm udev tests -type f); do \
    rm "$file"; \
    test "$file" != "${file%%.in}" && printf "\x25:\n\t#\n" > "$file"; \
    true; \
done

cd $INITIAL_ENVDIR

printf "#!/bin/sh\ncp \"$@\"\n" > %{name}-%{version}/cp
chmod 755 %{name}-%{version}/cp

# Install kernel sources
mkdir -p %{buildroot}%{_usrsrc}
mv %{name}-%{version} %{buildroot}%{_kmod_src_root}.dkms
cp dkms.conf %{buildroot}%{_kmod_src_root}.dkms

# Erase initramfs-tools on non-Debian
rm -rf %{buildroot}%{_initramfstoolsdir}

# Erase pam-configs on non-Debian
rm -rf %{buildroot}%{_datadir}/pam-configs

# Erase unused init files
rm -rf %{buildroot}%{_initconfdir}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/
rmdir %{buildroot}%{_sysconfdir}/bash_completion.d

%preun -n %{dkmsname}
if [  "$(dkms status -m %{name} -v %{version})" ]; then
   dkms remove -m %{name} -v %{version} --all %{?rpm_dkms_opt:--rpm_safe_upgrade}
fi

%post -n %{dkmsname}
if [ "$1" -ge "1" ]; then
   if [ -f /usr/lib/dkms/common.postinst ]; then
      /usr/lib/dkms/common.postinst %{name} %{version}
      exit $?
   fi
fi

%post
%systemd_post %{zfs_systemd_units}

%preun
%systemd_preun %{zfs_systemd_units}

%postun
%systemd_postun %{zfs_systemd_units}

%files
%license COPYRIGHT LICENSE NOTICE
%doc AUTHORS README.md
%{_bindir}/*
%{_libexecdir}/zfs/zed.d
%{_libexecdir}/zfs/zfs_prepare_disk
%{_libexecdir}/zfs/zpool.d
%{_libexecdir}/zfs/zpool_influxdb
%{_mandir}/man1/*.1.*
%{_mandir}/man4/*.4.*
%{_mandir}/man5/*.5.*
%{_mandir}/man7/*.7.*
%{_mandir}/man8/*.8.*
%{_udevdir}/vdev_id
%{_udevdir}/zvol_id
%{_udevrulesdir}/*
%{_modulesloaddir}/*
%{_unitdir}/*
%{_presetdir}/*
%{_systemdgeneratordir}/*
%dir %{_sysconfdir}/zfs
%dir %{_sysconfdir}/zfs/zed.d
%dir %{_sysconfdir}/zfs/zpool.d
%config(noreplace) %{_sysconfdir}/zfs/zfs-functions
%config(noreplace) %{_sysconfdir}/zfs/*.example
%config(noreplace) %{_sysconfdir}/zfs/zed.d/*
%config(noreplace) %{_sysconfdir}/zfs/zpool.d/*
%{_datadir}/bash-completion/completions/zfs

%files -n %{pamzfs}
%license COPYRIGHT LICENSE NOTICE
%{_libdir}/security/*

%files -n %{libname_zpool}
%license COPYRIGHT LICENSE NOTICE
%{_libdir}/libzpool.so.%{zpool_sover}
%{_libdir}/libzpool.so.%{zpool_sover}.*

%files -n %{libname_zfsbootenv}
%license COPYRIGHT LICENSE NOTICE
%{_libdir}/libzfsbootenv.so.%{zfsbootenv_sover}
%{_libdir}/libzfsbootenv.so.%{zfsbootenv_sover}.*

%files -n %{libname_nvpair}
%license COPYRIGHT LICENSE NOTICE
%{_libdir}/libnvpair.so.%{spl_sover}
%{_libdir}/libnvpair.so.%{spl_sover}.*

%files -n %{libname_uutil}
%license COPYRIGHT LICENSE NOTICE
%{_libdir}/libuutil.so.%{spl_sover}
%{_libdir}/libuutil.so.%{spl_sover}.*

%files -n %{libname_zfs}
%license COPYRIGHT LICENSE NOTICE
%license lib/libzfs/THIRDPARTYLICENSE.*
%{_libdir}/libzfs.so.%{zfs_sover}
%{_libdir}/libzfs.so.%{zfs_sover}.*
%{_libdir}/libzfs_core.so.%{zfscore_sover}
%{_libdir}/libzfs_core.so.%{zfscore_sover}.*

%files -n %{devname_zfs}
%license COPYRIGHT LICENSE NOTICE
%doc AUTHORS README.md
%{_libdir}/pkgconfig/libzfs.pc
%{_libdir}/pkgconfig/libzfs_core.pc
%{_libdir}/pkgconfig/libzfsbootenv.pc
%{_libdir}/*.so
%{_includedir}/*

%files kmod-common
%license COPYRIGHT LICENSE NOTICE
%license module/icp/algs/skein/THIRDPARTYLICENSE*
%license module/icp/asm-x86_64/aes/THIRDPARTYLICENSE*
%license module/os/linux/spl/THIRDPARTYLICENSE*
%license module/zfs/THIRDPARTYLICENSE*
%doc AUTHORS README.md

%files -n %{dkmsname}
%{_kmod_src_root}.dkms

%files test
%{_datadir}/%{name}

%files dracut
%doc contrib/dracut/README.md
%{_dracutdir}/modules.d/*

%changelog
* Mon Jun 15 2026 Cypress Reed <cypress@fyralabs.com>
- Port to Terra from https://codeberg.org/Conan_Kudo/openzfs-linux-packaging/src/branch/main

* Sat Dec 02 2023 Neal Gompa <neal@gompa.dev> - 2.2.2
- Update to 2.2.2

* Wed Nov 22 2023 Neal Gompa <neal@gompa.dev> - 2.2.1
- Update to 2.2.1

* Sun Oct 29 2023 Neal Gompa <neal@gompa.dev> - 2.2.0
- Rebase to 2.2.0
- Switch fully to SPDX license identifiers

* Tue May 16 2023 Neal Gompa <neal@gompa.dev> - 2.1.11
- Upgrade to 2.1.11

* Tue Oct 04 2022 Neal Gompa <ngompa@datto.com> - 2.1.6
- Upgrade to 2.1.6

* Sun Jul 10 2022 Neal Gompa <ngompa@datto.com> - 2.1.5
- Upgrade to 2.1.5

* Sat May 21 2022 Neal Gompa <ngompa@datto.com> - 2.1.4
- Upgrade to 2.1.4
- Simplify scriptlets

* Wed Dec 29 2021 Neal Gompa <ngompa@datto.com> - 2.1.2
- Upgrade to 2.1.2

* Thu Sep 30 2021 Neal Gompa <ngompa@datto.com> - 2.1.1
- Upgrade to 2.1.1

* Sun Jul 11 2021 Neal Gompa <ngompa@datto.com> - 2.1.0
- Rebase to 2.1.0
- Build pam module

* Wed Oct 07 2020 Neal Gompa <ngompa@datto.com> - 0.8.5
- Upgrade to 0.8.5

* Wed Jul 08 2020 Neal Gompa <ngompa@datto.com> - 0.8.4
- Rebase to 0.8.4
- Sync packaging changes from upstream rpm packaging
- Merge changes from 0.7.x packaging
- Drop all non-systemd support and distros associated with it
- Add kmod build for CentOS 8

* Sat Apr 27 2019 Neal Gompa <ngompa@datto.com> - 0.8.0~rc4
- Upgrade to 0.8.0-rc4

* Mon Jan 14 2019 Neal Gompa <ngompa@datto.com> - 0.8.0~rc3
- Upgrade to 0.8.0-rc3
- Sync packaging changes from upstream rpm packaging
- Build pyzfs bindings for Python 3

* Thu Nov 29 2018 Neal Gompa <ngompa@datto.com> - 0.8.0~rc2
- Upgrade to 0.8.0-rc2
- Sync packaging changes from upstream rpm packaging
- Add and document SPL licensing for dkms package

* Fri Sep 14 2018 Neal Gompa <ngompa@datto.com> - 0.8.0~rc1
- Rebase to 0.8.0-rc1
- Drop requirement on spl as it was merged into zfs
- Obsolete spl packages

* Thu Jul 06 2017 Neal Gompa <ngompa@datto.com> - 0.7.0~rc4
- Upgrade to 0.7.0-rc4

* Tue Apr 18 2017 Neal Gompa <ngompa@datto.com> - 0.7.0~rc3
- Upgrade to 0.7.0-rc3

* Mon Oct 31 2016 Neal Gompa <ngompa@datto.com> - 0.7.0~rc2
- Upgrade to 0.7.0-rc2

* Sat Oct 29 2016 Neal Gompa <ngompa@datto.com> - 0.6.5.8
- Set the correct relationship for zfs-dkms for Debian/Ubuntu
- Do not version the conflicts with Debian/Ubuntu packages

* Fri Oct 28 2016 Neal Gompa <ngompa@datto.com> - 0.6.5.8
- Ensure all services are processed with preset configuration on systemd

* Wed Oct 26 2016 Neal Gompa <ngompa@datto.com> - 0.6.5.8
- Strengthen the obsoletion of packages for Debian/Ubuntu

* Tue Oct 25 2016 Neal Gompa <ngompa@datto.com> - 0.6.5.8
- Redefine libexecdir for Debian/Ubuntu
- Further define /etc/zfs in file lists

* Thu Sep 29 2016 Neal Gompa <ngompa@datto.com> - 0.6.5.8
- Initial packaging
