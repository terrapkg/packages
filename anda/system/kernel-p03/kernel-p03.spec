
#     |\|\|\                       ________
#    _|_|_|_|_____________________|________ \
#  / ---------------------------|-|-|_---- \ \
# | |                                     | | |
# | |                                     | |_/
# |_|                                     | |
# | |     =========        =========      | |     LINUX    LINUX   LINUX
# |_|         =====            =====      | |     NU   L  L   N L      L
# | |                                     | |     XLINUX  I  I  X   LIN
# | |                        =            | |     IN      N L   U      N
# | |             ============            | |     UX       UXLIN   LINUX
# | |           ==          =             | |
# | |_____                           _____| |
# |    =   \                       //  =  \ |
# |  ===== |                       ||  =  | |
# |    =   |_______________________|\  =  / |
#  \________________|_|_|_|________________/

# ==============================================================================
# Distro detection / RHEL & openSUSE compatibility
# ==============================================================================

%define _distro_fedora %{?fedora:1}%{!?fedora:0}
%define _distro_rhel   %{?rhel:1}%{!?rhel:0}
%define _distro_suse   %{?suse_version:1}%{!?suse_version:0}

%if !%{_distro_fedora} && !%{_distro_rhel} && !%{_distro_suse}
  %{warn: could not detect distro (%%fedora/%%rhel/%%suse_version all unset) — falling back to Fedora packaging rules}
  %define _distro_fedora 1
%endif

# ==============================================================================
# Build system overrides
# ==============================================================================
%define __spec_install_post   %{__os_install_post}
%define _build_id_links       none
%define _default_patch_fuzz   2
%define _disable_source_fetch 0
%if %{_distro_suse}
%define _mimalloc_lib libmimalloc.so.3
%else
%define _mimalloc_lib libmimalloc.so.2
%endif
%define make_build            LD_PRELOAD=%{_mimalloc_lib} make %{?_clang_args} %{?_gcc_ld_args} %{?_smp_mflags}
%undefine __brp_mangle_shebangs
%undefine _auto_set_build_flags

# ==============================================================================
# Feature flags
# ==============================================================================

# 0 = no debuginfo, no frame pointers (default)
# 1 = debuginfo + DWARF5 + frame pointers (required for RPM Fusion / Fedora)
%define _build_debug 0

%if !%{_build_debug}
  %define debug_package %{nil}
  %undefine _include_frame_pointers
%endif

# Compiler: set exactly one to 1. Setting both or neither aborts the build.
%define _build_clang 1
%define _build_gcc   0

# LTO: clang-only. Set at most one to 1.
%define _build_lto 1
%define _lto_thin  1
%define _lto_full  0

# Optimization level: 0=size, 2=O2, 3=O3, other=default
%define _opt_level 3

# Secure Boot: generates a per-machine MOK key on first install.
# Enroll once with: mokutil --import /etc/kernel/certs/p03-kernel/mok.der
%define _build_secureboot 1

# Tickrate: 100, 250, 300, 500, 600, 750, 1000. Invalid value falls back to 1000.
%define _hz_tick 750

# x86_64 ISA level: 1-4. Invalid value falls back to x86_64_v3.
%define _x86_64_lvl 3

# Minimal kernel via modprobed.db (CI only, not for production).
%define _build_minimal 0

# Local-patches-only mode:
#   0 = default: download GitHub patchset and apply it, then apply local patches
#   1 = offline:  skip GitHub download entirely; apply only patches found in
#                 SOURCES/local-patches/ (kernel) and SOURCES/local-patches-nvidia/
%define _local_patches_only 0

%define _build_generic 1
%define _interactive_config 0

# NR_CPUS: 1 = set from _nr_cpus (defaults to nproc), 0 = use kernel default.
%define _set_nr_cpus 0
%define _nr_cpus     %(nproc)

# NVIDIA open kernel modules.
%define _build_nv 1
%define _nv_ver   610.57.04
%define _nv_pkg   open-gpu-kernel-modules-%{_nv_ver}

# ==============================================================================
# Build identification — the only section you edit
# ==============================================================================

# Paste the full Koji NVR for the kernel you want to build against.
# Accepted formats:
#   kernel-7.2.0-0.rc7.260814g2f1baf1fc892.58.fc46
#   kernel-7.2.0-0.rc7.54.fc45
#   kernel-7.1.8-200.fc44
%define _koji_nvr  kernel-7.2.0-0.rc7.260814g2f1baf1fc892.58.fc46

# openSUSE only — paste the NVR from Kernel:HEAD OBS project:
#   https://download.opensuse.org/repositories/Kernel:/HEAD/standard/src/
# Formats (git hash suffix is always present):
#   kernel-source-7.2~rc7-2.1.gaf18d8c     (RC)
#   kernel-source-7.1.8-5.1.ga5cdd68       (stable)
%define _suse_nvr  kernel-source-7.2~rc7-2.1.gaf18d8c

# p03 release tag — sets the version suffix and the GitHub source ref.
# Must match an existing tag in the repo when _fetch_tag is 1.
# Format: p03.N
%define _tag_ver   p03.17

# 1 = fetch GitHub sources from %%_tag_ver above (default; tagged releases)
# 0 = fetch from the moving main branch (COPR/OBS bleeding edge)
%define _fetch_tag 1

# ==============================================================================
# Version string derivation — do not edit below this line
# ==============================================================================
# Each distro parses its own NVR into the same RPM version string
# (e.g. 7.2.0.rc7.p03.18). openSUSE's tilde (7.2~rc7) is normalized to
# Fedora's dotted form (7.2.0).
#
%define _buildnum   %(echo "%{_tag_ver}" | sed -E 's/^p03\\.//')

