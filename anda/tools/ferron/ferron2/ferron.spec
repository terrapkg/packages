%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           ferron
Version:        2.8.1
Release:        1%{?dist}
Summary:        A fast, modern, and easily configurable web server with automatic TLS
SourceLicense:  MIT
License:        %{shrink:
    %{sourcelicense}
    AND (0BSD OR MIT OR Apache-2.0)
    AND Apache-2.0
    AND (Apache-2.0 AND ISC)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR ISC OR MIT)
    AND (Apache-2.0 OR MIT)
    AND ((Apache-2.0 OR MIT) AND BSD-3-Clause)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND BSD-3-Clause
    AND (BSD-3-Clause AND MIT)
    AND (BSD-3-Clause OR MIT)
    AND BSL-1.0
    AND CDLA-Permissive-2.0
    AND ISC
    AND (ISC AND (Apache-2.0 OR ISC))
    AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0))
    AND MIT
    AND (MIT AND Apache-2.0)
    AND (MIT AND Apache-2.0 AND BSD-3-Clause)
    AND (MIT OR Apache-2.0)
    AND ((MIT OR Apache-2.0) AND Apache-2.0)
    AND ((MIT OR Apache-2.0) AND Unicode-3.0)
    AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later)
    AND (MIT OR Apache-2.0 OR Zlib)
    AND (MIT OR Zlib OR Apache-2.0)
    AND MPL-2.0
    AND Unicode-3.0
    AND (Unlicense OR MIT)
    AND Zlib
    AND (Zlib OR Apache-2.0 OR MIT)
}
URL:            https://ferron.sh
Source0:        https://github.com/ferronweb/ferron/archive/refs/tags/%{version}.tar.gz
Source1:        ferron.sysusers

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  perl-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  systemd-rpm-macros

Requires:       ca-certificates
Provides:       webserver
Conflicts:      ferron3
Conflicts:      ferron3-fips

%description
Ferron is a fast, modern, and easily configurable web server with automatic TLS.

%prep
%autosetup -n ferron-%{version}
cargo run --manifest-path build/prepare/Cargo.toml
%cargo_prep_online

%build
%cargo_build -- --manifest-path build/workspace/Cargo.toml
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
for bin in ferron ferron-passwd ferron-precompress ferron-yaml2kdl; do
    install -Dm0755 build/workspace/target/rpm/$bin %{buildroot}%{_bindir}/$bin
done
install -Dm0644 configs/ferron.packages.kdl %{buildroot}%{_sysconfdir}/ferron.kdl
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/ferron.conf
install -Dm0644 packaging/rpm/ferron.service %{buildroot}%{_unitdir}/ferron.service
sed -i 's|/usr/sbin/ferron|%{_bindir}/ferron|' %{buildroot}%{_unitdir}/ferron.service
install -dm0755 %{buildroot}%{_localstatedir}/www/ferron
cp -r wwwroot/. %{buildroot}%{_localstatedir}/www/ferron/
install -dm0755 %{buildroot}%{_sharedstatedir}/ferron
install -dm0755 %{buildroot}%{_localstatedir}/log/ferron

%post
%systemd_post ferron.service

%preun
%systemd_preun ferron.service

%postun
%systemd_postun_with_restart ferron.service

%files
%license LICENSE LICENSE.dependencies
%doc README.md SECURITY.md CHANGELOG.md MODULES.md docs/
%{_bindir}/ferron
%{_bindir}/ferron-passwd
%{_bindir}/ferron-precompress
%{_bindir}/ferron-yaml2kdl
%config(noreplace) %{_sysconfdir}/ferron.kdl
%{_sysusersdir}/ferron.conf
%{_unitdir}/ferron.service
%dir %{_localstatedir}/www/ferron
%config(noreplace) %{_localstatedir}/www/ferron/*
%dir %attr(0755, ferron, ferron) %{_sharedstatedir}/ferron
%dir %attr(0755, ferron, ferron) %{_localstatedir}/log/ferron
