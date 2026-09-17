%global commit_date 20251208
%global commit 1c70ca25cdb62f9448e7e650be1faf32ab8f7f0c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           flashrom-cros
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%{?dist}
Epoch:          1
Summary:        Simple program for reading/writing flash chips content (ChromiumOS fork)
License:        GPL-2.0-only
URL:            https://chromium.googlesource.com/chromiumos/third_party/flashrom
Source0:        %url/+archive/%commit.tar.gz
BuildRequires:  gcc gnupg2 libusb1-devel meson pciutils-devel python3-sphinx systemd zlib-devel dmidecode
Requires:       dmidecode udev
Conflicts:      flashrom
Packager:       WeirdTreeThing <bradyn127@protonmail.com>

%description
flashrom is a utility for identifying, reading, writing, verifying and erasing
flash chips. It is designed to flash BIOS/EFI/coreboot/firmware/optionROM
images on mainboards, network/graphics/storage controller cards, and various
other programmer devices.

%package devel
Summary:    Development package for %{name}
Requires:   %{name} = %{evr}
Conflicts:  flashrom-devel

%description devel
Files for development with %{name}.

%prep
%setup -c

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Duse_internal_dmi=false
%meson_build

%install
install -Dm755 %{_vpath_builddir}/flashrom %{buildroot}%{_bindir}/%{name}

install -Dm755 include/libflashrom.h %{buildroot}%{_includedir}/libflashrom.h
install -Dm755 %{_vpath_builddir}/meson-private/flashrom.pc %{buildroot}%{_libdir}/pkgconfig/flashrom.pc
install -Dm755 %{_vpath_builddir}/libflashrom.so %{buildroot}%{_libdir}/libflashrom.so
install -Dm755 %{_vpath_builddir}/libflashrom.so.1 %{buildroot}%{_libdir}/libflashrom.so.1
install -Dm755 %{_vpath_builddir}/libflashrom.so.1.0.0 %{buildroot}%{_libdir}/libflashrom.so.1.0.0

%files
%{_bindir}/%{name}
%license COPYING
%doc README.rst README.chromiumos doc/
%{_libdir}/libflashrom.so.*

%files devel
%{_includedir}/libflashrom.h
%{_libdir}/libflashrom.so
%{_libdir}/pkgconfig/flashrom.pc

%changelog
* Sun Jan 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Bump, install .so files correctly, use proper versioning name

* Fri Jul 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Add back to terra, conflict with flashrom, add devel package, include other needed files

* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
