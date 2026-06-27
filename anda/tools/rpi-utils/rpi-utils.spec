%global commit a30e7c7b227d9a5e6dbedc1d343077be7ad92959
%global commit_date 20260624
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:			rpi-utils
Version:		%{commit_date}.%{shortcommit}
Release:		1%{?dist}
Summary:		A collection of scripts and simple applications for Raspberry Pi devices
License:		BSD-3-Clause
URL:			https://github.com/raspberrypi/utils
Source0:		%{url}/archive/%{commit}.tar.gz
Patch0:         dtoverlay-manpage.patch
BuildRequires:	cmake dtc libfdt-devel gcc-c++ gnutls-devel ncurses-devel

Requires:       %{name}-dtmerge = %{evr}
Requires:       %{name}-eeptools = %{evr}
Requires:       %{name}-kdtc = %{evr}
Requires:       %{name}-otamaker = %{evr}
Requires:       %{name}-otpset = %{evr}
Requires:       %{name}-overlaycheck = %{evr}
Requires:       %{name}-ovmerge = %{evr}
Requires:       %{name}-pinctrl = %{evr}
Requires:       %{name}-piolib = %{evr}
Requires:       %{name}-raspinfo = %{evr}
Requires:       %{name}-rpieepromab = %{evr}
Requires:       %{name}-rpi-gpu-usage = %{evr}
Requires:       %{name}-rpifwcrypto = %{evr}
Requires:       %{name}-vcgencmd = %{evr}
Requires:       %{name}-vclog = %{evr}
Requires:       %{name}-vcmailbox = %{evr}

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package        dtmerge
Summary:        A tool for applying compiled DT overlays (*.dtbo) to base Device Tree files (*.dtb)
%description    dtmerge
%{summary}. Also includes the dtoverlay and dtparam utilities.

%package        dtmerge-devel
Summary:        Development files for %{name}-dtmerge
Requires:       %{name}-dtmerge = %{evr}

%description    dtmerge-devel
%{summary}.

%package        eeptools
Summary:        Tools for creating and managing EEPROMs for HAT+ and HAT board
%description    eeptools
%{summary}.

%package        kdtc
Requires:       dtc
Summary:        A tool for compiling overlays with #includes, etc., as used in the kernel tree
%description    kdtc
%{summary}.

%package        otamaker
Summary:        Tool for building Remote Update/Over-The-Air packages for Raspberry Pi Connect Remote Update
%description    otamaker
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

%pkg_completion -Bn %name-pinctrl pinctrl

%package        pinctrl-devel
Summary:        Development files for %{name}-pinctrl
Requires:       %{name}-pinctrl = %{evr}

%description    pinctrl-devel
%{summary}.

%package        piolib
Summary:        A library for accessing the Pi 5's PIO hardware
%description    piolib
%{summary}.

%package        piolib-devel
Summary:        Development files for %{name}-piolib
Requires:       %{name}-piolib = %{evr}

%description    piolib-devel
%{summary}.

%package        raspinfo
Summary:        A short script to dump information about the Pi. Intended for the submission of bug reports
%description    raspinfo
%{summary}.

%package        rpieepromab
Summary:        Mailbox based API that allows you to update and manage the AB EEPROM partitions
%description    rpieepromab
The Raspberry Pi EEPROM AB service is a mailbox based API that allows you to update and manage the AB EEPROM partitions.

Although this service can be used via raw vcmailbox commands the recommended API is the command line rpi-eeprom-ab application.

%package        rpieepromab-devel
Summary:        Development files for %{name}-rpieepromab
Requires:       %{name}-rpieepromab = %{evr}

%description    rpieepromab-devel
%{summary}.

%package        rpifwcrypto
Summary:        A command line application and shared library for the firmware cryptography service
%description    rpifwcrypto
%{summary}.

%package -n     %{name}-rpifwcrypto-devel
Summary:        Development files for %{name}-rpifwcrypto
Requires:       %{name}-rpifwcrypto = %{evr}
%description -n %{name}-rpifwcrypto-devel

