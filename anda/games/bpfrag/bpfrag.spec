# SPDX-License-Identifier: MIT
# Adapted from upstream packaging/rpm/bpfrag.spec.

# libbpf-sys builds a static libbpf that must link into the Rust binary.
%global _lto_cflags %{nil}

Name:           bpfrag
Version:        0.5.1
Release:        1%{?dist}
Summary:        eBPF network tuning for competitive gaming that undoes itself

# bpfrag is MIT and its BPF program is GPL-2.0-only OR MIT. Crates linked
# into the binary: MIT OR Apache-2.0, MIT, Unlicense OR MIT, BSD-2-Clause
# (libbpf-sys) and LGPL-2.1-only OR BSD-2-Clause (libbpf-rs, libbpf).
SourceLicense: MIT AND (GPL-2.0-only OR MIT)
License:        MIT AND (GPL-2.0-only OR MIT) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND BSD-2-Clause AND (LGPL-2.1-only OR BSD-2-Clause)
URL:            https://github.com/shanefagan/bpfrag
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo >= 1.85
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust >= 1.85
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  /usr/bin/pkg-config
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

Recommends:     ethtool
Recommends:     iw

%description
bpfrag counts UDP traffic per process with eBPF. When a game's network
traffic appears (a steady, two-way stream of small packets from a process
that is a game), it applies a networking profile chosen from the tick
rate: socket busy-polling, NIC interrupt coalescing, buffer headroom, DSCP
marking of the game's packets, Wi-Fi power save and, optionally, tighter
dirty-page writeback. Every change is journalled first and put back when
the match ends or the game exits.

It never changes CPU scheduling, so it runs next to sched_ext schedulers,
and it leaves bpftune's sysctls alone while bpftune is running.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dpm0755 target/rpm/bpfrag %{buildroot}%{_bindir}/bpfrag
install -Dpm0644 dist/bpfrag.service %{buildroot}%{_unitdir}/bpfrag.service
install -Dpm0644 dist/bpfrag.8 %{buildroot}%{_mandir}/man8/bpfrag.8
install -Dpm0644 dist/bpfrag.default %{buildroot}%{_sysconfdir}/default/bpfrag
install -Dpm0644 dist/bpfrag.toml %{buildroot}%{_sysconfdir}/bpfrag/bpfrag.toml

%check
%cargo_test

%post
%systemd_post bpfrag.service

%preun
%systemd_preun bpfrag.service

%postun
%systemd_postun_with_restart bpfrag.service

%files
%license LICENSE LICENSE-GPL-2.0 LICENSE.dependencies
%doc README.md
%{_bindir}/bpfrag
%{_unitdir}/bpfrag.service
%{_mandir}/man8/bpfrag.8*
%dir %{_sysconfdir}/bpfrag
%config(noreplace) %{_sysconfdir}/bpfrag/bpfrag.toml
%config(noreplace) %{_sysconfdir}/default/bpfrag

%changelog
* Tue Oct 27 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.3.0-1
- Initial package
