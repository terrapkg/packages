%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}

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

Recommends:     akmod-openzfs

# we assume openzfs as the name for consistency, but if someone wants to install just zfs, this shows that this package provides zfs.
Provides:       zfs = %{version}-%{release}

Packager:       Willow Reed <willow@willowidk.dev>

%description
OpenZFS userspace tools

%package libs
Summary:        OpenZFS libraries
%description libs
Libraries for OpenZFS filesystem utilities.

%package devel
Summary:        OpenZFS development headers
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development headers for OpenZFS libraries.

%prep
%autosetup -n zfs-%{version}

%build
./autogen.sh

%configure \
    --with-config=user \
    --with-systemdunitdir=%{_unitdir} \
    --with-systemdpresetdir=%{_presetdir} \
    --with-systemdgeneratordir=%{_systemdgeneratordir} \
    --with-mounthelperdir=%{_sbindir} \
    --with-pamdir=%{_libdir}/security \
    --with-pamconfdir=%{_sysconfdir}/security \
    --with-udevdir=%{_udevrulesdir} \
    --with-pkgconfigdir=%{_libdir}/pkgconfig \
    --enable-systemd \
    --enable-pyzfs \
    --disable-static

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
???

%files libs
???

%files devel
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
