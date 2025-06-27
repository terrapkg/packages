%global commit ebf1a26831f518b9c2dcfd13daca3f53dae6a490
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250627
%global ver 1.0.13

Name:           scx-scheds-nightly
Version:        %{ver}^%{commitdate}.git.%{shortcommit}
Release:        1%?dist
Summary:        Nightly builds of sched_ext schedulers and tools
SourceLicense:  GPL-2.0-only
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND LGPL-2.1 AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (MPL-2.0 OR MIT OR Apache-2.0) AND MPL-2.0-only and MPL-2.0-or-later AND (Unlicense OR MIT) AND Zlib
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz
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
Provides:       scx_c_schedulers
Provides:       scxctl = %{version}
Provides:       scx_layered
Provides:       scx_rustland
Provides:       scx_rusty
Obsoletes:      scxctl >= 0.3.4
Packager:       Gilver E. <rockgrub@disroot.org>

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

%build
%meson \
 -Dsystemd=enabled \
 -Dopenrc=disabled \
 -Dlibalpm=disabled
%meson_build


%install
%meson_install

%{cargo_license_online} > LICENSE.dependencies

%files
%doc OVERVIEW.md
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/scx
%{_bindir}/scx*
%{_bindir}/vmlinux_docify
%{_unitdir}/scx_loader.service
%{_unitdir}/scx.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf
%{_datadir}/dbus-1/system-services/org.scx.Loader.service

%changelog
* Sun Jun 15 2025 Gilver E. <rockgrub@disroot.org> - 1.0.13^20250612.git.c1507b0-1
- Initial package
