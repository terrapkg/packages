%global pypi_name asyncclick
%global _desc Python composable command line utility, trio-compatible version.

Name:			python-%{pypi_name}
Version:		8.4.2.1
Release:		1%{?dist}
Summary:		Python composable command line utility, trio-compatible version
License:		BSD-3-Clause
URL:			https://github.com/python-trio/asyncclick/
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-flit-core
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
* Sun Jun 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