%if %{_distro_suse}
%define _is_rc    %(echo "%{_suse_nvr}" | grep -cE -- '~rc[0-9]')
%define _rcnum    %(echo "%{_suse_nvr}" | sed -nE 's/.*~rc([0-9]+).*/\\1/p')
%define _kver_str %(echo "%{_suse_nvr}" | cut -d- -f3 | sed 's/~.*//;/^[0-9]*\\.[0-9]*$/s/$/.0/')
%define _basekver %(echo "%{_suse_nvr}" | sed -E 's/^kernel-source-([0-9]+\\.[0-9]+).*/\\1/')
%else
%define _kver_str %(echo "%{_koji_nvr}" | cut -d- -f2)
%define _krel_str %(echo "%{_koji_nvr}" | cut -d- -f3-)
%define _is_rc    %(echo "%{_koji_nvr}" | grep -cE -- '-0\\.rc[0-9]')
%define _rcnum    %(echo "%{_koji_nvr}" | sed -nE 's/.*-0\\.rc([0-9]+)\\..*/\\1/p')
%define _basekver %(echo "%{_koji_nvr}" | sed -E 's/^kernel-([0-9]+\\.[0-9]+)\\..*/\\1/')
%endif

%if %{_is_rc} && "%{_rcnum}" == ""
  %{error: could not parse the RC number from the pasted NVR}
%endif

%if %{_build_gcc}
    %define _gccreltag  .gcc
    %define _gccpacktag -gcc
%endif

%define _custom_tag p03
%define _srcdir     linux-%{_kver_str}

%if %{_is_rc}
%define _pkgver_suffix .rc%{_rcnum}.%{_custom_tag}%{?_gccreltag}.%{_buildnum}
%else
%define _pkgver_suffix .%{_custom_tag}%{?_gccreltag}.%{_buildnum}
%endif
%define _pkgver %{_kver_str}%{_pkgver_suffix}

%define _rpmver     %{version}-%{release}
%define _kver       %{_rpmver}.%{_arch}
%define _devel_dir  %{_usrsrc}/kernels/%{_kver}
%define _kernel_dir /lib/modules/%{_kver}

# ==============================================================================
# Validation
# ==============================================================================
%if %{_build_clang} && %{_build_gcc}
  %{error: _build_clang and _build_gcc are mutually exclusive — set only one to 1}
%endif

%if !%{_build_clang} && !%{_build_gcc}
  %{error: no compiler selected — set either _build_clang or _build_gcc to 1}
%endif

%if %{_lto_thin} && %{_lto_full}
  %{error: _lto_thin and _lto_full are mutually exclusive — set only one to 1}
%endif

%if %{_build_gcc} && %{_build_lto}
  %{error: GCC LTO is not supported by this specfile — LTO is only available with _build_clang; unset _build_lto or set _build_clang to 1}
%endif

# ==============================================================================
# Compiler flags
# ==============================================================================
%if %{_opt_level}
  %define _opt_cflags -O%{_opt_level}
  %define _krustflags -Copt-level=%{_opt_level}
%else
  %define _opt_cflags %{nil}
  %define _krustflags %{nil}
%endif

%define _kcflags %{_opt_cflags}

%if %{_build_clang}
  %define _clang_args  CC=clang CXX=clang++ LD=ld.lld LLVM=1 LLVM_IAS=1
%else
  %define _gcc_ld_args LD=ld.lld
%endif

%if %{_build_secureboot}
  %define _mok_dir /etc/kernel/certs/p03-kernel
  %define _mok_der %{_mok_dir}/mok.der
  %define _mok_key %{_mok_dir}/mok.key
  %define _mok_pem %{_mok_dir}/mok.pem
%endif

%define _module_args KERNEL_UNAME=%{_kver} IGNORE_PREEMPT_RT_PRESENCE=1 SYSSRC=%{_builddir}/%{_srcdir} SYSOUT=%{_builddir}/%{_srcdir}

# ==============================================================================
# Package metadata
# ==============================================================================
Name:    kernel-%{_custom_tag}%{?_gccpacktag}
Summary: Linux P03
Version: %{_pkgver}
Release: 1%{?dist}
License: GPL-2.0-only
URL:     https://github.com/CatPieLeaf/linux-p03
Packager: CatPieLeaf <catpieleaf@proton.me>

Requires: %{name}-core    = %{_rpmver}
Requires: %{name}-modules = %{_rpmver}

Provides: installonlypkg(kernel)
%if %{_distro_suse}
Provides: multiversion(kernel)
%endif
Provides: kernel-%{_custom_tag}%{?_gccpacktag} > 6.12.9-cb1.0%{?_clang_args:.lto}.%{_custom_tag}%{?dist}

Obsoletes: kernel-%{_custom_tag}%{?_gccpacktag} <= 6.12.9-cb1.0.lto.%{_custom_tag}%{?dist}

# ==============================================================================
# Build dependencies
# ==============================================================================
BuildRequires: bc
BuildRequires: bison
BuildRequires: cpio
BuildRequires: dwarves
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: kmod
BuildRequires: make
BuildRequires: openssl
BuildRequires: python3-devel
BuildRequires: zstd
BuildRequires: rust
BuildRequires: rust-src
BuildRequires: quilt
BuildRequires: p7zip
BuildRequires: ncurses-devel

%if %{_distro_suse}
BuildRequires: libelf-devel
BuildRequires: libopenssl-devel
%else
BuildRequires: elfutils-devel
BuildRequires: openssl-devel
%endif

