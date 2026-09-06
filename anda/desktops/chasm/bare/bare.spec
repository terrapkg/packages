%global debug_package %{nil}

Name:           bare
Release:        1%{?dist}
Version:        0.2.43
Summary:        Interactive shell in x86_64 Linux assembly
License:        Unlicense
URL:            https://github.com/isene/bare
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Interactive shell in x86_64 Linux assembly. No libc, no runtime, pure syscalls.

%prep
%autosetup -C

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
install -Dm755 plugins/ask      %{buildroot}%{_datadir}/bare/plugins/ask
install -Dm755 plugins/suggest  %{buildroot}%{_datadir}/bare/plugins/suggest

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-open
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bare/plugins/*

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.2.43-1
- Initial commit
