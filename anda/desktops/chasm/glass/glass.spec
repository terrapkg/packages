%global debug_package %{nil}
%global glyph_ver 0.5.0

Name:           glass
Release:        1%{?dist}
Version:        0.3.46
Summary:        Pure assembly terminal emulator
License:        Unlicense
URL:            https://github.com/isene/glass
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/isene/glyph/archive/refs/tags/v%{glyph_ver}.tar.gz
BuildRequires:  nasm
BuildRequires:  make
Requires:       xorg-x11-server-Xorg
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Pure assembly terminal emulator. x86_64 Linux, no libc, X11 wire protocol. Part of CHasm.

%prep
%autosetup
mkdir ../glyph
tar -xf %{SOURCE1} -C ../glyph --strip-components=1

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
%make_install PREFIX=%{_prefix} install-emoji

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/glass/emoji/*.rgba

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.3.46-1
- Initial commit
