%global pypi_name enum_tools
%global _desc Tools to expand Python's enum module.

Name:			python-%{pypi_name}
Version:		0.13.0
Release:		1%?dist
Summary:		Tools to expand Python's enum module
License:		LGPL-3.0-or-later
URL:			https://enum-tools.readthedocs.io/en/latest/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-whey

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       python3-enum-tools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n enum_tools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files enum_tools

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sun Mar 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
