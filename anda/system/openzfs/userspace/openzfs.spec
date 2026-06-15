%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}
%global __python %{__python3}
%{!?python3_pkgversion: %global python3_pkgversion 3}
%{!?_udevdir: %global _udevdir %{_prefix}/lib/udev}
%{!?_dracutdir: %global _dracutdir %{_prefix}/lib/dracut}
%{!?_initconfdir: %global _initconfdir %{_sysconfdir}/sysconfig}
%{!?_pam_confdir: %global _pam_confdir %{_datadir}/pam-configs}
%{!?_pam_secconfdir: %global _pam_secconfdir %{_libdir}/security}
%global zfs_systemd_units zfs-import-cache.service zfs-import-scan.service zfs-mount.service zfs-share.service zfs-zed.service zfs.target zfs-import.target zfs-volume-wait.service zfs-volumes.target

Name:           openzfs
Version:        2.4.3
Release:        1%{?dist}
Summary:        OpenZFS filesystem userspace utilities
License:        CDDL-1.0
URL:            https://openzfs.org
Source0:        https://github.com/openzfs/zfs/releases/download/zfs-%{version}/zfs-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libblkid-devel
BuildRequires:  libudev-devel
BuildRequires:  openssl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libattr-devel
BuildRequires:  libaio-devel
BuildRequires:  libffi-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  python3-packaging

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:  util-linux
Requires:  sysstat
Requires:  bash-completion

Recommends:     akmod-openzfs
Conflicts:      zfs-fuse
Obsoletes:      spl < 0.8.0~

# we assume openzfs as the name for consistency, but if someone wants to install just zfs, this shows that this package provides zfs.
Provides:       zfs = %{version}-%{release}

Packager:       Willow Reed <willow@willowidk.dev>

%description
OpenZFS userspace tools

%package libs
%pkg_libs_files

%package devel
%pkg_devel_files

%prep
%autosetup -n zfs-%{version}

%build
./autogen.sh

%configure \
    --with-config=user \
    --with-python=%{__python} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --libexecdir=%{_libexecdir} \
    --sysconfdir=%{_sysconfdir} \
    --sharedstatedir=%{_sharedstatedir} \
    --localstatedir=%{_localstatedir} \
    --runstatedir=%{_runstatedir} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --datarootdir=%{_datadir} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir} \
    --with-udevdir=%{_udevdir} \
    --with-udevruledir=%{_udevrulesdir} \
    --with-dracutdir=%{_dracutdir} \
    --with-pamconfigsdir=%{_pam_confdir} \
    --with-pammoduledir=%{_pam_secconfdir} \
    --with-pkgconfigdir=%{_pkgconfigdir} \
    --with-mounthelperdir=%{_sbindir} \
    --with-systemdunitdir=%{_unitdir} \
    --with-systemdpresetdir=%{_presetdir} \
    --with-systemdmodulesloaddir=%{_modulesloaddir} \
    --with-systemdgeneratordir=%{_systemdgeneratordir} \
    --disable-sysvinit \
    --enable-pam \
    --enable-pyzfs \
    --enable-systemd \
    --disable-static

%make_build

( cd contrib/pyzfs && %py3_build )

%install
%make_install

( cd contrib/pyzfs && rm -rf %{buildroot}%{python3_sitelib} && %py3_install )

find %{buildroot} -name '*.la' -delete

%files
%doc AUTHORS COPYRIGHT LICENSE *.md
%{_sbindir}
%{_bindir}
%{_libdir}
%{_mandir}
%{_sysconfdir}/init.d
%{_sysconfdir}/zfs
%{_presetdir}/
%{_unitdir}/
%{_systemdgeneratordir}/zfs-mount-generator
%{_libdir}/udev/rules.d
%{_libdir}/udev/*_id
%{_datadir}/zfs
%{_sysconfdir}/sudoers.d/zfs
%{_sysconfdir}/sysconfig/zfs
%{bash_completions_dir}/zfs
%{bash_completions_dir}/zpool
%{python3_sitelib}
%{_libdir}/security/pam_zfs_key.so
%{_datadir}/pam-configs/zfs_key
%{_sysconfdir}/bash_completion.d/zpool

%post
%systemd_post zfs-import-cache.service
%systemd_post zfs-import-scan.service
%systemd_post zfs-mount.service
%systemd_post zfs-share.service
%systemd_post zfs-zed.service
%systemd_post zfs.target

%preun
%systemd_preun zfs-import-cache.service
%systemd_preun zfs-import-scan.service
%systemd_preun zfs-mount.service
%systemd_preun zfs-share.service
%systemd_preun zfs-zed.service
%systemd_preun zfs.target

%postun
%systemd_postun_with_restart zfs-import-cache.service
%systemd_postun_with_restart zfs-import-scan.service
%systemd_postun_with_restart zfs-mount.service
%systemd_postun_with_restart zfs-share.service
%systemd_postun_with_restart zfs-zed.service

%changelog
* Thu Jan 01 2026 Willow Reed <willow@willowidk.dev>
- Initial package
