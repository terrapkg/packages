%define debug_package %nil
%global build_cflags %__build_flags_lang_c %?_distro_extra_cflags -std=c17

Name:           cbmem
Version:        24.12
Release:        1%?dist
Summary:        Prints out coreboot mem table information
URL:            https://review.coreboot.org
License:        BSD-3-Clause
BuildRequires:  gcc g++ gcc-gnat make cmake ncurses-devel iasl git anda-srpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Prints out coreboot mem table information in JSON by default, and also implements the basic cbmem -list and -console commands.

%prep
%git_clone %url/coreboot %version

%build
cd util/cbmem
%make_build -std=c17

%install
install -Dm 755 util/cbmem/cbmem %buildroot%_bindir/cbmem

%files
%{_bindir}/cbmem

%changelog
* Thu Feb 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
