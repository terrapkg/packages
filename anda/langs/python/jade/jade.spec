%global pypi_name jade
%global _desc Exoplanet evolution code.

Name:			python-%{pypi_name}
Version:		0.1.0
Release:		1%?dist
Summary:		Exoplanet evolution code
License:		LGPL-3.0
URL:			https://gitlab.unige.ch/spice_dune/jade
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       jade
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n jade-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jade

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jade

%changelog
* Fri Jan 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
