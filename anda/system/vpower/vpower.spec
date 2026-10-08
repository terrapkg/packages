Name:           vpower
Version:        1.6.3
Release:        1%{?dist}
Summary:        Service that calculates battery metrics and handles critical battery scenarios
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
License:        MIT
URL:            https://github.com/evlav/vpower
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  lm_sensors-devel

Requires:       terra-upower

%description
Service that calculates battery metrics and handles critical battery scenarios

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dpm0755 target/rpm/vpower %{buildroot}%{_prefix}/lib/vpower
install -Dpm0644 vpower.service %{buildroot}%{_unitdir}/vpower.service
install -Dpm0644 vpower.toml %{buildroot}%{_sysconfdir}/vpower.toml

%post
%systemd_post vpower.service

%preun
%systemd_preun vpower.service

%postun
%systemd_postun_with_restart vpower.service

%files
%license LICENSE
%license LICENSE.dependencies
%{_prefix}/lib/vpower
%{_unitdir}/vpower.service
%config(noreplace) %{_sysconfdir}/vpower.toml

%changelog
* Wed Oct 07 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.6.3-1
- Initial vpower package
