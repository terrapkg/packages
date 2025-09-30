%global pypi_name jschon
%global _desc An object-oriented JSON Schema implementation for Python.

Name:			python-%{pypi_name}
Version:		0.11.1
Release:		2%?dist
Summary:		An object-oriented JSON Schema implementation for Python
License:		MIT
URL:			https://github.com/marksparkza/jschon
Source0:		%url/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Requires:       python3-requests
Requires:       python3-rfc3986

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       jschon
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%git_clone %{url}.git %{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jschon

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CONTRIBUTING.rst CHANGELOG.rst TESTING.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%{python3_sitelib}/jschon/catalog/json-schema-2019-09/*.json
%{python3_sitelib}/jschon/catalog/json-schema-2020-12/*.json
%python3_sitelib/jschon-%version.dist-info/*

%changelog
* Sun Sep 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
