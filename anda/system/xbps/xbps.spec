%global _distro_extra_cflags -Wno-discarded-qualifiers

Name:           xbps
Version:        0.60.7
Release:        1%?dist
License:        BSD-2-Clause AND BSD-3-Clause AND ISC
Summary:        A binary package system designed and implemented from scratch
URL:            https://github.com/void-linux/xbps
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
Packager:       Metcya <metcya@gmail.com>

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(pkgconf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libarchive) >= 3.3.3
Requires:       %name-lib = %evr

%pkg_completion -B xbps xbps-checkvers xbps-create xbps-dgraph xbps-install xbps-pkgdb xbps-query xbps-reconfigure xbps-remove xbps-rindex
%pkg_completion -z xbps xbps_src

%description
The X Binary Package System (in short XBPS) is a binary package system designed
and implemented from scratch. Its goal is to be fast, easy to use, bug-free,
featureful and portable as much as possible.

%package libs
%pkg_libs_files

%package static
%pkg_static_files

%package devel
%pkg_devel_files

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE LICENSE.3RDPARTY
%doc README.md NEWS 3RDPARTY AUTHORS
%_bindir/xbps-alternatives
%_bindir/xbps-checkvers
%_bindir/xbps-create
%_bindir/xbps-dgraph
%_bindir/xbps-digest
%_bindir/xbps-fbulk
%_bindir/xbps-fetch
%_bindir/xbps-install
%_bindir/xbps-pkgdb
%_bindir/xbps-query
%_bindir/xbps-reconfigure
%_bindir/xbps-remove
%_bindir/xbps-rindex
%_bindir/xbps-uchroot
%_bindir/xbps-uhelper
%_bindir/xbps-uunshare
%_datadir/%name.d/00-repository-main.conf
%_datadir/%name.d/%name.conf
%_mandir/man1/*.1.*
%_mandir/man5/*.5.*
%_mandir/man7/*.7.*
/var/db/%name/keys/*.plist

%changelog
* Fri Dec 12 2025 Metcya <metcya@gmail.com> - 0.60.6
- package xbps
