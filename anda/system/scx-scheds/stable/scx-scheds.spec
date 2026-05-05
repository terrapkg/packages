%undefine __brp_mangle_shebangs

Name:           scx-scheds
Version:        1.1.0
Release:        2%{?dist}
Summary:        sched_ext schedulers
SourceLicense:  GPL-2.0-only
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-only AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND LGPL-2.1-only AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (MPL-2.0 OR MIT OR Apache-2.0) AND MPL-2.0-or-later AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  bpftool
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang >= 17
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  libseccomp-devel
BuildRequires:  lld >= 17
BuildRequires:  llvm >= 17
BuildRequires:  meson >= 1.2
BuildRequires:  protobuf-compiler
BuildRequires:  python3
BuildRequires:  rust
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-ng-compat
Requires:       (scx-tools or scx-tools-nightly)
Suggests:       scx-tools
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
Conflicts:      scx-scheds-git
Conflicts:      scx-scheds-nightly
Provides:       rust-scx_utils-devel
Provides:       scx_c_schedulers
Provides:       scxctl = %{version}
Provides:       scx_layered
Provides:       scx_rustland
Provides:       scx_rusty
Obsoletes:      scxctl <= 0.3.4
Packager:       Gilver E. <roachy@fyralabs.com>

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them.

%package devel
License:       GPL-2.0-only
%pkg_devel_files
%doc BREAKING_CHANGES.md
%doc DEVELOPER_GUIDE.md
%license LICENSE

%prep
%autosetup -n scx-%{version} -p1
%cargo_prep_online

%build
%{cargo_build -a} \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_mitosis \
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
* Sat May 2 2026 Gilver E. <roachy@fyralabs.com> - 1.1.0-2
- Update licenses
* Sun Jun 15 2025 Gilver E. <rockgrub@disroot.org> - 1.0.13-1
- Initial package
