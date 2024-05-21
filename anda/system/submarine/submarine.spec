%ifarch x86_64
%global arch x86_64
%elifarch aarch64
%global arch arm64
%endif

Name:			submarine
Version:		0.2.1
Release:		1%?dist
Summary:		Experimental bootloader for ChomeOS's depthcharge
License:		GPL-3.0
URL:			https://github.com/FyraLabs/submarine
BuildRequires:	make gcc flex bison elfutils-devel parted vboot-utils golang xz bc openssl-devel git depthcharge-tools

%description
An experimental bootloader for ChomeOS's depthcharge.

Submarine provides a minimal Linux environmemt that lives in a small partition
(16mb) on the disk. We use this environment to bootstrap a full Linux system
(or a different system if you're brave.)

%prep
go install github.com/u-root/u-root@v0.11.0
git clone --recurse-submodules --shallow-submodules -b v%version %url .

%build
export PATH=$PATH:$HOME/go/bin
%make_build %arch

%install
mkdir -p %buildroot/boot %buildroot%_datadir/submarine
install -Dm644 build/submarine-*.kpart %buildroot%_datadir/submarine/
install -Dm644 build/submarine-*.bin %buildroot%_datadir/submarine/

%files
%_datadir/submarine/submarine-*.kpart
%_datadir/submarine/submarine-*.bin