%package        rpi-gpu-usage
Summary:        Simple tool for showing the per-process usage of the V3D GPU on Raspberry Pi 4 and 5
%description    rpi-gpu-usage
A simple tool for showing the per-process usage of the V3D GPU on Raspberry Pi 4 and 5.
It works by parsing the /proc/*/fdinfo/* information to find the processes that have drm stats information.

%pkg_completion -Bn %name-rpi-gpu-usage rpi-gpu-usage

%package        vcgencmd
Summary:        Query the VideoCore for information
%description    vcgencmd
A command line utility that can get various pieces of information
from the VideoCore GPU on the Raspberry Pi.

%pkg_completion -Bn %name-vcgencmd vcgencmd

%package        vcmailbox
Summary:        Send messages to the VideoCore via the mailbox
%description    vcmailbox
A low-level utility for sending mailbox messages to the VideoCore.

%package        vclog
Summary:        A tool to get VideoCore 'assert' or 'msg' logs with optional -f to wait for new logs to arrive
%description    vclog
%{summary}.

%prep
%autosetup -p1 -n utils-%{commit}

%build
%cmake -DBUILD_SHARED_LIBS=1
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENCE

%files dtmerge
%license LICENCE
%doc dtmerge/README.md
%{_bindir}/dt*
%{_mandir}/man1/dtmerge.1.gz
%{_mandir}/man1/dtoverlay.1.gz
%{_mandir}/man1/dtparam.1.gz
%{_mandir}/man2/dtoverlay.2.gz
%{_libdir}/libdtovl.so.0

%files dtmerge-devel
%{_includedir}/dtoverlay.h
%{_libdir}/libdtovl.so

%files eeptools
%doc eeptools/README.md
%license LICENCE
%{_bindir}/eep*

%files kdtc
%doc kdtc/README.md
%license LICENCE
%{_bindir}/kdtc

%files otamaker
%doc otamaker/README.md
%license LICENCE
%{_bindir}/otamaker

%files otpset
%doc otpset/README.md
%license LICENCE
%{_bindir}/otpset

%files overlaycheck
%doc overlaycheck/README.md
%license LICENCE
%{_bindir}/overlaycheck
# idek but upstream cmake file puts this here
%{_bindir}/overlaycheck_exclusions.txt

%files ovmerge
%doc ovmerge/README.md
%license LICENCE
%{_bindir}/ovmerge

%files pinctrl
%doc pinctrl/README.md
%license LICENCE
%{_bindir}/pinctrl
%{_libdir}/libgpiolib.so.0

%files pinctrl-devel
%{_includedir}/gpiolib.h
%{_libdir}/libgpiolib.so

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
%{_libdir}/libpio.so.0

%files piolib-devel
%{_libdir}/libpio.so
%{_includedir}/piolib/hardware/*.h
%{_includedir}/piolib/pico/*.h
%{_includedir}/piolib/*.h

%files raspinfo
%{_bindir}/raspinfo
%doc raspinfo/README.md

%files rpieepromab
%{_bindir}/rpi-eeprom-ab
%{_libdir}/librpieepromab.so.0
%doc rpieepromab/README.md
%license LICENCE

%files rpieepromab-devel
%{_includedir}/rpieepromab.h
%{_libdir}/librpieepromab.so

%files rpifwcrypto
%{_bindir}/rpi-fw-crypto
%{_libdir}/librpifwcrypto.so.0
%doc rpifwcrypto/README.md

%files rpifwcrypto-devel
%{_libdir}/librpifwcrypto.so
%{_includedir}/rpifwcrypto.h

%files rpi-gpu-usage
%{_bindir}/rpi-gpu-usage
%{_mandir}/man1/rpi-gpu-usage.1.*
%doc rpi-gpu-usage/README.md
%license LICENCE

%files vcgencmd
%license LICENCE
%{_bindir}/vcgencmd
%{_mandir}/man1/vcgencmd.1.gz

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
* Thu May 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Add new subpackages, tidy up

* Tue Jan 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Seperate needed files into -devel packages, add more packages/files, install all files.

* Mon May 19 2025 Owen Zimmerman <owen@fyralabs.com>
- Build shared libraries

* Tue Dec 17 2024 sadlerm <sad_lerm@hotmail.com>
- Split into individual subpackages and no longer package raspinfo

* Mon Nov 18 2024 Owen Zimmerman <owen@fyralabs.com>
- Package Raspberry Pi Utils
