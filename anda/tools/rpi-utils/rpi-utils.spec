%global commit e75e3296b1cb4b5b9903d08eaebcc9cf343aa5e7
%global commit_date 20241118
%global shortcommit %(c=%{commit}; echo ${C:0:7})

Name:			rpi-utils
Version:		%commit_date.%shortcommit
Release:		1%?dist
Summary:		A collection of scripts and simple applications for Raspberry Pi devices
License:		BSD
URL:			https://github.com/raspberrypi/utils
Source0:		%url/archive/%commit/utils-%commit.tar.gz
# BuildArch:      noarch
BuildRequires:	cmake dtc libfdt-devel g++

%description
dtmerge - A tool for applying compiled DT overlays (*.dtbo) to base Device Tree files (*.dtb). Also includes the dtoverlay and dtparam utilities.
eeptools - Tools for creating and managing EEPROMs for HAT+ and HAT board.
kdtc - A tool for compiling overlays with #includes, etc., as used in the kernel tree.
otpset - A short script to help with reading and setting the customer OTP bits.
overlaycheck - A tool for validating the overlay files and README in a kernel source tree.
ovmerge - A tool for merging DT overlay source files (*-overlay.dts), flattening and sorting .dts files for easy comparison, displaying the include tree, etc.
pinctrl - A more powerful replacement for raspi-gpio, a tool for displaying and modifying the GPIO and pin muxing state of a system, bypassing the kernel.
piolib - A library for accessing the Pi 5's PIO hardware.
raspinfo - A short script to dump information about the Pi. Intended for the submission of bug reports.
vclog - A tool to get VideoCore 'assert' or 'msg' logs with optional -f to wait for new logs to arrive.

%prep
%autosetup -n utils-%commit

%build
cmake .
make

%install
mkdir -p %buildroot%_bindir
install -pm755 dtmerge/dtmerge %buildroot%_bindir/
install -pm755 dtmerge/dtoverlay %buildroot%_bindir/
install -pm755 dtmerge/dtparam %buildroot%_bindir/
install -pm755 eeptools/eepdump %buildroot%_bindir/
install -pm755 eeptools/eepmake %buildroot%_bindir/
install -pm755 eeptools/eepflash.sh %buildroot%_bindir/
install -pm755 kdtc/kdtc %buildroot%_bindir/
install -pm755 otpset/otpset %buildroot%_bindir/
install -pm755 overlaycheck/overlaycheck %buildroot%_bindir/
install -pm755 ovmerge/ovmerge %buildroot%_bindir/
install -pm755 pinctrl/pinctrl %buildroot%_bindir/
install -pm755 piolib/piopwm %buildroot%_bindir/
install -pm755 piolib/dpi_interlace %buildroot%_bindir/
install -pm755 piolib/pioseq %buildroot%_bindir/
install -pm755 piolib/piotest %buildroot%_bindir/
install -pm755 piolib/piows2812 %buildroot%_bindir/
install -pm755 piolib/rp1sm %buildroot%_bindir/
install -pm755 raspinfo/raspinfo %buildroot%_bindir/
install -pm755 vcgencmd/vcgencmd %buildroot%_bindir/
install -pm755 vclog/vclog %buildroot%_bindir/
install -pm755 vcmailbox/vcmailbox %buildroot%_bindir/

%files
%doc README.md
%_bindir/dtmerge
%_bindir/dtoverlay
%_bindir/dtparam
%_bindir/eepdump
%_bindir/eepmake
%_bindir/eepflash.sh
%_bindir/kdtc
%_bindir/otpset
%_bindir/overlaycheck
%_bindir/ovmerge
%_bindir/pinctrl
%_bindir/piopwm
%_bindir/dpi_interlace
%_bindir/pioseq
%_bindir/piotest
%_bindir/piows2812
%_bindir/rp1sm
%_bindir/raspinfo
%_bindir/vcgencmd
%_bindir/vclog
%_bindir/vcmailbox

%changelog
* Mon Nov 18 2024 Owen-sz <owen@fyralabs.com>
- Package Raspberry Pi Utils