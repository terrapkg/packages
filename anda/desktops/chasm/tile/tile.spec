%global debug_package %{nil}

Name:           tile
Release:        1%{?dist}
Version:        0.1.42
Summary:        Pure-asm tiling window manager (CHasm suite)
License:        Unlicense
URL:            https://github.com/isene/tile
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Pure-asm tiling window manager (CHasm suite).
x86_64 Linux, no libc, X11 wire protocol, single static binary.

%prep
%autosetup -C

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
mv %{buildroot}%{_bindir}/strip %{buildroot}%{_bindir}/tile-strip

%files
%doc README.md PLAN.md CONFIG-FUTURE.md tilerc.example
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/tile-strip

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.42-1
- Initial commit
