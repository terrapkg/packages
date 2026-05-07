%global pypi_name pyproject-parser
%global _desc Parser for 'pyproject.toml'

Name:			python-%{pypi_name}
Version:		0.14.0
Release:		1%?dist
Summary:		Parser for 'pyproject.toml'
License:		MIT
URL:			https://pyproject-parser.readthedocs.io/en/latest/
Source0:		https://github.com/repo-helper/pyproject-parser/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-hatch-requirements-txt

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       pyvcd
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyproject_parser

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pyproject-fmt
%{_bindir}/pyproject-info
%{_bindir}/pyproject-parser
%{_bindir}/check-pyproject

%changelog
* Sat Sep 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
