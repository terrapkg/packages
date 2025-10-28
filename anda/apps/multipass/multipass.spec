%global commit 0e82c4bb73440675e7518b95796e4d2702b3f3f9
%global commit_date 20250821
%global shortcommit %(c=%{commit}; echo ${c:0:7})

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
%ifarch aarch64
export VCPKG_FORCE_SYSTEM_BINARIES=1
%endif
%git_clone %{url}.git %{commit}

%build
%cmake

%cmake_build

%install
%cmake_install

%files

%changelog
* DAY Oct DD 2025 Jaiden Riordan <jade@fyralabs.com>
- Initial package
