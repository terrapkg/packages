%define debug_package %nil

Name:			katsu
Version:		0.4.0
Release:		1%?dist
Summary:		The vicious image builder
License:		MIT
URL:			https://github.com/FyraLabs/katsu
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:		xorriso dracut limine grub2 systemd-devel squashfs-tools
Requires:		dracut-live dracut-config-generic dracut-config-rescue grub2-tools-extra dracut-squash
BuildRequires:	cargo rust-packaging pkgconfig(libudev) clang-devel

%description
Katsu is a tool for building bootable images from RPM based systems.
It is an alternative to Lennart Poettering's mkosi tool, designed to be robust,
fast, and easy to use while still providing many output formats.

%prep
%autosetup

%build
%(echo "%{cargo_build}" | sed "s@--profile rpm@--profile release@g" | sed "s@-j @@")

%install
export CARGO_INSTALL_ROOT=%buildroot%_prefix
cargo install --path .
rm %buildroot%_prefix/.crates.toml %buildroot%_prefix/.crates2.json

%files
%doc README.md
%license LICENSE
%_bindir/katsu


%changelog
%autochangelog
