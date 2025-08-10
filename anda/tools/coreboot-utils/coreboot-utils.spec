%define debug_package %nil

Name:           coreboot-utils
Version:        25.06
Release:        1%?dist
Summary:        Various coreboot utilities
URL:            https://doc.coreboot.org
License:        BSD-3-Clause AND Apache-2.0 AND CC-BY-SA-3.0 AND GPL-2.0-only AND GPL-3.0-or-later AND ISC AND BSD-2-Clause-Patent AND BSD-4-Clause-UC AND CC-PDDC AND GPL-2.0-or-later AND HPND-sell-varient AND LGPL-2.1-or-later AND BSD-2-Clause AND CC-BY-4.0 AND GPL-3.0-only AND HPND AND X11 AND MIT
Packager:	    Owen Zimmerman <owen@fyralabs.com>

Patch0:         spdtool-python3.patch
Patch1:         elf_segment_extractor-python3.patch

BuildRequires:  anda-srpm-macros
BuildRequires:  go-rpm-macros
BuildRequires:  pkg-config

BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  gcc-gnat
BuildRequires:  bison
BuildRequires:  meson
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  golang

BuildRequires:  libstdc++
BuildRequires:  libgcc
BuildRequires:	libbpf-devel
BuildRequires:  glibc-devel
BuildRequires:  ncurses-devel
BuildRequires:  libfl-devel
BuildRequires:  pciutils-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt5-qtsvg-devel

BuildRequires:  inkscape
BuildRequires:  flex
BuildRequires:  acpica-tools
BuildRequires:  binutils

%if 0%{?fedora} >= 42
BuildRequires:  gcc14 gcc14-c++
%endif

Requires:       bash
Requires:       python3
Requires:       dmidecode
# Make requires for seperate subpackages

%description
%summary.

%package        abuild
Conflicts:      abuild <= 25.06-1
Obsoletes:      abuild <= 25.06-1
Summary:        coreboot autobuild script builds coreboot images for all available targets
%description    abuild
%summary.

%package        amdfwtool
Summary:        Create AMD Firmware combination
%description    amdfwtool
%summary.

%package        amdtools
Summary:        Various tools for AMD processors
%description    amdtools
%summary.

%package        apcb
Summary:        AMD PSP Control Block tools
%description    apcb
The necessary tools for building APCBs are not available for use by coreboot.
This tool allows patching an existing APCB binary with specific SPDs
and GPIO selection pins.

apcb_edit - This tool allows patching an existing APCB binary with specific SPDs and GPIO selection pins.
apcb_v3_edit - This tool allows patching an existing APCB v3 binary with up to  16 specific SPDs.

%dnl %package archive - ### Currently bugged and does not compile ###
%dnl Summary:        Concatenate files and create an archive
%dnl %description    archive
%dnl %summary.

%package        autoport
Summary:        Porting coreboot using autoport
Requires:       acpica dmidecode ectool glibc pciutils
Requires:       inteltool = %{version}
Requires:       superiotool = %{version}
%description    autoport
Automated porting coreboot to Sandy Bridge/Ivy Bridge/Haswell platforms.

%package        bincfg
Summary:        Compiler/Decompiler for data blobs with specs
%description    bincfg
%summary.

%package        board_status
Summary:        Tools to collect logs and upload them to the board status repository
%description    board_status
%summary.

%package        bucts
Summary:        A tool to manipulate the BUC.TS bit on Intel targets
%description    bucts
%summary.

%package        cavium
Summary:        Devicetree_convert Tool to convert a DTB to a static C file
%description    cavium
%summary.

%package        cbfstool
Conflicts:      cbfstool <= 25.06-1
Obsoletes:      cbfstool <= 25.06-1
Summary:        Management utility for CBFS formatted ROM images
%description    cbfstool
%summary.

%package        cbmem
Conflicts:      cbmem <= 25.06-1
Obsoletes:      cbmem <= 25.06-1
Summary:        Prints out coreboot mem table information
%description    cbmem
Prints out coreboot mem table information in JSON by default, and also implements the basic cbmem -list and -console commands.

