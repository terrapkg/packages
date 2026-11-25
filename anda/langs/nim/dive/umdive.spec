Name:           umdive
Version:        0.1.5
Release:        2%{?dist}
Summary:        Chroot utility (just like arch-chroot)
License:        MIT
URL:            https://github.com/Ultramarine-Linux/dive
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:       %_bindir/chroot
Requires:       %_bindir/mount
BuildSystem:    nimble
BuildRequires:  nim
Provides:       dive = %{evr}

%description
%summary.

%files
%doc README.md
%license LICENSE
%_bindir/dive

%changelog
* Sat Nov 21 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.5-1
- Switch to BuildSystem
