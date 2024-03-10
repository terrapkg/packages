# Created by pyp2rpm-3.3.10
%global pypi_name jellyfin-apiclient-python
%global pypi_version 1.9.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python API client for Jellyfin

License:        GPLv3
URL:            https://github.com/iwalton3/jellyfin-apiclient-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Jellyfin ApiClient PythonThis is the API client from Jellyfin Kodi extracted
as a python package so that other users may use the API without maintaining a
fork of the API client. Please note that this API client is not complete. You
may have to add API calls to perform certain tasks. Please see **Contributing**
below. UsageThis client can be installed with pip3 install jellyfin-
apiclient-...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(certifi)
Requires:       python3dist(requests)
Requires:       python3dist(urllib3)
Requires:       python3dist(websocket-client)
%description -n python3-%{pypi_name}
 Jellyfin ApiClient PythonThis is the API client from Jellyfin Kodi extracted
as a python package so that other users may use the API without maintaining a
fork of the API client. Please note that this API client is not complete. You
may have to add API calls to perform certain tasks. Please see **Contributing**
below. UsageThis client can be installed with pip3 install jellyfin-
apiclient-...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/jellyfin_apiclient_python
%{python3_sitelib}/jellyfin_apiclient_python-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Dec 17 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 1.9.2-1
- Initial package.