%package        chromeos-coreboot-utilities
Summary:        access or generate ChromeOS resources
%description    chromeos-coreboot-utilities
These scripts can be used to access or generate ChromeOS resources, for example
to extract System Agent reference code and other blobs (e.g. `mrc.bin`, refcode,
VGA option roms) from a ChromeOS recovery image.

%package        coreboot-configurator
Summary:        A simple GUI to change settings in coreboot's CBFS, via the nvramtool utility
Requires:       coreboot-utils-nvramtool = %version
%description    coreboot-configurator
%summary.

%package        docs
Summary:        Coreboot utility documentation
%description    docs
%summary.

%package        dtd_parser
Summary:        DTD structure parser
%description    dtd_parser
%summary.

%package        ectool
Conflicts:      chromium-ectool
Summary:        Dumps the RAM of a laptop's Embedded/Environmental Controller (EC)
%description    ectool
%summary.

%package        exynos
Summary:        Computes and fills Exynos ROM checksum (for BL1 or BL2)
%description    exynos
%summary.

%package        find_usbdebug
Summary:        Help find USB debug ports
%description    find_usbdebug
%summary.

%package        futility
Summary:        Firmware utility for signing ChromeOS images
%description    futility
%summary.

%package        genbuild_h
Summary:        Generate build system definitions
%description    genbuild_h
%summary.

%package        hda-decoder
Summary:        Dumps decoded HDA default configuration registers into a format which can be used in coreboot's verb table
%description    hda-decoder
%summary.

%package        ifdtool
Summary:        Extract and dump Intel Firmware Descriptor information
%description    ifdtool
%summary.

%package        intelmetool
Summary:        Dump interesting things about Management Engine even if hidden
%description    intelmetool
%summary.

%package        intelp2m
Summary:        convert the configuration DW0/1 registers value from an inteltool dump to coreboot macros
%description    intelp2m
%summary.

%package        intelvbttool
Summary:        Parse VBT from VGA BIOS
%description    intelvbttool
%summary.

%package        kbc1126
Summary:        dump the two blobs from the factory firmware of some HP laptops
%description    kbc1126
Tools used to dump the two blobs from the factory firmware of many HP
laptops with 8051-based SMSC KBC1098/KBC1126 embedded controller and
insert them to the firmware image.

%package        mediatek-coreboot-utilities
Summary:        Generate MediaTek bootload header
%description    mediatek-coreboot-utilities
check-pi-img.py - Check `PI_IMG` firmware.
gen-bl-img.py - Generate MediaTek bootloader header.

%package        mma
Summary:        Memory Margin Analysis automation tests
%description    mma
%summary.

%package        msrtool
Summary:        Dumps chipset-specific MSR registers
%description    msrtool
%summary.

%package        nvramtool
Summary:        Reads and writes coreboot parameters and displaying information from the coreboot table in CMOS/NVRAM
%description    nvramtool
%summary.

%package        pmh7tool
Summary:        Dumps, reads and writes PMH7 registers on Lenovo ThinkPads. PMH7 is used for switching on and off the power of some devices on the board such as dGPU
%description    pmh7tool
%summary.

%package        post
Summary:        Userspace utility that can be used to test POST cards
%description    post
%summary.

%package        qualcomm-coreboot-utilities
Summary:        CMM script to debug Qualcomm coreboot environments
%description    qualcomm-coreboot-utilities
CMM script to debug Qualcomm coreboot environments.

createxbl - Concatenates XBL segments into one ELF image
ipqheader - Returns a packed MBN header image with the specified base and size
mbncat - Generate ipq8064 uber SBL
mbn_tools - Contains all MBN Utilities for image generation

%package        riscv-coreboot-utilities
Summary:        riscv coreboot utilities
%description    riscv-coreboot-utilities
%summary.

%package        rockchip-coreboot-utilities
Summary:        Generate Rockchip idblock bootloader
%description    rockchip-coreboot-utilities
%summary.

