%global pypi_name py7zr
%global _desc Pure python 7-zip library.

%global _python_dist_allow_version_zero 1

Name:			python-%{pypi_name}
Version:		1.1.3
Release:		3%{?dist}
Summary:		Pure python 7-zip library
License:		LGPL-2.1-or-later
URL:			https://py7zr.readthedocs.io/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%pyproject_patch_dependency multivolumefile:drop_constraints
%pyproject_patch_dependency inflate64:drop_constraints
%pyproject_patch_dependency pybcj:drop_constraints
%pyproject_patch_dependency pyppmd:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/py7zr

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
