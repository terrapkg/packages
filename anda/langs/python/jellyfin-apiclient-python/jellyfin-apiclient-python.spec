%global pypi_name jellyfin-apiclient-python
%global _desc Python API Client for Jellyfin.

Name:			python-%{pypi_name}
Version:		1.14.0
Release:		1%{?dist}
Summary:		Python API Client for Jellyfin
License:		GPL-3.0-or-later
URL:			https://github.com/jellyfin/jellyfin-apiclient-python
Source0:		%{pypi_source jellyfin_apiclient_python}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       jellyfin-apiclient-python
Provides:       jellyfin-apiclient
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jellyfin_apiclient_python

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
* Sun Dec 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
