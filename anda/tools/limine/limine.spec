Name:		limine
Version:	5.20230726.0
Release:	1%?dist
Summary:	Modern, advanced, portable, multiprotocol bootloader
License:	BSD-2-Clause
URL:		https://limine-bootloader.org
Source0:	https://github.com/limine-bootloader/limine/releases/download/v%version/limine-%version.tar.xz
BuildRequires:	nasm mtools llvm mold clang make

%description
Limine is a modern, advanced, portable, multiprotocol bootloader, also used as
the reference implementation for the Limine boot protocol.

%prep
%autosetup

%build
%configure --enable-all TOOLCHAIN_FOR_TARGET=llvm LD_FOR_TARGET=mold
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE

%changelog
%autochangelog
