%global pypi_name pi-topd
%global commit eb4edb5e1649732db22520c4033a93e1c3e35d5e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250123

Name:           python-%{pypi_name}
Version:        0~%commit_date.git~%shortcommit
Release:        1%{?dist}
Summary:        Daemon for managing pi-top functionality by managing the pi-top hub connection

License:        Apache-2.0
URL:            https://github.com/pi-top/pi-topd
Source0:        %url/archive/%commit.tar.gz
Source1:        Apache-2.0.txt
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
Packager:       Jaiden Riordan <jade@fyralabs.com>

%global _description %{expand:
%summary.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{commit}

%build
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%pyproject_save_files pitopd
%endif
install -Dm644 debian/pi-topd.service %{buildroot}%{_unitdir}/pi-topd.service
install -Dm644 debian/pt-reboot.service %{buildroot}%{_unitdir}/pt-reboot.service
install -Dm644 debian/pt-poweroff.service %{buildroot}%{_unitdir}/pt-poweroff.service
install -Dm644 %{SOURCE1} %{buildroot}%{_defaultlicensedir}/python3-%{pypi_name}/LICENSE

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

%dnl %if 0%{?fedora} > 43
%dnl %check
%dnl %pyproject_check_import
%dnl %endif

%if 0%{?fedora} <= 41 || 0%{?rhel}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/pi-topd
%{_bindir}/pt-poweroff
%{_bindir}/pt-reboot
%python3_sitelib/tests/__init__.py
%python3_sitelib/tests/__pycache__/*.cpython-*.pyc
%python3_sitelib/tests/test_config_parser.py
%{_unitdir}/pi-topd.service
%{_unitdir}/pt-reboot.service
%{_unitdir}/pt-poweroff.service
%else
%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/pi-topd
%{_bindir}/pt-poweroff
%{_bindir}/pt-reboot
%python3_sitelib/tests/__init__.py
%python3_sitelib/tests/__pycache__/*.cpython-*.pyc
%python3_sitelib/tests/test_config_parser.py
%{_unitdir}/pi-topd.service
%{_unitdir}/pt-reboot.service
%{_unitdir}/pt-poweroff.service
%endif

%changelog
* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com> - 5.7.0-1
- Install files properly, update script
* Sun Oct 26 2025 Jaiden Riordan <jade@fyralabs.com> - 5.7.0-1
- ehehehe :3
