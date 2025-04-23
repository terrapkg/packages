%global common_description %{expand:
flashprog is a utility for detecting, reading, writing, verifying and erasing flash chips. It is often used to flash BIOS/EFI/coreboot/firmware images in-system using a supported mainboard, but it also supports flashing of network cards (NICs), SATA controller cards, and other external devices which can program flash chips.

It supports a wide range of flash chips (most commonly found in SOIC8, DIP8, SOIC16, WSON8, PLCC32, DIP32, TSOP32, and TSOP40 packages), which use various protocols such as LPC, FWH, parallel flash, or SPI.}

Name:           flashprog
Version:        1.4
Release:        1%{?dist}
Summary:        Utility for detecting, reading, writing, verifying and erasing flash chips

License:        GPL-2.0
URL:            https://review.sourcearcade.org/flashprog

Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  anda-srpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  pciutils-devel
BuildRequires:  libusb1-devel
BuildRequires:  libftdi-devel
BuildRequires:  libjaylink-devel
BuildRequires:  libgpiod-devel
BuildRequires:  systemd-devel

%description
%{common_description}


%package libs-static
Summary:        Shared static library for flashprog

%description libs-static
%{common_description}

%package devel
Summary:        Development headers for flashprog

%description devel
%{common_description}


%prep
%git_clone %{url} v%{version}

%build
%make_build PREFIX=%{_prefix}

%install
%__make DESTDIR=%{buildroot} PREFIX=%{_prefix} install libinstall

%files
%license COPYING
%doc README.md
%{_bindir}/flashprog
%{_mandir}/man8/flashprog.8.gz
%{_mandir}/man8/flashprog-config.8.gz
%{_mandir}/man8/flashprog-write-protect.8.gz

%files libs-static
%license COPYING
%{_prefix}/lib/libflashprog.a

%files devel
%{_includedir}/libflashprog.h

%changelog
* Thu Feb 27 2025 sadlerm <lerm@chromebook.lol>
- Initial package