%if %{_distro_suse}
BuildRequires: perl
%else
BuildRequires: perl-Carp
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
%endif

%if %{_distro_suse}
BuildRequires: python3-PyYAML
%else
BuildRequires: python3-pyyaml
%endif

%if %{_distro_suse}
BuildRequires: libmimalloc3
%else
BuildRequires: mimalloc
%endif

%if %{_distro_suse}
BuildRequires: rust-bindgen
BuildRequires: cargo
%else
BuildRequires: bindgen
%endif

# openSUSE's "rust" package already bundles rustfmt; it has no standalone package.
%if !%{_distro_suse}
BuildRequires: rustfmt
%endif

BuildRequires: lld

%if %{_build_clang}
BuildRequires: clang
BuildRequires: llvm
%endif

%if %{_build_clang} && %{_build_lto}
%if %{_distro_suse}
BuildRequires: llvm-polly
%else
BuildRequires: polly
%endif
%endif

%if %{_build_nv}
BuildRequires: gcc-c++
%endif

%if %{_interactive_config}
%if %{_distro_suse}
BuildRequires: libqt5-qtbase-devel
%else
BuildRequires: qt5-qtbase-devel
%endif
%endif

# ==============================================================================
# Sources
# ==============================================================================

%if %{_fetch_tag}
%define _baseurl    https://raw.githubusercontent.com/CatPieLeaf/linux-p03/refs/tags/%{_tag_ver}/sources
%define _gh_archive https://github.com/CatPieLeaf/linux-p03/archive/refs/tags/%{_tag_ver}.tar.gz
%else
%define _baseurl    https://raw.githubusercontent.com/CatPieLeaf/linux-p03/refs/heads/main/sources
%define _gh_archive https://github.com/CatPieLeaf/linux-p03/archive/refs/heads/main.tar.gz
%endif

%if !%{_distro_suse}
Source0: https://koji.fedoraproject.org/packages/kernel/%{_kver_str}/%{_krel_str}/src/%{_koji_nvr}.src.rpm
%else
Source0: https://download.opensuse.org/repositories/Kernel:/HEAD/standard/src/%{_suse_nvr}.src.rpm
%endif

Source1: %{_baseurl}/kconfig/linux-p03.config

%if %{_build_minimal}
Source2: https://raw.githubusercontent.com/Frogging-Family/linux-tkg/master/linux-tkg-config/%{_basekver}/minimal-modprobed.db
%endif

%if !%{_local_patches_only}
Source3: %{_gh_archive}
%endif

%if %{_build_nv}
Source10: https://github.com/NVIDIA/open-gpu-kernel-modules/archive/%{_nv_ver}/%{_nv_pkg}.tar.gz
%endif

# Patches are NOT declared here individually.
# Everything inside sources/patchset/, sources/patches-p03/, and
# sources/patchset-nvidia/ in the GitHub repo is applied automatically
# in %%prep. Drop a .patch into SOURCES/local-patches/ for local testing.

# ==============================================================================
%description
    The meta package for %{name}.

# ==============================================================================
%prep
# ==============================================================================
%setup -q %{?SOURCE10:-b 10} -c -T -n %{_srcdir}

    mkdir -p "%{_sourcedir}/local-patches"
    mkdir -p "%{_sourcedir}/local-patches-nvidia"

%if !%{_local_patches_only}
    _gh_tmp="%{_builddir}/_gh_repo"
    mkdir -p "${_gh_tmp}"
    tar xzf %{SOURCE3} -C "${_gh_tmp}" --strip-components=1
%endif

%if %{_build_nv}
    # ---- Apply NVIDIA patches ------------------------------------------------
    mkdir -p %{_builddir}/nv-patches
    export QUILT_PATCHES=%{_builddir}/nv-patches

%if !%{_local_patches_only}
    find "${_gh_tmp}/sources/patchset-nvidia" -maxdepth 1 -name "*.patch" -exec cp {} "%{_builddir}/nv-patches/" \; 2>/dev/null
%endif

    find "%{_sourcedir}/local-patches-nvidia" -maxdepth 1 -name "*.patch" -exec cp {} "%{_builddir}/nv-patches/" \; 2>/dev/null

    while IFS= read -r p; do
        echo "$(basename "$p")" >> "%{_builddir}/nv-patches/series"
    done < <(find "%{_builddir}/nv-patches" -maxdepth 1 -name "*.patch" 2>/dev/null | sort)

    if [ -s "%{_builddir}/nv-patches/series" ]; then
        cd %{_builddir}/%{_nv_pkg}
        quilt push -a --fuzz=2 --leave-rejects
        cd %{_builddir}/%{_srcdir}
    fi
%endif

