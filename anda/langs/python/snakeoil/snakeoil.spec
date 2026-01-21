%global pypi_name snakeoil
%global _desc A python library that implements optimized versions of common functionality.

Name:			python-%{pypi_name}
Version:		0.11.0
Release:		1%?dist
Summary:		Implements optimized versions of common functionality
License:		BSD-3-Clause
URL:			https://pkgcore.github.io/snakeoil
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-flit-core
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
%autosetup -n snakeoil-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files snakeoil

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
