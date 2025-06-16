Name:           scx-scheds
Version:        1.0.13
Release:        1%{?dist}
Summary:        sched_ext schedulers and tools
License:        GPL-2.0
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
Conflicts:      scx-scheds-git
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

%package devel
Summary:        Development files for %{name}

%description devel
The %{name}-devel package contains libraries header files for developing applications that use %{name}

%prep
%autosetup -n scx-%{version} -p1
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
%{_prefix}/lib/systemd/system/scx_loader.service
%{_prefix}/lib/systemd/system/scx.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf
%{_datadir}/dbus-1/system-services/org.scx.Loader.service

%files devel
%doc BREAKING_CHANGES.md
%doc DEVELOPER_GUIDE.md
%{_includedir}/scx/

%changelog
* Sun Jun 15 2025 Gilver E. <rockgrub@disroot.org> - 1.0.13-1
- Initial package
