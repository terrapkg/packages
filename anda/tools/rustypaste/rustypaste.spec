%define __brp_mangle_shebangs %{nil}

Name:          rustypaste
Version:       0.16.1
Release:       2%?dist
Summary:       A minimal file upload/pastebin service
License:       MIT AND Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT) AND (CC0-1.0 OR Artistic-2.0) AND CC0-1.0 AND ISC AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
URL:           https://github.com/orhun/rustypaste
Source0:       %url/archive/refs/tags/v%{version}.tar.gz

BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: gcc
BuildRequires: cargo
BuildRequires: mold
BuildRequires: systemd-rpm-macros

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/rustypaste %{buildroot}%{_bindir}/rustypaste
install -Dm644 config.toml %{buildroot}%{_sysconfdir}/rustypaste/config.toml
install -Dm644 extra/systemd/rustypaste.env %{buildroot}%{_sysconfdir}/rustypaste/rustypaste.env
install -Dm644 extra/systemd/rustypaste.service %{buildroot}/usr/lib/systemd/system/rustypaste.service
install -Dm644 extra/systemd257+/rustypaste.sysusers %{buildroot}/usr/lib/sysusers.d/rustypaste.conf
install -Dm644 extra/systemd/rustypaste.tmpfiles %{buildroot}/usr/lib/tmpfiles.d/rustypaste.conf
%{cargo_license_online -a} > LICENSE.dependencies

%post
%systemd_post swayosd-libinput-backend.service

%preun
%systemd_preun swayosd-libinput-backend.service

%postun
%systemd_postun_with_restart swayosd-libinput-backend.service

%files
%doc README.md CHANGELOG.md RELEASE.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/rustypaste
%{_sysconfdir}/rustypaste/config.toml
%{_sysconfdir}/rustypaste/rustypaste.env
%{_unitdir}/rustypaste.service
%{_sysusersdir}/rustypaste.conf
%{_tmpfilesdir}/rustypaste.conf

%changelog
* Tue Jan 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Add dependency licenses

* Thu Nov 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
