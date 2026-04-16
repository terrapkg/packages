%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}
%global __python %{__python3}

Name:           openzfs
Version:        2.4.0
Release:        1%?dist
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
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:  util-linux
Requires:  sysstat

Recommends:     akmod-openzfs

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
    --with-udevdir=%{_udevdir} \
    --with-udevruledir=%{_udevrulesdir} \
    --with-dracutdir=%{_dracutdir} \
    --with-pamconfigsdir=%{_datadir}/pam-configs \
    --with-pammoduledir=%{_libdir}/security \
    --with-python=%{__python} \
    --with-pkgconfigdir=%{_pkgconfigdir} \
    --with-mounthelperdir=%{_sbindir} \
    --disable-static \
    %{debug} \
    %{debuginfo} \
    %{asan} \
    %{ubsan} \
    %{systemd} \
    %{pam} \
    %{pyzfs}

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
???

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
* Thu Jan 01 2026 Willow Reed <willow@willowidk.dev> - 2.4.0-1
- Initial package