%if %{_distro_suse}
    # openSUSE: Source0 is the Kernel:HEAD SRPM, pre-fetched by OBS.
    mkdir -p %{_builddir}/suse-srpm
    cd %{_builddir}/suse-srpm
    rpm2cpio %{SOURCE0} | cpio -idm
    _suse_tarball=$(ls linux-*.tar.xz)
    tar xf "${_suse_tarball}" --strip-components=1 -C %{_builddir}/%{_srcdir}
    cd %{_builddir}/%{_srcdir}

    tar xjf %{_builddir}/suse-srpm/patches.rpmify.tar.bz2 -C %{_builddir}/suse-srpm
    tar xjf %{_builddir}/suse-srpm/patches.suse.tar.bz2   -C %{_builddir}/suse-srpm

    mkdir -p %{_builddir}/suse-patches
    export QUILT_PATCHES=%{_builddir}/suse-patches

    find "%{_builddir}/suse-srpm/patches.rpmify" -maxdepth 1 -type f -exec cp {} "%{_builddir}/suse-patches/" \;
    find "%{_builddir}/suse-srpm/patches.suse"   -maxdepth 1 -type f -exec cp {} "%{_builddir}/suse-patches/" \;

    grep -oE '^[[:space:]]*patches\.(rpmify|suse)/[^[:space:]]+' %{_builddir}/suse-srpm/series.conf \
        | xargs -n1 basename >> %{_builddir}/suse-patches/series

    quilt push -a --fuzz=2 --leave-rejects

    rm -rf %{_builddir}/%{_srcdir}/.pc

    # Base kconfig: openSUSE's x86_64 "default" flavor, same role as
    # Fedora's kernel-x86_64-fedora.config.
    tar xjf %{_builddir}/suse-srpm/config.tar.bz2 -C %{_builddir}/suse-srpm
    cp %{_builddir}/suse-srpm/config/x86_64/default .config
%else
    # Fedora/RHEL: Source0 is the Koji SRPM, pre-fetched before build.
    cd %{_builddir}
    rpm2cpio %{SOURCE0} | cpio -idm
    _tarball=$(ls linux-*.tar.xz)
    tar xf "${_tarball}" --strip-components=1 -C %{_srcdir}
    cd %{_srcdir}

    cp %{_builddir}/kernel-x86_64-fedora.config .config
%endif
%if %{_build_minimal}
    %make_build LSMOD=%{SOURCE2} localmodconfig
%else
    %make_build olddefconfig
%endif

%if %{_interactive_config}
    if [ -t 0 ]; then
        make %{?_clang_args} xconfig
    else
        make %{?_clang_args} nconfig
    fi
%endif

    mkdir -p %{_builddir}/patches
    export QUILT_PATCHES=%{_builddir}/patches

%if !%{_local_patches_only}
    find "${_gh_tmp}/sources/patchset" -maxdepth 1 -name "*.patch" -exec cp {} "%{_builddir}/patches/" \; 2>/dev/null
    find "${_gh_tmp}/sources/patches-p03" -maxdepth 1 -name "*.patch" -exec cp {} "%{_builddir}/patches/" \; 2>/dev/null
%endif

find "%{_sourcedir}/local-patches" -maxdepth 1 -name "*.patch" -exec cp {} "%{_builddir}/patches/" \; 2>/dev/null

while IFS= read -r p; do
    echo "$(basename "$p")" >> "%{_builddir}/patches/series"
done < <(find "%{_builddir}/patches" -maxdepth 1 -name "*.patch" 2>/dev/null | sort)

if [ -s "%{_builddir}/patches/series" ]; then
    quilt push -a --fuzz=2 --leave-rejects
fi

./scripts/kconfig/merge_config.sh -m .config %{SOURCE1}

# --- Kconfig -----------------------------------------------------------------

%if %{_build_generic}
    ./scripts/config --enable GENERIC_CPU
%else
    ./scripts/config -u GENERIC_CPU
%endif

    # Tickrate
    case %{_hz_tick} in
    100|250|300|500|600|750|1000)
        ./scripts/config --enable HZ_%{_hz_tick}
        ./scripts/config --set-val HZ %{_hz_tick}
        ;;
    *)
        echo "Invalid tickrate value, using default 1000"
        ./scripts/config --enable HZ_1000
        ./scripts/config --set-val HZ 1000
        ;;
    esac

    # x86_64 ISA level
%if %{_x86_64_lvl} < 5 && %{_x86_64_lvl} > 0
    scripts/config --set-val X86_64_VERSION %{_x86_64_lvl}
%else
    echo "Invalid x86_64 ISA Level. Using x86_64_v3"
    scripts/config --set-val X86_64_VERSION 3
%endif

    # Secure Boot: IMA, module signing, lockdown
%if %{_build_secureboot}
    scripts/config -e  IMA
    scripts/config -e  IMA_APPRAISE
    scripts/config -e  IMA_APPRAISE_BOOTPARAM
    scripts/config -e  IMA_APPRAISE_MODSIG
    scripts/config -e  IMA_ARCH_POLICY
    scripts/config -e  IMA_SECURE_AND_OR_TRUSTED_BOOT
    scripts/config -d  IMA_DEFAULT_HASH_SHA1
    scripts/config -e  IMA_DEFAULT_HASH_SHA256
    scripts/config --set-str IMA_DEFAULT_HASH "sha256"
    scripts/config -e  MODULE_SIG
    scripts/config -e  MODULE_SIG_ALL
    scripts/config -d  MODULE_SIG_FORCE
    # DO NOT ENABLE MODULE_SIG_FORCE. it causes DKMS not to load in some devices
    # Including mok signed DKMS!
    scripts/config -e  MODULE_SIG_SHA512
    scripts/config --set-str MODULE_SIG_HASH sha512
    scripts/config -e  KEXEC_SIG
    scripts/config -e  INTEGRITY_ASYMMETRIC_KEYS
    scripts/config -e  INTEGRITY_SIGNATURE
    scripts/config -e  LOCK_DOWN_KERNEL_FORCE_NONE
    # DO NOT CHANGE LOCKDOWN TO CONFIDENTIALITY OR INTEGRITY.
    # it causes DKMS not to load in some devices. Including mok signed DKMS!
    scripts/config -e  SECURITY_LOCKDOWN_LSM
    scripts/config -e  SECURITY_LOCKDOWN_LSM_EARLY
    scripts/config -e  SYSTEM_EXTRA_CERTIFICATE
    scripts/config --set-val SYSTEM_EXTRA_CERTIFICATE_SIZE 4096
    scripts/config -e  SYSTEM_TRUSTED_KEYRING
