%ifarch x86_64
%global arch x86_64
%elifarch aarch64
%global arch arm64
%endif
# do not strip binaries
%define __strip /bin/true
%define debug_package %{nil}


Name:			submarine
Version:		0.2.1
Release:		1%?dist
Summary:		Experimental bootloader for ChomeOS's depthcharge
License:		GPL-3.0
URL:			https://github.com/FyraLabs/submarine
BuildRequires:	make gcc flex bison elfutils-devel parted vboot-utils golang xz bc openssl-devel git depthcharge-tools uboot-tools

%description
An experimental bootloader for ChomeOS's depthcharge.

Submarine provides a minimal Linux environmemt that lives in a small partition
(16mb) on the disk. We use this environment to bootstrap a full Linux system
(or a different system if you're brave.)

%prep
git clone --recurse-submodules --shallow-submodules -b v%version %url .

pushd u-root
go install
popd

%build
export PATH=$PATH:$HOME/go/bin
%make_build %arch

%install
mkdir -p %buildroot/boot %buildroot%_datadir/submarine
install -Dm644 build/submarine-*.kpart %buildroot%_datadir/submarine/
# Symlink the installed kpart to just submarine.kpart
pushd %buildroot%_datadir/submarine/
find . -name 'submarine-*.kpart' -exec ln -srf {} submarine.kpart \;
popd

install -Dm644 build/submarine-*.bin %buildroot%_datadir/submarine/

%files
%_datadir/submarine/submarine-*.kpart
%_datadir/submarine/submarine.kpart
%_datadir/submarine/submarine-*.bin
