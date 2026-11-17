%global tag 3.0.0-rc.11
%global git_url https://github.com/ferronweb/ferron

%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           ferron3-fips
Version:        3.0.0~rc.11
Release:        1%{?dist}
Summary:        A fast, modern web server built for production debugging
SourceLicense:  MIT
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND BSD-3-Clause AND MIT AND BSL-1.0 AND ISC AND ((MIT OR Apache-2.0) AND Apache-2.0) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://ferron.sh
Source0:        https://github.com/ferronweb/ferron/archive/refs/tags/%{tag}.tar.gz
Source1:        ferron.sysusers

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  perl-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang

Requires:       ca-certificates
Provides:       webserver

Conflicts:      ferron
Conflicts:      ferron3

%description
Ferron is a fast, modern web server built for production debugging.
This build uses the FIPS 140-3 validated AWS-LC module.

%prep
%git_clone %{git_url} %{tag}
%cargo_prep_online

%build
%cargo_build -f fips -- --config "profile.rpm.package.aws-lc-fips-sys.debug=0"
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
for bin in ferron ferron-fmt ferron-kdl2ferron ferron-passwd ferron-precompress ferron-serve; do
    install -Dm0755 target/rpm/$bin %{buildroot}%{_bindir}/$bin
done
install -Dm0644 configs/ferron.pkgunix.conf %{buildroot}%{_sysconfdir}/ferron/ferron.conf
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
%doc README.md SECURITY.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md docs/
%{_bindir}/ferron
%{_bindir}/ferron-fmt
%{_bindir}/ferron-kdl2ferron
%{_bindir}/ferron-passwd
%{_bindir}/ferron-precompress
%{_bindir}/ferron-serve
%dir %{_sysconfdir}/ferron
%config(noreplace) %{_sysconfdir}/ferron/ferron.conf
%{_sysusersdir}/ferron.conf
%{_unitdir}/ferron.service
%dir %{_localstatedir}/www/ferron
%config(noreplace) %{_localstatedir}/www/ferron/*
%dir %attr(0755, ferron, ferron) %{_sharedstatedir}/ferron
%dir %attr(0755, ferron, ferron) %{_localstatedir}/log/ferron