%endif

    # Clang LTO
%if %{_build_clang} && %{_build_lto}
    scripts/config -d LTO_NONE
    scripts/config -e POLLY_CLANG  # requires clang-polly patch from patchset/
  %if %{_lto_thin}
    scripts/config -e  LTO_CLANG_THIN
    scripts/config -d  LTO_CLANG_FULL
  %endif
  %if %{_lto_full}
    scripts/config -e  LTO_CLANG_FULL
    scripts/config -d  LTO_CLANG_THIN
  %endif
%endif

    # Optimization level
%if %{_opt_level} == 3
    scripts/config -d CC_OPTIMIZE_FOR_PERFORMANCE
    scripts/config -e CC_OPTIMIZE_FOR_PERFORMANCE_O3
    scripts/config -d CC_OPTIMIZE_FOR_SIZE
%else
  %if %{_opt_level} == 2
    scripts/config -e CC_OPTIMIZE_FOR_PERFORMANCE
    scripts/config -d CC_OPTIMIZE_FOR_PERFORMANCE_O3
    scripts/config -d CC_OPTIMIZE_FOR_SIZE
  %else
    %if %{_opt_level} == 0
      scripts/config -d CC_OPTIMIZE_FOR_PERFORMANCE
      scripts/config -d CC_OPTIMIZE_FOR_PERFORMANCE_O3
      scripts/config -e CC_OPTIMIZE_FOR_SIZE
    %endif
  %endif
%endif

%if %{_set_nr_cpus}
    scripts/config -d CPUMASK_OFFSTACK
    scripts/config -d MAXSMP
    scripts/config --set-val NR_CPUS %{_nr_cpus}
%endif

%if %{_build_debug}
    scripts/config -d DEBUG_INFO_NONE
    scripts/config -e DEBUG_INFO
    scripts/config -e DEBUG_INFO_DWARF5
    scripts/config -e DEBUG_INFO_BTF
%endif

    %make_build oldconfig

%if %{_build_minimal}
    %make_build LSMOD=%{SOURCE2} localmodconfig
%else
    %make_build olddefconfig
%endif

    diff -u %{SOURCE1} .config || :

# ==============================================================================
%build
# ==============================================================================
    %make_build EXTRAVERSION=%{_pkgver_suffix}-%{release}.%{_arch} KCFLAGS="%{?_kcflags}" KRUSTFLAGS="%{?_krustflags}" all

    # bpftool vmlinux.h for the devel package
    %make_build -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1 || true

%if %{_build_nv}
    cd %{_builddir}/%{_nv_pkg}
    CFLAGS= CXXFLAGS= LDFLAGS= %make_build %{?_clang_args} %{_module_args} IGNORE_CC_MISMATCH=yes modules
%endif

# ==============================================================================
%install
# ==============================================================================

    # 1. Kernel modules
    echo "Installing kernel modules..."
    ZSTD_CLEVEL=19 %make_build INSTALL_MOD_PATH="%{buildroot}" INSTALL_MOD_STRIP=1 DEPMOD=/doesnt/exist modules_install

    # 2. NVIDIA modules
