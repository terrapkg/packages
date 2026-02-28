%global pypi_name iterable-io
%global _desc Python library to adapt iterables to a file-like interface.

Name:			python-%{pypi_name}
Version:		1.0.1
Release:		1%?dist
Summary:		Python library to adapt iterables to a file-like interface

# According to README
License:		LGPL-3.0-only

URL:			https://github.com/pR0Ps/iterable-io
Source0:		%{pypi_source}
Source1:        LICENSE.txt
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       iterable-io
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n iterable-io-%{version}

%build
%pyproject_wheel

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE
%pyproject_install
%pyproject_save_files iterableio

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_defaultlicensedir}/%{name}/LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/iterable_io-%version.dist-info/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
