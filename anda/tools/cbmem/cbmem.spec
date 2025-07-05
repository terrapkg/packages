%define debug_package %nil

Name:           cbmem
Version:        25.06
Release:        1%?dist
Summary:        Prints out coreboot mem table information
URL:            https://review.coreboot.org
License:        BSD-3-Clause AND Apache-2.0 AND CC-BY-SA-3.0 AND GPL-2.0-only AND GPL-3.0-or-later AND ISC AND BSD-2-Clause-Patent AND BSD-4-Clause-UC AND CC-PDDC AND GPL-2.0-or-later AND HPND-sell-varient AND LGPL-2.1-or-later AND BSD-2-Clause AND CC-BY-4.0 AND GPL-3.0-only AND HPND AND X11 AND MIT 
BuildRequires:  gcc g++ make cmake ncurses-devel iasl git anda-srpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Prints out coreboot mem table information in JSON by default, and also implements the basic cbmem -list and -console commands.

%prep
%git_clone %url/coreboot %version

%build
cd util/cbmem
%make_build CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS"

%install
install -Dm 755 util/cbmem/cbmem %buildroot%_bindir/cbmem

%files
%doc util/cbmem/description.md
%license LICENSES/*
%{_bindir}/cbmem

%changelog
* Sun Jun 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