%if %{_build_nv}
    echo "Installing NVIDIA modules..."
    cd %{_builddir}/%{_nv_pkg}
    install -Dt %{buildroot}%{_kernel_dir}/nvidia -m644 kernel-open/*.ko
    find %{buildroot}%{_kernel_dir}/nvidia -name '*.ko' -exec zstd -19 --rm {} \;
    install -Dt %{buildroot}/%{_defaultlicensedir}/%{name}-nvidia-open -m644 COPYING
    cd %{_builddir}/%{_srcdir}
%endif

    # 3. Kernel image — signing deferred to posttrans on the target machine;
    #    the build host must never hold the private MOK key.
    echo "Installing kernel image..."
    install -Dm644 "$(%make_build -s image_name)" "%{buildroot}%{_kernel_dir}/vmlinuz"

%if %{_build_secureboot}
    # ship sign-file so posttrans can sign external modules without -devel
    install -Dm755 scripts/sign-file "%{buildroot}%{_kernel_dir}/sign-file"
%endif

    # 4. Development files
    zstdmt -19 < Module.symvers > %{buildroot}%{_kernel_dir}/symvers.zst

    install -Dt %{buildroot}%{_devel_dir} -m644 .config Makefile Module.symvers System.map
    [ -f tools/bpf/bpftool/vmlinux.h ] && install -m644 tools/bpf/bpftool/vmlinux.h %{buildroot}%{_devel_dir}/ || true
    cp .config    %{buildroot}%{_kernel_dir}/config
    cp System.map %{buildroot}%{_kernel_dir}/System.map

    cp --parents `find -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}%{_devel_dir}
    cp -a scripts %{buildroot}%{_devel_dir}

    # Files needed for `make scripts`
    cp -a --parents security/selinux/include/classmap.h              %{buildroot}%{_devel_dir}
    cp -a --parents security/selinux/include/initial_sid_to_string.h %{buildroot}%{_devel_dir}
    cp    --parents security/selinux/include/policycap.h             %{buildroot}%{_devel_dir}
    cp    --parents security/selinux/include/policycap_names.h       %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/tools/be_byteshift.h               %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/tools/le_byteshift.h               %{buildroot}%{_devel_dir}

    # Files needed for `make prepare` — generic
    cp -a --parents tools/bpf/resolve_btfids          %{buildroot}%{_devel_dir}
    cp -a --parents tools/build/Build.include         %{buildroot}%{_devel_dir}
    cp    --parents tools/build/fixdep.c              %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/asm                 %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/asm-generic         %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/linux               %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/linux/compiler*     %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/linux/types.h       %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/uapi/asm            %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/uapi/asm-generic    %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/uapi/linux          %{buildroot}%{_devel_dir}
    cp -a --parents tools/include/vdso                %{buildroot}%{_devel_dir}
    cp -a --parents tools/lib/bpf                     %{buildroot}%{_devel_dir}
    cp    --parents tools/lib/bpf/Build               %{buildroot}%{_devel_dir}
    cp    --parents tools/lib/*.c                     %{buildroot}%{_devel_dir}
    cp -a --parents tools/lib/subcmd                  %{buildroot}%{_devel_dir}
    cp    --parents tools/objtool/*.[ch]              %{buildroot}%{_devel_dir}
    cp    --parents tools/objtool/Build               %{buildroot}%{_devel_dir}
    cp    --parents tools/objtool/include/objtool/*.h %{buildroot}%{_devel_dir}
    cp    --parents tools/objtool/sync-check.sh       %{buildroot}%{_devel_dir}
    cp    --parents tools/scripts/utilities.mak       %{buildroot}%{_devel_dir}

    # Files needed for `make prepare` — x86_64
    cp -a --parents arch/x86/boot/ctype.h                    %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/boot/string.c                   %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/boot/string.h                   %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/entry/syscalls/syscall_32.tbl   %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/entry/syscalls/syscall_64.tbl   %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/include                         %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/purgatory/entry64.S             %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/purgatory/purgatory.c           %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/purgatory/setup-x86_64.S        %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/purgatory/stack.S               %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/tools/relocs.c                  %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/tools/relocs.h                  %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/tools/relocs_32.c               %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/tools/relocs_64.c               %{buildroot}%{_devel_dir}
    cp -a --parents arch/x86/tools/relocs_common.c           %{buildroot}%{_devel_dir}
    cp -a --parents scripts/syscallhdr.sh                    %{buildroot}%{_devel_dir}
    cp -a --parents scripts/syscalltbl.sh                    %{buildroot}%{_devel_dir}
    cp -a --parents tools/arch/x86/include/asm               %{buildroot}%{_devel_dir}
    cp -a --parents tools/arch/x86/include/uapi/asm          %{buildroot}%{_devel_dir}
    cp -a --parents tools/arch/x86/lib/                      %{buildroot}%{_devel_dir}
    cp -a --parents tools/arch/x86/tools/gen-insn-attr-x86.awk %{buildroot}%{_devel_dir}
    cp -a --parents tools/objtool/arch/x86/                  %{buildroot}%{_devel_dir}

    cp -a include                    %{buildroot}%{_devel_dir}
    cp -a sound/soc/sof/sof-audio.h  %{buildroot}%{_devel_dir}/sound/soc/sof
    cp -a tools/objtool/fixdep       %{buildroot}%{_devel_dir}/tools/objtool/
    cp -a tools/objtool/objtool      %{buildroot}%{_devel_dir}/tools/objtool/

    echo "Cleaning up development files..."
    find %{buildroot}%{_devel_dir}/scripts \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
    find %{buildroot}%{_devel_dir}/tools   \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
    touch -r %{buildroot}%{_devel_dir}/Makefile %{buildroot}%{_devel_dir}/include/generated/uapi/linux/version.h %{buildroot}%{_devel_dir}/include/config/auto.conf

    # These symlinks are owned by the modules package; they would be broken
    # without the -devel package installed.
    rm -rf %{buildroot}%{_kernel_dir}/build
    ln -s %{_devel_dir}        %{buildroot}%{_kernel_dir}/build
    ln -s %{_kernel_dir}/build %{buildroot}%{_kernel_dir}/source

    # Stub initramfs to prevent failures due to insufficient space in /boot (bz #530778)
    install -dm755 %{buildroot}/boot
    dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{_kver}.img bs=1M count=90

# ==============================================================================
%package core
# ==============================================================================
Summary: Linux P03
AutoReq: no

Conflicts: xfsprogs < 4.3.0-1
%if %{_distro_suse}
Conflicts: xf86-input-vmmouse < 13.0.99
%else
Conflicts: xorg-x11-drv-vmmouse < 13.0.99
%endif

Provides: installonlypkg(kernel)
%if %{_distro_suse}
Provides: multiversion(kernel)
%endif
Provides: kernel              = %{_rpmver}
Provides: kernel-core-uname-r = %{_kver}
Provides: kernel-uname-r      = %{_kver}

Requires:      kernel-modules-uname-r = %{_kver}
Requires(pre): /usr/bin/kernel-install
Requires(pre): coreutils
Requires(pre): dracut >= 027
Requires(pre): systemd >= 203-2

%if %{_distro_suse}
Requires(pre): ((kernel-firmware-all) if kernel-firmware-all)
%else
Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
%endif

Requires(preun): systemd >= 200

%if %{_distro_suse}
Recommends: kernel-firmware-all
%else
Recommends: linux-firmware
%endif

%if %{_build_secureboot}
Requires(post): openssl
Requires(post): sbsigntools
%endif

%description core
    The kernel package contains the Linux kernel (vmlinuz), the core of any
    Linux operating system. The kernel handles the basic functions of the
    operating system: memory allocation, process allocation, device input
    and output, etc.

%post core
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    touch %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{_kver}

%posttrans core
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{_kver}
%if %{_build_secureboot}
    # MOK key generation and vmlinuz signing — runs on the TARGET machine.
    # The private key is never present on the build host; generated here once
    # and reused across upgrades that share the same enrolled MOK certificate.
    MOK_CN="P03 Kernel Secure Boot"
    MOK_DIR="%{_mok_dir}"
    MOK_KEY="%{_mok_key}"
    MOK_DER="%{_mok_der}"
    MOK_PEM="%{_mok_pem}"

    mkdir -p "${MOK_DIR}"
    chmod 700 "${MOK_DIR}"

    if [ ! -f "${MOK_KEY}" ]; then
        echo "Generating MOK key at ${MOK_DIR} ..."
        openssl req -new -x509 -newkey rsa:4096 -keyout "${MOK_KEY}" -outform DER -out "${MOK_DER}" -nodes -days 36500 -subj "/CN=${MOK_CN}/" -addext "extendedKeyUsage=codeSigning"
        chmod 600 "${MOK_KEY}"
        openssl x509 -inform DER -in "${MOK_DER}" -out "${MOK_PEM}"
        echo "MOK key generated."
    else
        echo "Reusing existing MOK key from ${MOK_DIR}."
    fi

    # Sign vmlinuz in-place BEFORE kernel-install copies it to /boot
    # so the file that ends up in /boot is already signed.
    echo "Signing vmlinuz for Secure Boot..."
    SB_VMLINUZ="%{_kernel_dir}/vmlinuz"
    sbsign --key "${MOK_KEY}" --cert "${MOK_PEM}" --output "${SB_VMLINUZ}.signed" "${SB_VMLINUZ}"
    mv "${SB_VMLINUZ}.signed" "${SB_VMLINUZ}"
    echo "vmlinuz signed."
%endif
    if [ ! -e /run/ostree-booted ]; then
        /bin/kernel-install add %{_kver} %{_kernel_dir}/vmlinuz || exit $?
        if [[ ! -e "/boot/symvers-%{_kver}.zst" ]]; then
            cp "%{_kernel_dir}/symvers.zst" "/boot/symvers-%{_kver}.zst"
            if command -v restorecon &>/dev/null; then
                restorecon "/boot/symvers-%{_kver}.zst"
            fi
        fi
    fi
%if %{_build_secureboot}
    if command -v mokutil &>/dev/null; then
        SB_STATE=$(mokutil --sb-state 2>/dev/null || true)
        echo ""
        echo "======================================================================"
        echo " Kernel P03: Secure Boot key enrollment"
        echo "======================================================================"
        echo " MOK key: %{_mok_der}"
        echo " Current Secure Boot state: ${SB_STATE:-unknown}"
        echo " To enroll the key (only needed once per machine), run:"
        echo "   sudo mokutil --import %{_mok_der}"
        echo " Then reboot and confirm enrollment in the MOK Manager (shim)."
        echo "======================================================================"
    fi
%endif

%preun core
    /bin/kernel-install remove %{_kver} || exit $?
    if [ -x /usr/sbin/weak-modules ]; then
        /usr/sbin/weak-modules --remove-kernel %{_kver} || exit $?
    fi

%files core
    %license COPYING
    %ghost %attr(0600, root, root) /boot/initramfs-%{_kver}.img
    %ghost %attr(0644, root, root) /boot/symvers-%{_kver}.zst
%if %{_build_secureboot}
    # ghost: generated on the target machine by posttrans; tracked for removal
    # but not present in the RPM payload itself.
    %ghost %attr(0700, root, root) %dir %{_mok_dir}
    %ghost %attr(0600, root, root) %{_mok_key}
    %ghost %attr(0644, root, root) %{_mok_der}
    %ghost %attr(0644, root, root) %{_mok_pem}
    %{_kernel_dir}/sign-file
%endif
    %{_kernel_dir}/System.map
    %{_kernel_dir}/config
    %{_kernel_dir}/modules.builtin
    %{_kernel_dir}/modules.builtin.modinfo
    %{_kernel_dir}/symvers.zst
    %{_kernel_dir}/vmlinuz

# ==============================================================================
%package modules
# ==============================================================================
Summary: Kernel modules for %{name}

Provides: installonlypkg(kernel-module)
Provides: kernel-modules              = %{_rpmver}
Provides: kernel-modules-core         = %{_rpmver}
Provides: kernel-modules-core-uname-r = %{_kver}
Provides: kernel-modules-extra        = %{_rpmver}
Provides: kernel-modules-extra-uname-r = %{_kver}
Provides: kernel-modules-uname-r      = %{_kver}
Provides: v4l2loopback-kmod           = 0.14.0

Requires: kernel-uname-r = %{_kver}
Requires: kmod

%description modules
    This package provides kernel modules for the %{name}-core kernel package.

%post modules
    if [ ! -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{_kver} ]; then
        mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
        touch %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver}
    fi

%posttrans modules
    /sbin/depmod -a %{_kver}
    if [ ! -e /run/ostree-booted ]; then
        if [ -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver} ]; then
            rm -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver}
            echo "Running: dracut -f --kver %{_kver}"
            dracut -f --kver "%{_kver}" || exit $?
        fi
    fi
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver}

%files modules
    %dir %{_kernel_dir}
    %{_kernel_dir}/build
    %{_kernel_dir}/kernel
    %{_kernel_dir}/modules.order
    %{_kernel_dir}/source

# ==============================================================================
%package devel
# ==============================================================================
Summary:     Development package for building kernel modules against %{name}
AutoReqProv: no

Provides: installonlypkg(kernel)
%if %{_distro_suse}
Provides: multiversion(kernel)
%endif
Provides: kernel-devel         = %{_rpmver}
Provides: kernel-devel-uname-r = %{_kver}

Requires: bison
Requires: findutils
Requires: flex
Requires: make

%if %{_distro_suse}
Requires: libelf-devel
Requires: libopenssl-devel
Requires: perl
%else
Requires: elfutils-libelf-devel
Requires: openssl-devel
Requires: perl-interpreter
%endif

Requires: lld

%if %{_build_clang}
Requires: clang
Requires: llvm
%if %{_build_lto}
%if %{_distro_suse}
Requires: llvm-polly
%else
Requires: polly
%endif
%endif
%else
Requires: gcc
%endif

%description devel
    This package provides kernel headers and makefiles sufficient to build
    modules against %{name}.

%post devel
    if [ -f /etc/sysconfig/kernel ]; then
        . /etc/sysconfig/kernel || exit $?
    fi
    if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ]; then
        (cd /usr/src/kernels/%{_kver} &&
        /usr/bin/find . -type f | while read f; do
            hardlink -c /usr/src/kernels/*%{?dist}.*/$f $f > /dev/null
        done;
        )
    fi

