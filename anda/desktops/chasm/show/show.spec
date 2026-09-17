%global _hardened_ldflags %nil

Name:           show
Release:        1%{?dist}
Version:        0.1.0
Summary:        Pure assembly file viewer with syntax highlighting
License:        Unlicense
URL:            https://github.com/isene/show
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm gcc
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64
Conflicts:      nmh

%description
Pure assembly file viewer with syntax highlighting. Part of CHasm.

%prep
%autosetup -C
sed '/^\s*nasm/s/nasm /nasm -g /;/^\s*ld/s@ld @gcc -nostdlib -fuse-ld=mold -Wl,-z,muldefs %build_ldflags@' -i Makefile

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
