Name:           zlib
Version:        1.3.2
Release:        1%?dist
License:        Zlib
URL:            https://zlib.net
Source:         https://github.com/madler/zlib/archive/v%{version}.tar.gz
Summary:        A massively spiffy yet delicately unobtrusive compression library
Conflicts:      zlib-ng-compat

BuildRequires:  gcc

%description
%summary.

%package devel
%pkg_devel_files

%package static
%pkg_static_files

%prep
%autosetup 
export CFLAGS="%optflags"
export LDFLAGS="%build_ldflags"
./configure --libdir=%_libdir \
            --includedir=%_includedir \
            --sysconfdir=%_sysconfdir \
            --localstatedir=%_localstatedir \
            --prefix=%_prefix

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README 
%_mandir/man3/zlib.3.*
%_libdir/libz.so.*

%changelog
* Wed Nov 26 2025 metcya <metcya@gmail.com>
- package zlib
