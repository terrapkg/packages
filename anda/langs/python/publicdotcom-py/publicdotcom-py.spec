%global pypi_name publicdotcom_py
%global real_name publicdotcom-py
%global _desc A Python SDK for interacting with the Public Trading API, providing a simple and intuitive interface for trading operations, market data retrieval, and account management.

Name:			python-%{real_name}
Version:		0.1.14
Release:		1%{?dist}
Summary:		Python SDK for interacting with the Public Trading API
License:		Apache-2.0
URL:			https://github.com/PublicDotCom/publicdotcom-py
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{real_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files public_api_sdk

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.md
%license LICENCE

%changelog
* Thu May 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
