%global pypi_name deprecation-alias
%global _desc A wrapper around 'deprecation' providing support for deprecated aliases.

Name:			python-%{pypi_name}
Version:		0.4.0
Release:		1%?dist
Summary:		A wrapper around 'deprecation' providing support for deprecated aliases
License:		Apache-2.0
URL:			https://github.com/domdfcoding/deprecation-alias
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-hatchling
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-hatch-requirements-txt
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
%pyproject_save_files deprecation_alias

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
