Name:           cbmem
Version:        24.12
Release:        1%?dist
Summary:        Prints out coreboot mem table information.
URL:            https://review.coreboot.org
License:        GPLv2
BuildRequires:  gcc g++ gcc-gnat make cmake ncurses-devel iasl git
Requires:       glibc
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Prints out coreboot mem table information in JSON by default, and also implements the basic cbmem -list and -console commands

%prep
git clone %url/coreboot.git -b %version --depth 1

%build
cd coreboot/util/cbmem
make

%install
install -Dm 777 coreboot/util/cbmem/cbmem %buildroot%_bindir/cbmem

%files
%{_bindir}/cbmem

%changelog
* Thu Feb 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
