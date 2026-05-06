Name:           cardwire
Version:        0.6.0
Release:        1%{?dist}
Summary:        A GPU Manager for linux that uses eBPF LSM hooks to block GPUs
URL:            https://opengamingcollective.github.io/cardwire/
Source0:        https://github.com/OpenGamingCollective/cardwire/archive/refs/tags/v%{version}.tar.gz
License:	GPL-3.0-or-later
BuildRequires:  cargo-rpm-macros
BuildRequires:	systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  rust
BuildRequires:	libbpf-devel
BuildRequires:	clang-devel
ExclusiveArch:  x86_64

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
	
%{cargo_license_summary_online}
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
