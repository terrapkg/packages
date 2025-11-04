%global pypi_name spake2
%global _desc pure-python implementation of the SPAKE2 Password-Authenticated Key Exchange algorithm.

Name:			python-%{pypi_name}
Version:		0.9
Release:		1%?dist
Summary:		pure-python implementation of the SPAKE2 Password-Authenticated Key Exchange algorithm
License:		MIT
URL:			https://github.com/warner/python-spake2
Source0:		%{pypi_source}
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
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n spake2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spake2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/spake2-%version.dist-info/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
