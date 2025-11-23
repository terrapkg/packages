Name:		limine
Version:	10.3.1
Release:	1%?dist
Summary:	Modern, advanced, portable, multiprotocol bootloader
License:	BSD-2-Clause
URL:		https://limine-bootloader.org
Source0:	https://codeberg.org/Limine/Limine/releases/download/v%version/limine-%version.tar.gz
Source1:	https://codeberg.org/Limine/Limine/raw/tag/v%version/README.md
Packager:	madonuko <mado@fyralabs.com>
BuildRequires:	nasm mtools llvm lld clang make

%description
Limine is a modern, advanced, portable, multiprotocol bootloader, also used as
the reference implementation for the Limine boot protocol.

%prep
%autosetup
cp %{S:1} .

%build
%configure --enable-all CC_FOR_TARGET=clang LD_FOR_TARGET=ld.lld
%make_build

%install
%make_install


%files
%doc README.md 3RDPARTY.md FAQ.md CONFIG.md PROTOCOL.md COPYING USAGE.md
%license %_datadir/doc/limine/LICENSES/LicenseRef-scancode-bsd-no-disclaimer-unmodified.txt
%license COPYING
%_bindir/limine
%_includedir/limine.h
%_datadir/limine/
%_mandir/man1/limine.1.gz