%package        scripts
Summary:        Various coreboot utility scripts
%description    scripts
- capture_commands.sh - Write all commands from the build to a file.
- config - Manipulate options in a .config file from the command line.
- cross-repo-cherrypick - Pull in patches from another tree from a gerrit repository.
- decode_spd.sh - Decodes Serial Presence Detect (SPD) files into various human readable formats.
- dts-to-fmd.sh -Converts a depthcharge fmap.dts into an fmaptool compatible .fmd format.
- find_new_user_commits.sh - Finds new gerrit committers.
- find-unused-kconfig-symbols.sh - Points out Kconfig variables that may be unused. There are some false positives, but it serves as a starting point.
- gerrit-rebase - Applies all commits that from-branch has over to-branch, based on a common ancestor and gerrit meta-data.
- get_maintainer.pl - Print selected MAINTAINERS information for the files modified in a patch or for a file.
- maintainers.go - Build subsystem Maintainers.
- no-fsf-addresses.sh - Removes various FSF addresses from license headers.
- parse-maintainers.pl - Script to alphabetize MAINTAINERS file.
- rm_unused_code - Remove all code not used for a platform from the local git repository for auditing or release.
- show_platforms.sh - Makes a list of platforms in the tree. Does not show variants.
- ucode_h_to_bin.sh - Microcode conversion tool.
- update_submodules - Check all submodules for updates.

%package        smmstoretool
Summary:        Offline SMMSTORE variable modification tool
%description    smmstoretool
%summary.

%package        spdtool
Summary:        Dumps SPD ROMs from a given blob to separate files using known patterns and reserved bits
%description    spdtool
Dumps SPD ROMs from a given blob to separate files using known patterns
and reserved bits. Useful for analysing firmware that holds SPDs on boards
that have soldered down DRAM.

%package        spd_tools
Summary:        A set of tools to generate SPD files for platforms with memory down configurations
%description    spd_tools
%summary.

%package        spkmodem_recv
Summary:        Decode spkmodem signals
%description    spkmodem_recv
%summary.

%package        superiotool
Summary:        A user-space utility to detect Super I/O of a mainboard and provide detailed information about the register contents of the Super I/O
%description    superiotool
%summary.

%package        vboot_lib
Summary:        vboot library file
%description    vboot_lib
%summary.

%package        xcompile
Summary:        Cross compile setup
%description    xcompile
%summary.

%prep
%git_clone https://review.coreboot.org/coreboot.git %version
ls -la
%patch -P0 -p1
%patch -P1 -p1

%build
%if 0%{?fedora} >= 42
export CC=gcc-14
export CXX=g++-14
%endif

pushd util
%make_build -C amdfwtool LDFLAGS="-fPIE -lcrypto"
%dnl %make_build -C archive # bugged upstream, does not build
%make_build -C bincfg
%make_build -C bucts LDFLAGS="-fPIE"
%make_build -C cbmem CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS"
%make_build -C cbfstool
%make_build -C ectool LDFLAGS="-fPIE"
%make_build -C futility
%make_build -C ifdtool
%make_build -C intelmetool CFLAGS="%{optflags} -I %{_builddir}/coreboot/src/commonlib/bsd/include"
%make_build -C nvramtool LDFLAGS="-fPIE"
%make_build -C inteltool
%make_build -C superiotool
%make_build -C intelvbttool
%make_build -C intelp2m
%make_build -C hda-decoder
%make_build -C kbc1126
%make_build -C pmh7tool LDFLAGS="-fPIE"
%make_build -C post
%make_build -C smmstoretool CFLAGS="$CFLAGS -U_FORTIFY_SOURCE"
%make_build -C spd_tools
%make_build -C spkmodem_recv
%make_build -C riscv/starfive-jh7110-spl-tool LDFLAGS="-fPIE"

pushd autoport
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
%gobuild -o %{_builddir}/autoport
popd

pushd msrtool
./configure
%make_build
popd

pushd coreboot-configurator
%meson
%meson_build
popd
popd

%install
install -Dm 777 util/abuild/abuild %buildroot%_bindir/abuild

install -Dm 755 util/amdfwtool/amdfwtool %buildroot%_bindir/amdfwtool
install -Dm 755 util/amdfwtool/amdfwread %buildroot%_bindir/amdfwread

