Name:		limine
Version:	12.0.2
Release:	1%{?dist}
Summary:	Modern, advanced, portable, multiprotocol bootloader
License:	BSD-2-Clause
URL:		https://limine-bootloader.org
Source0:	https://github.com/Limine-Bootloader/Limine/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    https://github.com/Limine-Bootloader/Limine/releases/download/v%{version}/limine-%{version}.tar.gz.sig
Source2:    https://raw.githubusercontent.com/Limine-Bootloader/Limine/refs/tags/v%{version}/README.md
Packager:	madonuko <mado@fyralabs.com>
BuildRequires:	nasm mtools llvm lld clang make

%description
Limine is a modern, advanced, portable, multiprotocol bootloader, also used as
the reference implementation for the Limine boot protocol.

%prep
%autosetup
cp %{S:2} .
gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys 05D29860D0A0668AAEFB9D691F3C021BECA23821
gpg --verify %{S:1} %{S:0} || exit 1

%conf
%configure --enable-all CC_FOR_TARGET=clang LD_FOR_TARGET=ld.lld

%build
%make_build

%install
%make_install


%files
%doc README.md 3RDPARTY.md FAQ.md CONFIG.md COPYING USAGE.md ChangeLog
%license %_datadir/doc/limine/LICENSES/LicenseRef-scancode-bsd-no-disclaimer-unmodified.txt
%license COPYING
%_bindir/limine
%_datadir/limine/
%_mandir/man1/limine.1.*
