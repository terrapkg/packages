%global pypi_name halo
%global _desc Beautiful spinners for terminal, IPython and Jupyter.

Name:			python-%{pypi_name}
Version:		0.0.31
Release:		1%?dist
Summary:		Beautiful spinners for terminal, IPython and Jupyter
License:		MIT
URL:			https://github.com/manrajgrover/halo
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       halo
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n halo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files halo

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/halo-%{version}.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
