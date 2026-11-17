Name:           vpower
Version:        1.6.4
Release:        3%{?dist}
Summary:        Service that calculates battery metrics and handles critical battery scenarios
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
License:        MIT
URL:            https://github.com/evlav/vpower
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

# See: https://github.com/ublue-os/bazzite/issues/6346
Patch0:         battery-discover-hwmon-path.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  lm_sensors-devel

Requires:       upower

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
