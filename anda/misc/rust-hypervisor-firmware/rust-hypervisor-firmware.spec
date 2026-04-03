%dnl %bcond rust_nightly 0

Name:           rust-hypervisor-firmware
Version:        0.4.2
Release:        1%{?dist}
Summary:        Simple firmware that is designed to be launched from anything that supports loading ELF binaries
URL:            https://github.com/cloud-hypervisor/rust-hypervisor-firmware
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
License:        Apache-2.0
BuildRequires:  anda-srpm-macros gcc cargo-rpm-macros
%dnl %if %{with rust_nightly}
BuildRequires: rustup
%dnl %endif

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
This repository contains a simple firmware that is designed
to be launched from anything that supports loading ELF
binaries and running them with the PVH booting standard.

The purpose is to be able to use this firmware to be able to
load a bootloader from within a disk image without requiring
the use of a complex firmware such as TianoCore/edk2 and without
requiring the VMM to reuse functionality used for booting the Linux kernel.

Currently it will directly load a kernel from a
disk image that follows the Boot Loader Specification

There is also minimal EFI compatibility support allowing the boot of
some images that use EFI (shim + GRUB2 as used by Ubuntu).

The firmware is primarily developed against Cloud Hypervisor
but there is also support for using QEMU's PVH loader.

This project was originally developed using Firecracker however as
it does not currently support resetting the virtio block device it
is not possible to boot all the way into the OS.

%prep
%autosetup -n %{name}-%{version}
%dnl %if %{with rust_nightly}
%rustup_nightly
%dnl %endif
%cargo_prep_online

%build
# ls -laH .cargo/bin
# cat /builddir/build/BUILD/rust-hypervisor-firmware-0.4.2-build/.rustup/settings.toml
# export RUSTFLAGS="-C linker=lld -C linker-flavor=ld.lld";
# CARGO_HOME=/home/owen/rpmbuild/BUILD/.cargo RUSTUP_HOME=/home/owen/rpmbuild/BUILD/.rustup
%{__cargo} build --profile rpm --target x86_64-unknown-none.json -Zbuild-std=core -Zbuild-std-features=compiler-builtins-mem
%dnl %{cargo_build} -Zbuild-std=core -Zbuild-std-features=compiler-builtins-mem

%install
install -Dm755 target/rpm/hypervisor-fw %{buildroot}%{_bindir}/hypervisor-fw
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/hypervisor-fw

%changelog
* Fri Apr 03 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
