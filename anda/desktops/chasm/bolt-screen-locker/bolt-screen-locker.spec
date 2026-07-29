%global _hardened_ldflags %nil

Name:           bolt-screen-locker
Release:        1%{?dist}
Version:        0.2.0
Summary:        Pure-asm screen locker for the CHasm desktop suite
License:        Unlicense
URL:            https://github.com/isene/bolt
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch:          0001-fix-install-permissions.patch
BuildRequires:  nasm
BuildRequires:  gcc
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Pure-asm screen locker for the CHasm desktop suite (x86_64 NASM, no libc).

%prep
%autosetup -C

%build
%make_build NASM="nasm -g" LD="%{__cc} -nostdlib -fuse-ld=mold -Wl,-z,muldefs %build_ldflags" CFLAGS="%build_cflags"

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license UNLICENSE
%{_bindir}/bolt
%attr(4755, root, root) %{_bindir}/bolt-auth

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.2.0-1
- Initial commit
