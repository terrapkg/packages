%global _hardened_ldflags %nil

Name:           glyph
Release:        1%{?dist}
Version:        0.5.0
Summary:        Pure assembly TrueType font rasterizer
License:        Unlicense
URL:            https://github.com/isene/glyph
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm gcc
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Pure assembly TrueType font rasterizer. x86_64 Linux, no libc.
Handles composite glyphs, UTF-8, OpenType variable fonts. Part of CHasm.

%prep
%autosetup -C

%build
%make_build NASM="nasm -g" LD="gcc -nostdlib -fuse-ld=mold -Wl,-z,muldefs %build_ldflags"

%install
install -Dm755 glyph %{buildroot}%{_bindir}/glyph

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.5.0-1
- Initial commit
