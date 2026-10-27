%global commit abcc603de96a0809e74b4b266eea8e16419be567
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20261027
%global ver 1.1.4

%global toolchain clang
%undefine __brp_mangle_shebangs

Name:           scx-scheds-nightly
Version:        %{ver}^%{commitdate}.git.%{shortcommit}
Release:        1%{?dist}
Summary:        Nightly builds of sched_ext schedulers and tools
SourceLicense:  GPL-2.0-only
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-only AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND LGPL-2.1-only AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (MPL-2.0 OR MIT OR Apache-2.0) AND MPL-2.0-or-later AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  bpftool
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang >= 17
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  libseccomp-devel
BuildRequires:  lld >= 17
BuildRequires:  llvm >= 17
BuildRequires:  make
BuildRequires:  meson >= 1.2
BuildRequires:  protobuf-compiler
BuildRequires:  python3
BuildRequires:  rust
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-ng-compat
BuildRequires:  pkgconfig(openssl)
Requires:       (scx-tools or scx-tools-nightly)
Suggests:       scx-tools-nightly
Requires:       elfutils-libelf
Requires:       jq
Requires:       libseccomp
Requires:       protobuf
Requires:       zlib
Conflicts:      rust-scx_utils-devel
Conflicts:      scx_c_schedulers
Conflicts:      scx_layered
Conflicts:      scx_rustland
Conflicts:      scx_rusty
Conflicts:      scx-scheds
Provides:       rust-scx_utils-devel
Provides:       scxctl = %{version}
Provides:       scx_layered = %{evr}
Provides:       scx_rustland = %{evr}
Provides:       scx_rusty = %{evr}
Obsoletes:      scxctl <= 0.3.4
Packager:       Gilver E. <roachy@fyralabs.com>

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them.

This package contains nightly builds of the sched_ext schedulers.

%package devel
License:       GPL-2.0-only
%pkg_devel_files
%doc BREAKING_CHANGES.md
%doc DEVELOPER_GUIDE.md
%license LICENSE

%prep
%autosetup -p1 -n scx-%{commit}
%cargo_prep_online
# libbpf-sys 1.7.0 vendors a libbpf whose linux/types.h shadows the kernel's and lacks __u128,
# which newer arm64 uapi headers (asm/sigcontext.h, asm/ptrace.h) use. Backport libbpf f90a9c487d75.
for h in $(find . %{_builddir} -path '*/libbpf-sys-*/libbpf/include/linux/types.h' 2>/dev/null | sort -u); do
  grep -q '__u128' "$h" || sed -i '/#include <asm\/posix_types.h>/a\
\
#ifdef __SIZEOF_INT128__\
typedef __signed__ __int128 __s128 __attribute__((aligned(16)));\
typedef unsigned __int128 __u128 __attribute__((aligned(16)));\
#endif' "$h"
done

%build
export AWS_LC_SYS_NO_JITTER_ENTROPY=1
%{cargo_build -a} \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_mitosis \
     --exclude scx_nitosis \
     --exclude scx_wd40 \
     --exclude xtask \
     --exclude scxcash \
     --exclude vmlinux_docify \
     --exclude scx_arena_selftests

%install
%install_cargo_bins
%install_cargo_devel_libs

%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc OVERVIEW.md
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/scx*

%changelog
* Sat May 2 2026 Gilver E. <roachy@fyralabs.com> - 1.1.0^20260502.git.ce8aa3d-2
- Update licenses
* Sun Jun 15 2025 Gilver E. <rockgrub@disroot.org> - 1.0.13^20250612.git.c1507b0-1
- Initial package
