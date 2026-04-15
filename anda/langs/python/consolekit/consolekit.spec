%global pypi_name consolekit
%global _desc Additional utilities for click.

Name:			python-%{pypi_name}
Version:		1.13.0
Release:		1%?dist
Summary:		Additional utilities for click
License:		MIT
URL:			https://consolekit.readthedocs.io/en/latest/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-flit-core

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
%doc README.rst
%license LICENSE

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
