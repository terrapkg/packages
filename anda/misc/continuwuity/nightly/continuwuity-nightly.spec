%global commit b1bbf0f4652d9c29a0a0afa230478bccc5aea7bb
%global commit_date 20260704
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ver 26.6.0-alpha.1

Name:           continuwuity-nightly
Version:        %(echo "%{ver}" | sed 's/-/~/g')^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        A Matrix homeserver written in Rust.
License:        (MIT OR Apache-2.0 OR BSD-3-Clause) AND ((MIT OR Apache-2.0) AND NCSA) AND Unlicense AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND BlueOak-1.0.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR Apache-2.0) AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND MIT AND ISC AND ((MIT OR Apache-2.0) AND Apache-2.0) AND 0BSD AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

URL:            https://continuwuity.org
Source0:        https://forgejo.ellis.link/continuwuation/continuwuity/archive/%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  systemd-rpm-macros
# Needed to build rust-librocksdb-sys
BuildRequires:  clang
BuildRequires:  liburing-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  rust-srpm-macros
Requires:       liburing
Requires:       glibc
Requires:       libstdc++
Provides:       continuwuity-nightly
Packager:       Julian Anderson <julian@julian45.net>

%global _description %{expand:
A Matrix homeserver written in Rust, the official continuation of the conduwuit homeserver.}

%description %{_description}

%prep
%autosetup -n continuwuity
# Here's the one legally required mystery incantation in this file.
# Some of our dependencies have source files which are (for some reason) marked as executable.
# Files in .cargo/registry/ are copied into /usr/src/ by the debuginfo machinery
# at the end of the build step, and then the BRP shebang mangling script checks
# the entire buildroot to find executable files, and fails the build because
# it thinks Rust's file attributes are shebangs because they start with `#!`.
# So we prevent that mangler from kicking in.
%undefine __brp_mangle_shebangs
%cargo_prep_online

%build
%cargo_build
%cargo_vendor_manifest_online
%cargo_license_summary_online

%install
install -Dpm0755 target/rpm/conduwuit -t %{buildroot}%{_bindir}
install -Dpm0644 pkg/conduwuit.service -t %{buildroot}%{_unitdir}
install -Dpm0600 conduwuit-example.toml %{buildroot}%{_sysconfdir}/conduwuit/conduwuit.toml
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%license src/core/matrix/state_res/LICENSE
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%config(noreplace) %{_sysconfdir}/conduwuit/conduwuit.toml

%{_bindir}/conduwuit
%{_unitdir}/conduwuit.service
# Do not create /var/lib/conduwuit, systemd will create it if necessary

%post
%systemd_post conduwuit.service

%preun
%systemd_preun conduwuit.service

%postun
%systemd_postun_with_restart conduwuit.service

%changelog
* Sun Jun 28 2026 julian45 <julian@julian45.net>
- Initial package
