%global commit f883b0bca53634d7df1bbeb5e1f8ed7907d2ab74
%global shortcommit %{sub %{commit} 0 7}
%global commit_date 20220829
%global latest_stable_version 10.2.4

Name:           make-dynpart-mappings
Version:        %{latest_stable_version}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Sets up device-mapper targets for Android dynamic partitions

License:        GPL-3.0-only AND Apache-2.0
URL:            https://gitlab.com/flamingradian/make-dynpart-mappings
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch1:         0001-skip-partitions-with-no-extents.patch
Patch2:         0002-map-partitions-defined-in-later-metadata-slots.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libmd)
BuildRequires:  pkgconfig(blkid)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Android devices from Android 10 onward carve "dynamic partitions" (vendor,
system, product, odm, ...) out of a single super partition, described by
Google's liblp metadata format rather than a standard partition table.
make-dynpart-mappings reads that metadata and creates matching device-mapper
targets, so tools like msm-firmware-loader can mount those logical partitions
without needing Android's own fs_mgr.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
# To build debug packages
%set_build_flags
make %{?_smp_mflags} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
install -Dm755 make-dynpart-mappings %{buildroot}%{_bindir}/make-dynpart-mappings

%files
%license LICENSE
%doc README.md
%{_bindir}/make-dynpart-mappings

%changelog
* Tue Sep 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