install -Dm 755 util/amdtools/k8-compare-pci-space.pl %buildroot%_bindir/k8-compare-pci-space
install -Dm 755 util/amdtools/k8-interpret-extended-memory-settings.pl %buildroot%_bindir/k8-interpret-extended-memory-settings
install -Dm 755 util/amdtools/k8-read-mem-settings.sh %buildroot%_bindir/k8-read-mem-settings
install -Dm 755 util/amdtools/parse-bkdg.pl %buildroot%_bindir/parse-bkdg
install -Dm 755 util/amdtools/update_efs_spi_speed %buildroot%_bindir/update_efs_spi_speed

install -Dm 755 util/apcb/apcb_edit.py %buildroot%_bindir/apcb_edit
install -Dm 755 util/apcb/apcb_v3a_edit.py %buildroot%_bindir/apcb_v3a_edit
install -Dm 755 util/apcb/apcb_v3_edit.py %buildroot%_bindir/apcb_v3_edit

%dnl install -Dm 777 util/archive/archive %buildroot%_bindir/archive

install -Dm 755 %{_builddir}/autoport %buildroot%_bindir/autoport

install -Dm 755 util/bincfg/bincfg %buildroot%_bindir/bincfg

install -Dm 755 util/board_status/board_status.sh %buildroot%_bindir/board_status
install -Dm 755 util/board_status/getrevision.sh %buildroot%_bindir/getrevision
install -Dm 755 util/board_status/set_up_live_image.sh %buildroot%_bindir/set_up_live_image

install -Dm 755 util/bucts/bucts %buildroot%_bindir/bucts

install -Dm 755 util/cavium/devicetree_convert.py %buildroot%_bindir/devicetree_convert

install -Dm 777 util/cbfstool/cbfstool %buildroot%_bindir/cbfstool

install -Dm 755 util/cbmem/cbmem %buildroot%_bindir/cbmem

install -Dm 755 util/chromeos/crosfirmware.sh %buildroot%_bindir/crosfirmware
install -Dm 755 util/chromeos/extract_blobs.sh %buildroot%_bindir/extract_blobs
install -Dm 755 util/chromeos/gen_test_hwid.sh %buildroot%_bindir/gen_test_hwid
install -Dm 755 util/chromeos/update_ec_headers.sh %buildroot%_bindir/update_ec_headers

install -Dm 755 util/coreboot-configurator/redhat-linux-build/src/application/coreboot-configurator %buildroot%_bindir/coreboot-configurator
install -Dm 644 util/coreboot-configurator/src/resources/org.coreboot.nvramtool.policy %{buildroot}%{_datadir}/polkit-1/actions/org.coreboot.nvramtool.policy
install -Dm 644 util/coreboot-configurator/src/resources/org.coreboot.reboot.policy %{buildroot}%{_datadir}/polkit-1/actions/org.coreboot.reboot.policy
install -Dm 644 util/coreboot-configurator/src/resources/coreboot-configurator.desktop %{buildroot}%{_datadir}/applications/coreboot-configurator.desktop
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/coreboot-configurator.png
install -Dm 644 util/coreboot-configurator/redhat-linux-build/src/resources/512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/coreboot-configurator.png


install -Dm 755 util/dtd_parser/dtd_parser.py %buildroot%_bindir/dtd_parser

install -Dm 755 util/ectool/ectool %buildroot%_bindir/ectool

install -Dm 755 util/exynos/fixed_cksum.py %buildroot%_bindir/fixed_cksum
install -Dm 755 util/exynos/variable_cksum.py %buildroot%_bindir/variable_cksum

install -Dm 755 util/find_usbdebug/find_usbdebug.sh %buildroot%_bindir/find_usbdebug

install -Dm 755 util/futility/futility %buildroot%_bindir/futility

install -Dm 755 util/genbuild_h/genbuild_h.sh %buildroot%_bindir/genbuild_h

install -Dm 755 util/hda-decoder/hda-decoder %buildroot%_bindir/hda-decoder

install -Dm 755 util/ifdtool/ifdtool %buildroot%_bindir/ifdtool

install -Dm 755 util/intelmetool/intelmetool %buildroot%_bindir/intelmetool

install -Dm 755 util/intelp2m/intelp2m %buildroot%_bindir/intelp2m

