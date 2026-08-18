Name:           pion
Version:        0.2.0
Release:        1%{?dist}
Summary:        Binder IPC Linux userspace root service
License:        MIT AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://github.com/technobaboo/pion
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros

%description
Binder IPC Linux userspace root service... Binder objects bound to files (like UNIX domain sockets!).

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/pion-binder   %{buildroot}%{_bindir}/pion-binder
install -Dm644 dist/pion-binder.service %{buildroot}%{_unitdir}/pion-binder.service
install -Dm644 dist/dev-pionfs.mount  %{buildroot}%{_unitdir}/dev-pionfs.mount

%post
%systemd_post pion-binder.service

%preun
%systemd_preun pion-binder.service

%postun
%systemd_postun_with_restart pion-binder.service

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/pion-binder
%{_unitdir}/pion-binder.service
%{_unitdir}/dev-pionfs.mount

%changelog
* Tue Mar 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
