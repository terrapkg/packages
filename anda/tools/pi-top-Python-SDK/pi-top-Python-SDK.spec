%global pypi_name pitop
%global _desc A simple, modular interface for interacting with a pi-top and its related accessories and components.
%global ver 0.35.0-4
%global sanitized_ver %(echo %{ver} | sed 's/-//g')

Name:			python-%{pypi_name}
Version:		%{sanitized_ver}
Release:		1%?dist
Summary:		pi-top's Python SDK pitop package
License:		Apache-2.0
URL:			https://github.com/pi-top/pi-top-Python-SDK
Source0:		%{url}/archive/v%{ver}/%{name}-%{ver}.tar.gz
BuildArch:      noarch

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
Provides:       pitop
Provides:       pi-top-Python-SDK
Provides:       pi-top-python-sdk
Provides:       pi-top-sdk
Provides:       pitop-sdk
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%dnl %package battery

%prep
%autosetup -n pi-top-Python-SDK-%{ver}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pitop

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
