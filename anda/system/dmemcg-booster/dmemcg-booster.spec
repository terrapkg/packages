Name:           dmemcg-booster
Version:        0.1.2
Release:        1%?dist
Summary:        Userspace utility for controling VRAM utilization
License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://gitlab.steamos.cloud/holo/dmemcg-booster
Source0:        %url/-/archive/%version/dmemcg-booster-%version.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  dbus-devel
Packager:       Tulip Blossom <tulilirockz@outlook.com>

Patch:          0001-License-under-MIT.patch

%description
%summary.

%prep
%autosetup -n %name-%version
%cargo_prep_online

%build
%{cargo_license_online -a} > LICENSE.dependencies

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_datadir}/licenses/dmemcg-booster/ ./LICENSE
install -Dpm0644 -t %{buildroot}%{_userunitdir}/ ./dmemcg-booster-user.service
install -Dpm0644 -t %{buildroot}%{_unitdir}/ ./dmemcg-booster-system.service

%post
%systemd_post dmemcg-booster.service

%preun
%systemd_preun dmemcg-booster.service

%postun
%systemd_postun_with_restart dmemcg-booster.service

%files
%license %{_datadir}/licenses/dmemcg-booster/LICENSE
%license LICENSE.dependencies
%{_bindir}/dmemcg-booster
%{_userunitdir}/dmemcg-booster-user.service
%{_unitdir}/dmemcg-booster-system.service

%changelog
* Thu May 05 2026 Tulip Blossom <tulilirockz@outlook.com> - 0.1.2-1
- Intial Commit
