%global pypi_name PGPy13
%global _desc PGPy is a Python library for implementing Pretty Good Privacy into Python programs, conforming to the OpenPGP specification per RFC 4880.

Name:			python-%{pypi_name}
Version:		0.6.1rc1
Release:		1%?dist
Summary:		Pretty Good Privacy for Python
License:		BSD-3-Clause
URL:			https://github.com/memory/PGPy
Source0:		https://files.pythonhosted.org/packages/source/P/PGPy13/pgpy13-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3.10
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  git

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       PGPy13
Provides:       pgpy13
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n pgpy13-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pgpy

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
