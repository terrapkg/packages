%global pypi_name pi-topd
%global ver 5.7.0-1
%global sanitized_ver %(echo %{ver} | sed 's/-//g')
%global setup_ver %(echo %{ver} | sed 's/^v//')

Name:           python-%{pypi_name}
Version:        %{sanitized_ver}
Release:        1%{?dist}
Summary:        Daemon for managing pi-top functionality by managing the pi-top hub connection

License:        Apache-2.0
URL:            https://github.com/pi-top/pi-topd
Source0:        %{url}/archive/refs/tags/%{ver}.tar.gz
Source1:        Apache-2.0.txt
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
Packager:       Owen Zimmerman <owen@fyralabs.com>

%global _description %{expand:
%summary.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{setup_ver}

%pyproject_patch_dependency pyee:drop_constraints
%pyproject_patch_dependency pyzmq:drop_constraints
%pyproject_patch_dependency smbus2:drop_constraints
%pyproject_patch_dependency spidev:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pitopd
install -Dm644 debian/pi-topd.service %{buildroot}%{_unitdir}/pi-topd.service
install -Dm644 debian/pt-reboot.service %{buildroot}%{_unitdir}/pt-reboot.service
install -Dm644 debian/pt-poweroff.service %{buildroot}%{_unitdir}/pt-poweroff.service
install -Dm644 %{S:1} %{buildroot}%{_defaultlicensedir}/python3-%{pypi_name}/LICENSE

%post
%systemd_post pi-topd.service
%systemd_post pt-reboot.service
%systemd_post pt-poweroff.service

%preun
%systemd_preun pi-topd.service
%systemd_preun pt-reboot.service
%systemd_preun pt-poweroff.service

%postun
%systemd_postun_with_restart pi-topd.service
%systemd_postun_with_restart pt-reboot.service
%systemd_postun_with_restart pt-poweroff.service

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license %{_defaultlicensedir}/python3-%{pypi_name}/LICENSE
%doc README.rst
%{_bindir}/pi-topd
%{_bindir}/pt-poweroff
%{_bindir}/pt-reboot
%{_unitdir}/pi-topd.service
%{_unitdir}/pt-reboot.service
%{_unitdir}/pt-poweroff.service
%python3_sitelib/tests/*

%changelog
* Thu May 07 2026 Owen Zimmerman <owen@fyralabs.com> - 5.7.0-1
- Clean up spec, track upstream tag, use %%pyproject_patch_dependency

* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com> - 5.7.0-1
- Install files properly, update script

* Sun Oct 26 2025 Jaiden Riordan <jade@fyralabs.com> - 5.7.0-1
- ehehehe :3
