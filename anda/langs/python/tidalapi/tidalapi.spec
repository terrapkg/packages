%global pypi_name tidalapi
%global _desc Python API for TIDAL music streaming service.

Name:			python-%{pypi_name}
Version:		0.8.11
Release:		1%?dist
Summary:		Python API for TIDAL music streaming service
License:		LGPL-3.0-or-later
URL:			https://github.com/matrix-org/synapse-s3-storage-provider
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

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
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE

%changelog
* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