install -Dm 755 util/kbc1126/kbc1126_ec_dump %buildroot%_bindir/kbc1126_ec_dump
install -Dm 755 util/kbc1126/kbc1126_ec_insert %buildroot%_bindir/kbc1126_ec_insert

install -Dm 755 util/mediatek/check-pi-img.py %buildroot%_bindir/check-pi-img
install -Dm 755 util/mediatek/gen-bl-img.py %buildroot%_bindir/gen-bl-img

install -Dm 755 util/mma/mma_automated_test.sh %buildroot%_bindir/mma_automated_test
install -Dm 755 util/mma/mma_get_result.sh %buildroot%_bindir/mma_get_result
install -Dm 755 util/mma/mma_setup_test.sh %buildroot%_bindir/mma_setup_test

install -Dm 755 util/msrtool/msrtool %buildroot%_bindir/msrtool

install -Dm 755 util/nvramtool/nvramtool %buildroot%_bindir/nvramtool

install -Dm 755 util/pmh7tool/pmh7tool %buildroot%_bindir/pmh7tool

install -Dm 755 util/post/post %buildroot%_bindir/post

install -Dm 755 util/qualcomm/createxbl.py %buildroot%_bindir/createxbl
install -Dm 755 util/qualcomm/create_multielf.py %buildroot%_bindir/create_multielf
install -Dm 755 util/qualcomm/ipqheader.py %buildroot%_bindir/ipqheader
install -Dm 755 util/qualcomm/mbncat.py %buildroot%_bindir/mbncat
install -Dm 755 util/qualcomm/mbn_tools.py %buildroot%_bindir/mbn_tools
install -Dm 755 util/qualcomm/qgpt.py %buildroot%_bindir/qgpt
install -Dm 755 util/qualcomm/elf_segment_extractor.py %buildroot%_bindir/elf_segment_extractor

# install -Dm 755 util/qualcomm/sifive-gpt.py %buildroot%_bindir/sifive-gpt
# install -Dm 755 util/qualcomm/starfive-jh7110-spl-tool/ %buildroot%_bindir/spl_tool #funny?

install -Dm 755 util/riscv/make-spike-elf.sh %buildroot%_bindir/make-spike-elf

install -Dm 755 util/rockchip/make_idb.py %buildroot%_bindir/make_idb

install -Dm 755 util/scripts/capture_commands.sh %buildroot%_bindir/capture_commands
install -Dm 755 util/scripts/config %buildroot%_bindir/config
install -Dm 755 util/scripts/cross-repo-cherrypick %buildroot%_bindir/cross-repo-cherrypick
install -Dm 755 util/scripts/decode_spd.sh %buildroot%_bindir/decode_spd
install -Dm 755 util/scripts/dts-to-fmd.sh %buildroot%_bindir/dts-to-fmd
install -Dm 755 util/scripts/find_new_user_commits.sh %buildroot%_bindir/find_new_user_commits
install -Dm 755 util/scripts/find-unused-kconfig-symbols.sh %buildroot%_bindir/find-unused-kconfig-symbols
install -Dm 755 util/scripts/gerrit-rebase %buildroot%_bindir/gerrit-rebase
install -Dm 755 util/scripts/get_maintainer.pl %buildroot%_bindir/get_maintainer
install -Dm 755 util/scripts/no-fsf-addresses.sh %buildroot%_bindir/no-fsf-addresses
install -Dm 755 util/scripts/parse-maintainers.pl %buildroot%_bindir/parse-maintainers
install -Dm 755 util/scripts/prepare-commit-msg.clang-format %buildroot%_bindir/prepare-commit-msg.clang-format
install -Dm 755 util/scripts/rm_unused_code %buildroot%_bindir/rm_unused_code
install -Dm 755 util/scripts/show_platforms.sh %buildroot%_bindir/show_platforms
install -Dm 755 util/scripts/testsoc %buildroot%_bindir/testsoc
install -Dm 755 util/scripts/ucode_h_to_bin.sh %buildroot%_bindir/ucode_h_to_bin
install -Dm 755 util/scripts/update_submodules %buildroot%_bindir/update_submodules

install -Dm 755 util/smmstoretool/smmstoretool %buildroot%_bindir/smmstoretool

