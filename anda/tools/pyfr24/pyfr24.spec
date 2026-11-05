%global pypi_name pyfr24
%global _desc A Python client for the Flightradar24 API with CLI support.


Name:			python-%{pypi_name}
Version:		0.3.0
Release:		1%{?dist}
Summary:		A Python client for the Flightradar24 API with CLI support
License:		CC0-1.0
URL:			https://github.com/stiles/pyfr24
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3dist(setuptools)

Packager:	      Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/tests/*

%changelog
* Thu Nov 05 2026 Owen Zimmerman <owen@fyralabs.com> - 0.3.0-1
- Initial commit
