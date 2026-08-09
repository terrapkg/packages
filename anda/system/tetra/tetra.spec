Name:           tetra
Version:        0.2.1
Release:        2%{?dist}
Summary:        Modular host agent for Ultramarine Server and cloud hosts
SourceLicense:  AGPL-3.0-or-later
License:        (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND AGPL-3.0-or-later AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/Ultramarine-Linux/tetra
Source0:        https://github.com/Ultramarine-Linux/tetra/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  anda-srpm-macros
BuildRequires:  rust-packaging
BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  systemd-rpm-macros

Requires:       podman
Requires:       systemd

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Tetra is a modular host agent that exposes host-management operations
through a typed command envelope.

%prep
%autosetup -n tetra-%{version}
%cargo_prep_online

%build

%install
%cargo_install

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

# Remove the cargo registry and metadata files that get installed when building online
rm -rf %{buildroot}%{_datadir}/cargo/registry
rm -f %{buildroot}%{_prefix}/.crates.toml %{buildroot}%{_prefix}/.crates2.json

# State directories
mkdir -p %{buildroot}%{_sharedstatedir}/tetra
mkdir -p %{buildroot}%{_sharedstatedir}/tetra/identity

# Config directory & example transport
install -Dm644 examples/transport.json %{buildroot}%{_sysconfdir}/tetra/transport.json.example

# Data files (templates)
mkdir -p %{buildroot}%{_datadir}/tetra
cp -pr templates %{buildroot}%{_datadir}/tetra/

# Systemd service
install -Dm644 systemd/tetra.service %{buildroot}%{_unitdir}/tetra.service

%post
%systemd_post tetra.service

%preun
%systemd_preun tetra.service

%postun
%systemd_postun_with_restart tetra.service

%files
%license LICENSE LICENSE.dependencies
%doc README.md SECURITY.md docs/*
%{_bindir}/tetra
%{_unitdir}/tetra.service
%{_datadir}/tetra/templates
%config(noreplace) %{_sysconfdir}/tetra/transport.json.example
%dir %attr(0750, root, root) %{_sharedstatedir}/tetra
%dir %attr(0750, root, root) %{_sharedstatedir}/tetra/identity

%changelog
* Sun Aug 09 2026 Cypress Reed <cypress@fyralabs.com>
- Change license to AGPL

* Sun Jul 26 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package release
