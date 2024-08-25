Name:           cbfstool
Version:        24.08
Release:        1%?dist
Summary:        Management utility for CBFS formatted ROM images
URL:            https://doc.coreboot.org/lib/fw_config.html#cbfs
Source0:        https://github.com/coreboot/coreboot/archive/%{version}.tar.gz
License:        GPLv2
BuildRequires:  gcc g++ gcc-gnat make cmake ncurses-devel iasl 
Requires:       glibc
Packager:       Owen Zimmerman <owen@fyralabs.com>
 
%description
Management utility for CBFS formatted ROM images.
 
%prep
%autosetup -n coreboot-%version
 
%build
make -C corebook/util/cbfstool
 
%install
install -Dm 777 cbfstool %buildroot%_bindir/cbfstool

%files
/usr/bin/cbfstool

%changelog
* Sat Aug 24 2024 Owen Zimmerman <owen@fyralabs.com>
- Initial Package