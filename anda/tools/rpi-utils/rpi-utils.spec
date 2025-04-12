%global commit 358ac7085d6a9c3d4ffa62e03c23c8671904c3ec
%global commit_date 20250412
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _unpackaged_files_terminate_build 0

Name:			rpi-utils
Version:		%{commit_date}.%{shortcommit}
Release:		1%?dist
Summary:		A collection of scripts and simple applications for Raspberry Pi devices
License:		BSD-3-Clause
URL:			https://github.com/raspberrypi/utils
Source0:		%{url}/archive/%{commit}.tar.gz
Patch0:         dtoverlay-manpage.patch
# BuildArch:      noarch
BuildRequires:	cmake dtc libfdt-devel gcc-c++

Requires:       %{name}-dtmerge
Requires:       %{name}-eeptools
Requires:       %{name}-kdtc
Requires:       %{name}-otpset
Requires:       %{name}-overlaycheck
Requires:       %{name}-ovmerge
Requires:       %{name}-pinctrl
Requires:       %{name}-piolib
Requires:       %{name}-vcgencmd
Requires:       %{name}-vclog
Requires:       %{name}-vcmailbox

%description
%{summary}

%package        dtmerge
Summary:        A tool for applying compiled DT overlays (*.dtbo) to base Device Tree files (*.dtb)
%description    dtmerge
%{summary}. Also includes the dtoverlay and dtparam utilities.

%package        eeptools
Summary:        Tools for creating and managing EEPROMs for HAT+ and HAT board
%description    eeptools
%{summary}.

%package        kdtc
Requires:       dtc
Summary:        A tool for compiling overlays with #includes, etc., as used in the kernel tree
%description    kdtc
%{summary}.

%package        otpset
Requires:       rpi-utils-vcmailbox = %{version}
Summary:        A short script to help with reading and setting the customer OTP bits
%description    otpset
%{summary}.

%package        overlaycheck
Requires:       rpi-utils-dtmerge = %{version}
Requires:       rpi-utils-ovmerge = %{version}
Summary:        A tool for validating the overlay files and README in a kernel source tree
%description    overlaycheck
%{summary}.

%package        ovmerge
Summary:        A tool for merging DT overlay source files (*-overlay.dts), flattening and sorting .dts files for easy comparison, displaying the include tree, etc
%description    ovmerge
%{summary}.

%package        pinctrl
Summary:        A more powerful replacement for raspi-gpio, a tool for displaying and modifying the GPIO and pin muxing state of a system, bypassing the kernel
%description    pinctrl
%{summary}.

%package        piolib
Summary:        A library for accessing the Pi 5's PIO hardware
%description    piolib
%{summary}.

%package        vcgencmd
Summary:        Query the VideoCore for information
%description    vcgencmd
A command line utility that can get various pieces of information
from the VideoCore GPU on the Raspberry Pi.

%package        vcmailbox
Summary:        Send messages to the VideoCore via the mailbox
%description    vcmailbox
A low-level utility for sending mailbox messages to the VideoCore.

%package        vclog
Summary:        A tool to get VideoCore 'assert' or 'msg' logs with optional -f to wait for new logs to arrive
%description    vclog
%{summary}.

%prep
%autosetup -p1 -n utils-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENCE

%files dtmerge
%license LICENCE
%{_bindir}/dt*
%{_mandir}/man1/dtmerge.1.gz
%{_mandir}/man1/dtoverlay.1.gz
%{_mandir}/man1/dtparam.1.gz
%{_mandir}/man2/dtoverlay.2.gz

%files eeptools
%doc eeptools/README.md
%license LICENCE
%{_bindir}/eep*

%files kdtc
%doc kdtc/README.md
%license LICENCE
%{_bindir}/kdtc

%files otpset
%doc otpset/README.md
%license LICENCE
%{_bindir}/otpset

%files overlaycheck
%doc overlaycheck/README.md
%license LICENCE
%{_bindir}/overlaycheck

%files ovmerge
%doc ovmerge/README.md
%license LICENCE
%{_bindir}/ovmerge

%files pinctrl
%doc pinctrl/README.md
%license LICENCE
%{_bindir}/pinctrl
%{_datadir}/bash-completion/completions/pinctrl

%files piolib
%doc piolib/README.md
%license LICENCE
%{_bindir}/apitest
%{_bindir}/dpi_csync
%{_bindir}/piopwm
%{_bindir}/pioseq
%{_bindir}/piotest
%{_bindir}/piows2812
%{_bindir}/quadenc
%{_bindir}/rp1sm

%files vcgencmd
%license LICENCE
%{_bindir}/vcgencmd
%{_mandir}/man1/vcgencmd.1.gz
%{_datadir}/bash-completion/completions/vcgencmd

%files vclog
%doc vclog/README.md
%license LICENCE
%{_bindir}/vclog

%files vcmailbox
%license LICENCE
%{_bindir}/vcmailbox
%{_mandir}/man1/vcmailbox.1.gz
%{_mandir}/man7/vcmailbox.7.gz
%{_mandir}/man7/raspiotp.7.gz
%{_mandir}/man7/raspirev.7.gz

%changelog
* Tue Dec 17 2024 sadlerm <sad_lerm@hotmail.com>
- Split into individual subpackages and no longer package raspinfo

* Mon Nov 18 2024 Owen-sz <owen@fyralabs.com>
- Package Raspberry Pi Utils
