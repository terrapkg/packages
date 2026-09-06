%global _hardened_ldflags %nil

Name:           chasm-bits
Release:        1%{?dist}
Version:        0.1.2
Summary:        Tiny per-segment programs for the strip status bar (CHasm suite)
License:        Unlicense
URL:            https://github.com/isene/chasm-bits
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://unlicense.org/UNLICENSE
BuildRequires:  nasm
BuildRequires:  make
BuildRequires:  gcc
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64

%description
Tiny per-segment programs for the strip status bar. Part of the CHasm suite.

We call them asmites: little pieces of assembly, each a single focused tool
that strip composes into a status row. Same idea as i3blocks blocklets or
polybar modules, but each is a static x86_64 ELF talking straight to the kernel.

Each program is a single x86_64 NASM source file, no libc, pure syscalls.
Each does ONE thing: read some piece of system state, format it, write
it to stdout, exit. Static binaries, ~5-13 KB each.

strip spawns these as children on a refresh interval and reads their stdout.
Output may include ANSI SGR escapes (ESC[Nm) for color; strip parses
them and switches GC foreground per text-run.

%prep
%autosetup -C

sed '/^\s*nasm/s/nasm /nasm -g /;/^\s*ld/s@ld @gcc -nostdlib -fuse-ld=mold -Wl,-z,muldefs %build_ldflags@' -i Makefile

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
cp %{S:1} LICENSE

%files
%doc README.md
%license LICENSE
%{_bindir}/bits-battery
%{_bindir}/bits-brightness
%{_bindir}/bits-clock
%{_bindir}/bits-cpu
%{_bindir}/bits-date
%{_bindir}/bits-disk
%{_bindir}/bits-ip
%{_bindir}/bits-mailbox
%{_bindir}/bits-mailfetch
%{_bindir}/bits-mem
%{_bindir}/bits-moonphase
%{_bindir}/bits-ping
%{_bindir}/bits-pingok
%{_bindir}/bits-sep
%{_bindir}/bits-uptime
%{_bindir}/bits-wintitle

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.2-1
- Initial commit
