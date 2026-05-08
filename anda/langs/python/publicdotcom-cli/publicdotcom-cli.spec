%global pypi_name publicdotcom_cli
%global real_name publicdotcom-cli
%global _desc Command-line client for the Public.com Trading API.

Name:			python-%{real_name}
Version:		1.1.0
Release:		1%?dist
Summary:		Command-line client for the Public.com Trading API
License:		Apache-2.0
URL:			https://github.com/PublicDotCom/publicdotcom-cli
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-hatchling

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
%pyproject_save_files %{pypi_name}

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/public

%changelog
* Thu May 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
