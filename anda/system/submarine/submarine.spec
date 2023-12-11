%ifarch x86_64
%global arch x86_64
%elifarch aarch64
%global arch arm64
%endif

Name:			submarine
Version:		0.1.0
Release:		1%?dist
Summary:		Experimental bootloader for ChomeOS's depthcharge
License:		GPL-3.0
URL:			https://github.com/FyraLabs/submarine
Source0:		%url/archive/%version/submarine-%version.tar.gz
BuildRequires:	make gcc flex bison elfutils-devel parted vboot-utils golang xz bc openssl-devel

%description
An experimental bootloader for ChomeOS's depthcharge.

Submarine provides a minimal Linux environmemt that lives in a small partition
(16mb) on the disk. We use this environment to bootstrap a full Linux system
(or a different system if you're brave.)

%prep
%autosetup

go install github.com/u-root/u-root@latest

%build
%make_build %arch

%install
mkdir -p %buildroot/boot %buildroot%_datadir/submarine
install -Dm644 build/submarine-*.kpart %buildroot/boot/
install -Dm644 build/submarine.bin %buildroot%_datadir/submarine/

%files
/boot/submarine-*.kpart
%_datadir/submarine/submarine.bin
