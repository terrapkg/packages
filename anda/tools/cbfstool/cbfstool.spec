Name:           cbfstool
Version:        24.08
Release:        1%?dist
Summary:        Management utility for CBFS formatted ROM images
URL:            https://doc.coreboot.org/lib/fw_config.html#cbfs
License:        GPLv2
BuildRequires:  gcc g++ gcc-gnat make cmake ncurses-devel iasl git
Requires:       glibc
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Management utility for CBFS formatted ROM images.

%prep
git clone https://review.coreboot.org/coreboot.git -b %version

%build
make -C coreboot/util/cbfstool

%install
install -Dm 777 coreboot/util/cbfstool/cbfstool %buildroot%_bindir/cbfstool

%files
/usr/bin/cbfstool

%changelog
* Sun Aug 25 2024 Owen Zimmerman <owen@fyralabs.com>
- Initial Package