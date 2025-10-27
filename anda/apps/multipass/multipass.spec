Name:			multipass
Version:		1.16.1
Release:		1%?dist
Summary:		Multipass orchestrates virtual Ubuntu instances
License:		GPLv3.0
URL:			https://canonical.com/multipass
Source0:		https://github.com/canonical/multipass/archive/refs/tags/v%version.tar.gz
BuildRequires:	devscripts flutter

%ifarch aarch64
Requires:       qemu-system-arm qemu-efi-aarch64
%endif
%ifarch x86_64
Requires:       qemu-system-x86
%endif
Requires:       mesa-libGL libpng qt6-qtbase qt6-qtbase-gui libxml2 dnsmasq dnsmasq-utils qemu-img slang iproute iptables-nft iputils linux-atm-libs iptables-libs xterm

%prep
%autosetup -n %name-%version

%build
%cmake

%cmake_build

%install
%cmake_install

