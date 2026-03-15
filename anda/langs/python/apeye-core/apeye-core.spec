%global pypi_name apeye_core
%global _desc Core (offline) functionality for the apeye library.

Name:			python-%{pypi_name}
Version:		1.1.5
Release:		1%?dist
Summary:		Core (offline) functionality for the apeye library
License:		BSD-3-Clause
URL:			https://github.com/domdfcoding/apeye-core
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-hatch-requirements-txt

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files apeye_core

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
