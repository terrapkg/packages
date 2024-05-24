Name:		limine
Version:	7.5.3
Release:	1%?dist
Summary:	Modern, advanced, portable, multiprotocol bootloader
License:	BSD-2-Clause
URL:		https://limine-bootloader.org
Source0:	https://github.com/limine-bootloader/limine/releases/download/v%version/limine-%version.tar.gz
Source1:	https://raw.githubusercontent.com/limine-bootloader/limine/v%version/README.md
BuildRequires:	nasm mtools llvm lld clang make

%description
Limine is a modern, advanced, portable, multiprotocol bootloader, also used as
the reference implementation for the Limine boot protocol.

%prep
%autosetup
cp %SOURCE1 .

%build
%configure --enable-all TOOLCHAIN_FOR_TARGET=llvm
%make_build

%install
%make_install

%files
%doc README.md CONFIG.md PHILOSOPHY.md PROTOCOL.md COPYING USAGE.md
%license COPYING
%_bindir/limine
%_includedir/limine.h
%_datadir/limine/
%_mandir/man1/limine.1.gz

%changelog
%autochangelog
