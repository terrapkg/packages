Name:           cardwire
Version:        0.7.1
Release:        1%{?dist}
Summary:        A GPU Manager for linux that uses eBPF LSM hooks to block GPUs
URL:            https://opengamingcollective.github.io/cardwire/
Source0:        https://github.com/OpenGamingCollective/cardwire/archive/refs/tags/v%{version}.tar.gz
License:	GPL-3.0-or-later AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND ISC AND MIT (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND Zlib
BuildRequires:  cargo-rpm-macros
BuildRequires:	systemd-rpm-macros
BuildRequires:	libbpf-devel
BuildRequires:	clang-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm0755 target/rpm/cardwire %{buildroot}%{_bindir}/cardwire
install -Dm0755 target/rpm/cardwired %{buildroot}%{_bindir}/cardwired
install -Dm0644 assets/cardwired.service %{buildroot}%{_unitdir}/cardwired.service
install -Dm0644 assets/com.github.opengamingcollective.cardwire.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.github.opengamingcollective.cardwire.conf
	
%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post cardwired.service

%preun
%systemd_preun cardwired.service

%postun
%systemd_postun_with_restart cardwired.service

%files
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/cardwire
%{_bindir}/cardwired
%{_unitdir}/cardwired.service
%{_datadir}/dbus-1/system.d/com.github.opengamingcollective.cardwire.conf

%changelog
* Wed May 06 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
