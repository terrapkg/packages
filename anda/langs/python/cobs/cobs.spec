%global pypi_name cobs
%global _desc Python functions for encoding and decoding COBS.

Name:			python-%{pypi_name}
Version:		1.2.2
Release:		1%?dist
Summary:		Python functions for encoding and decoding COBS
License:		MIT
URL:			https://pypi.org/project/cobs/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       cobs
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n cobs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cobs

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Sun Sep 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
