Name:           dfu-programmer
Version:        1.1.0
Release:        1%?dist
Summary:        A Device Firmware Update based USB programmer for Atmel chips
License:        GPL-2.0-or-later
URL:            https://github.com/dfu-programmer/dfu-programmer
Source0:        %url/archive/refs/tags/v%version.tar.gz
Patch0:         dfu-programmer-c99.patch
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0
BuildRequires: 	make gcc autoconf automake

%description 
A linux based command-line programmer for Atmel chips with a USB
bootloader supporting ISP. This is a mostly Device Firmware Update
(DFU) 1.0 compliant user-space application. Supports all DFU enabled
Atmel chips with USB support.

%prep
%autosetup -p1
touch ./ChangeLog
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