%files devel
    %{_devel_dir}

# ==============================================================================
%package devel-matched
# ==============================================================================
Summary: Meta package to install matching core, modules and devel for %{name}

Provides: installonlypkg(kernel)
%if %{_distro_suse}
Provides: multiversion(kernel)
%endif
Provides: kernel-devel-matched = %{_rpmver}

Requires: %{name}-core    = %{_rpmver}
Requires: %{name}-modules = %{_rpmver}
Requires: %{name}-devel   = %{_rpmver}

%description devel-matched
    This meta package pulls in kernel-p03-core, kernel-p03-modules and
    kernel-p03-devel together.

%files devel-matched

# ==============================================================================
%if %{_build_nv}
%package nvidia-open
# ==============================================================================
Summary: nvidia-open %{_nv_ver} kernel modules for %{name}
License: MIT AND GPL-2.0-only

Provides: installonlypkg(kernel-module)

Requires: kernel-uname-r = %{_kver}
Requires: kmod
%if !%{_distro_suse}
Requires: nvidia-gpu-firmware
%endif
%if %{_build_secureboot}
Requires: zstd
%endif

# These are the real RPM Fusion package/capability names for the same role -
# never let both be installed together.
Conflicts: akmod-nvidia
Conflicts: kmod-nvidia
Conflicts: nvidia-kmod