install -Dm 755 util/spdtool/spdtool.py %buildroot%_bindir/spdtool

install -Dm 755 util/spd_tools/bin/part_id_gen %buildroot%_bindir/part_id_gen
install -Dm 755 util/spd_tools/bin/spd_gen %buildroot%_bindir/spd_gen

install -Dm 755 util/spkmodem_recv/spkmodem-recv %buildroot%_bindir/spkmodem-recv

install -Dm 755 util/superiotool/superiotool %buildroot%_bindir/superiotool

install -Dm 755 util/xcompile/xcompile %buildroot%_libdir/xcompile

%files
%doc util/README.md AUTHORS MAINTAINERS
%license COPYING
%license LICENSES/*

%files abuild
%{_bindir}/abuild

%files amdfwtool
%{_bindir}/amdfwtool
%{_bindir}/amdfwread

%files amdtools
%{_bindir}/k8-compare-pci-space
%{_bindir}/k8-interpret-extended-memory-settings
%{_bindir}/k8-read-mem-settings
%{_bindir}/parse-bkdg
%{_bindir}/update_efs_spi_speed

%files apcb
%{_bindir}/apcb_edit
%{_bindir}/apcb_v3a_edit
%{_bindir}/apcb_v3_edit

%dnl %files archive
%dnl %{_bindir}/archive

%files autoport
%{_bindir}/autoport
%doc util/autoport/readme.md
%doc util/autoport/description.md

%files bincfg
%{_bindir}/bincfg
%doc util/bincfg/description.md

%files board_status
%{_bindir}/board_status
%{_bindir}/getrevision
%{_bindir}/set_up_live_image
%doc util/board_status/*.md

%files bucts
%{_bindir}/bucts
%doc util/bucts/*.md

%files cavium
%{_bindir}/devicetree_convert
%doc util/cavium/description.md

%files cbfstool
%{_bindir}/cbfstool

%files cbmem
%{_bindir}/cbmem

%files chromeos-coreboot-utilities
%{_bindir}/crosfirmware
%{_bindir}/extract_blobs
%{_bindir}/gen_test_hwid
%{_bindir}/update_ec_headers
%doc util/chromeos/*.md

%files coreboot-configurator
%{_bindir}/coreboot-configurator
%{_datadir}/polkit-1/actions/org.coreboot.nvramtool.policy
%{_datadir}/polkit-1/actions/org.coreboot.reboot.policy
%{_datadir}/applications/coreboot-configurator.desktop
%{_datadir}/icons/hicolor/24x24/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/48x48/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/96x96/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/16x16/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/32x32/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/64x64/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/128x128/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/256x256/apps/coreboot-configurator.png
%{_datadir}/icons/hicolor/512x512/apps/coreboot-configurator.png
%doc /util/coreboot-configurator/README.md

%files dtd_parser
%{_bindir}/dtd_parser

%files ectool
%{_bindir}/ectool

%files exynos
%{_bindir}/fixed_cksum
%{_bindir}/variable_cksum

%files find_usbdebug
%{_bindir}/find_usbdebug

%files futility
%{_bindir}/futility

%files genbuild_h
%{_bindir}/genbuild_h

%files hda-decoder
%{_bindir}/hda-decoder

%files ifdtool
%{_bindir}/ifdtool

%files intelmetool
%{_bindir}/intelmetool

%files intelp2m
%{_bindir}/intelp2m

%files kbc1126
%{_bindir}/kbc1126_ec_dump
%{_bindir}/kbc1126_ec_insert
%doc util/kbc1126/*.md

%files mediatek-coreboot-utilities
%{_bindir}/gen-bl-img
%{_bindir}/check-pi-img

%files mma
%{_bindir}/mma_automated_test
%{_bindir}/mma_get_result
%{_bindir}/mma_setup_test

%files msrtool
%{_bindir}/msrtool
%doc util/msrtool/README
%doc util/msrtool/description.md

%files nvramtool
%{_bindir}/nvramtool
%doc util/nvramtool/README
%doc util/nvramtool/DISCLAIMER
%doc util/nvramtool/Changelog
%license util/nvramtool/COPYING

%files pmh7tool
%{_bindir}/pmh7tool

%files post
%{_bindir}/post
%doc util/post/README

%files qualcomm-coreboot-utilities
%{_bindir}/createxbl
%{_bindir}/create_multielf
%{_bindir}/ipqheader
%{_bindir}/mbncat
%{_bindir}/mbn_tools
%{_bindir}/qgpt
%{_bindir}/elf_segment_extractor

%files riscv-coreboot-utilities
%{_bindir}/make-spike-elf
%{_bindir}/sifive-gpt
%{_bindir}/spl_tool
%doc util/riscv/starfive-jh7110-spl-tool/README.md
%license util/riscv/starfive-jh7110-spl-tool/LICENSE

%files rockchip-coreboot-utilities
%{_bindir}/make_idb
%license util/rockchip/LICENSE

%files scripts
%{_bindir}/capture_commands
%{_bindir}/config
%{_bindir}/cross-repo-cherrypick
%{_bindir}/decode_spd
%{_bindir}/dts-to-fmd
%{_bindir}/find_new_user_commits
%{_bindir}/find-unused-kconfig-symbols
%{_bindir}/gerrit-rebase
%{_bindir}/get_maintainer
%{_bindir}/no-fsf-addresses
%{_bindir}/parse-maintainers
%{_bindir}/prepare-commit-msg.clang-format
%{_bindir}/rm_unused_code
%{_bindir}/show_platforms
%{_bindir}/testsoc
%{_bindir}/ucode_h_to_bin
%{_bindir}/update_submodules

%files smmstoretool
%{_bindir}/smmstoretool

%files spdtool
%{_bindir}/spdtool

%files spd_tools
%{_bindir}/part_id_gen
%{_bindir}/spd_gen
%doc util/spd_tools/README.md

%files spkmodem_recv
%{_bindir}/spkmodem-recv

%files superiotool
%{_bindir}/superiotool
%doc util/superiotool/README
%license util/superiotool/LICENSE

%files vboot_lib
%{_libdir}/libvboot_host.so

%files xcompile
%{_libdir}/xcompile

%files docs
%doc Documentation/*.md
%doc Documentation/*.txt
%doc Documentation/util/abuild/*
%doc Documentation/util/cbfstool/*.md
%doc util/amdtool/*.md
%doc util/cbmem/description.md
%doc Documentation/util/ifdtool/*
%doc util/apcb/README
%doc util/apcb/description.md
%doc util/autoport/readme.md
%doc util/autoport/description.md
%doc util/bincfg/description.md
%doc util/board_status/*.md
%doc util/bucts/*.md
%doc util/cavium/description.md
%doc util/chromeos/*.md
%doc /util/coreboot-configurator/README.md
%doc util/dtd_parser/description.md
%doc util/ectool/description.md
%doc util/exynos/description.md
%doc util/futility/description.md
%doc util/genbuild_h/description.md
%doc util/hda-decoder/description.md
%doc util/ifdtool/description.md
%doc util/intelmetool/description.md
%doc util/intelp2m/description.md
%doc util/kbc1126/*.md
%doc Documentation/util/intelp2m/*
%doc util/mma/description.md
%doc util/msrtool/README
%doc util/msrtool/description.md
%license util/msrtool/COPYING
%doc util/mtkheader/description.md
%doc util/nvramtool/README
%doc util/nvramtool/DISCLAIMER
%doc util/nvramtool/Changelog
%doc util/nvramtool/description.md
%license util/nvramtool/COPYING
%doc util/pmh7tool/description.md
%doc util/post/README
%doc util/post/description.md
%doc util/qualcomm/description.md
%doc util/riscv/description.md
%doc util/riscv/starfive-jh7110-spl-tool/README.md
%license util/riscv/starfive-jh7110-spl-tool/LICENSE
%doc util/scripts/description.md
%doc util/smmstoretool/description.md
%doc util/spdtool/description.md
%doc util/spd_tools/README.md
%doc util/superiotool/description.md
%doc util/superiotool/README
%doc util/xcompile/description.md
%dnl %doc util/archive/description.md
%doc Documentation/util/smmstoretool/*
%license Documentation/COPYING

%changelog
* Wed Jul 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
