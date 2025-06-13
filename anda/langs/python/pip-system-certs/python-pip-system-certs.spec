# Created by pyp2rpm-3.3.10
%global pypi_name pip-system-certs
%global pypi_version 5.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Live patches pip to use system certs by default

License:        BSD-2-Clause
URL:            https://gitlab.com/alelec/pip-system-certs
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pip_system_certs-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel python3-pip python3dist(setuptools) python3dist(wheel) git-core


%description
This package patches pip and requests at runtime to use
certificates from the default system store (rather than the bundled certs
ca). This will allow pip to verify tls/ssl connections to servers who's cert is
trusted by your system install.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(wrapt) >= 1.10.4
%description -n python3-%{pypi_name}
This package patches pip and requests at runtime to use
certificates from the default system store (rather than the bundled certs
ca). This will allow pip to verify tls/ssl connections to servers who's cert is
trusted by your system install.

%prep
%autosetup -n pip_system_certs-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
pip install git-versioner
%if 0%{?fedora} <= 41
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41
%py3_install
%else
%pyproject_install

%pyproject_save_files pip_system_certs
%endif

%if 0%{?fedora} <= 41
%files -n python3-%{pypi_name}
%{python3_sitelib}/python_pip_certs/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%files -n python3-%{pypi_name} -f %pyproject_files
%endif
%license LICENSE
%doc README.rst
%python3_sitelib/pip_system_certs.pth

%changelog
* Thu Apr 04 2024 madomado <madonuko@outlook.com> - 4.0-1
- Initial package.