%description nvidia-open
    This package provides nvidia-open %{_nv_ver} kernel modules for %{name}.

%post nvidia-open
    _NV_URL="https://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}/NVIDIA-Linux-x86_64-%{_nv_ver}.run"
    echo ""
    echo "======================================================================"
    echo " !!!   NVIDIA USERSPACE DRIVER REQUIRED   !!!"
    echo "======================================================================"
    echo " This package ships ONLY the open kernel modules."
    echo " You MUST install the matching NVIDIA userspace driver (%{_nv_ver})"
    echo " separately."
    echo " "
    echo " DO NOT use dnf/rpm to install nvidia drivers — they will pull in"
    echo " conflicting kernel modules."
    echo " Use the official .run installer with the flags below."
    echo " "
    echo " Download:"
    echo "   wget ${_NV_URL}"
    echo " "
    echo " Install:"
    echo "   sudo sh ./NVIDIA-Linux-x86_64-%{_nv_ver}.run --no-kernel-modules --no-dkms --no-nouveau-check"
    echo " "
    echo "======================================================================"

    /sbin/depmod -a %{_kver}
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    touch %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver}

%posttrans nvidia-open
%if %{_build_secureboot}
    # Sign NVIDIA modules on the target machine using the MOK key from posttrans core.
    MOK_KEY="%{_mok_key}"
    MOK_PEM="%{_mok_pem}"
    SIGN_FILE="%{_kernel_dir}/sign-file"

    if [ -f "${MOK_KEY}" ] && [ -x "${SIGN_FILE}" ]; then
        echo "Signing NVIDIA modules for Secure Boot..."
        while IFS= read -r KO; do
            UNZST="${KO%.zst}"
            if ! zstd -d --rm "${KO}" -o "${UNZST}"; then
                echo "ERROR: failed to decompress ${KO}" >&2; exit 1
            fi
            if ! "${SIGN_FILE}" sha512 "${MOK_KEY}" "${MOK_PEM}" "${UNZST}"; then
                echo "ERROR: failed to sign ${UNZST}" >&2; exit 1
            fi
            if ! zstd -19 --rm "${UNZST}" -o "${KO}"; then
                echo "ERROR: failed to recompress ${UNZST}" >&2; exit 1
            fi
        done < <(find "%{_kernel_dir}/nvidia" -name "*.ko.zst")
        echo "NVIDIA modules signed."
    else
        echo "WARNING: MOK key not found at ${MOK_KEY}."
        echo "         Install or reinstall %{name}-core first so the key is"
        echo "         generated, then reinstall %{name}-nvidia-open."
    fi
%endif
    /sbin/depmod -a %{_kver}
    if [ -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver} ]; then
        rm -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{_kver}
        echo "Running: dracut -f --kver %{_kver}"
        dracut -f --kver "%{_kver}" || exit $?
    fi

%files nvidia-open
    %license %{_defaultlicensedir}/%{name}-nvidia-open/COPYING
    %{_kernel_dir}/nvidia
%endif

# ==============================================================================
%files

%changelog
* %(date '+%a %b %d %Y') CatPieLeaf <catpieleaf@proton.me> - %{version}-%{release}
- See https://github.com/CatPieLeaf/linux-p03/releases/tag/%{_tag_ver}
