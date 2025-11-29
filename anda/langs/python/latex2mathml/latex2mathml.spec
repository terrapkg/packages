%global pypi_name latex2mathml
%global _desc Pure Python library for LaTeX to MathML conversion.

Name:			python-%{pypi_name}
Version:		3.78.1
Release:		1%?dist
Summary:		Pure Python library for LaTeX to MathML conversion
License:		MIT
URL:			https://github.com/roniemartinez/latex2mathml
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildRequires:  python3-installer
BuildRequires:  python3-build

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       latex2mathml
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n latex2mathml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files latex2mathml

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/l2m
%{_bindir}/latex2mathml
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/latex2mathml-%version.dist-info/*

%changelog
* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
