%global pypi_name mdtex2html
%global _desc python3-library to convert Markdown with included LaTeX-Formulas to HTML with MathML.

Name:			python-%{pypi_name}
Version:		1.3.2
Release:		1%?dist
Summary:		python3-library to convert Markdown with included LaTeX-Formulas to HTML with MathML
License:		LGPL-2.1
URL:			https://github.com/polarwinkel/mdtex2html
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
Provides:       mdtex2html
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n mdtex2html-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdtex2html

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/mdtex2html-%version.dist-info/*

%changelog
* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
