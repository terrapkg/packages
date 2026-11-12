Name:           zlib
Version:        1.4
Release:        2%{?dist}
License:        Zlib
URL:            https://zlib.net
Source:         https://github.com/madler/zlib/archive/v%{version}.tar.gz
Summary:        A massively spiffy yet delicately unobtrusive compression library
Conflicts:      zlib-ng-compat

BuildRequires:  gcc

%description
%summary.

%package devel
Requires:       %{name}%{?_isa} = %{evr}
%pkg_devel_files

%package static
%pkg_static_files

%prep
%autosetup

%conf
%configure

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
* Mon Nov 9 2026 Cypress Reed <cypress@fyralabs.com> - 1.4-2
- Make zlib-devel require the matching zlib, so libz.so isn't left dangling

* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.3.2-2
- Update packager

* Tue Apr 21 2026 Owen Zimmerman <owen@fyralabs.com>
- Use %conf and %configure

* Wed Nov 26 2025 Olivia <git@olivia.sh>
- package zlib
