%define _unpackaged_files_terminate_build 0

%global pypi_name curl_cffi
%global _desc Python binding for curl-impersonate fork via cffi.
%global _version 0.14.0b2

Name:			python-%{pypi_name}
Version:		0.13.0
Release:		1%?dist
Summary:		Python binding for curl-impersonate fork via cffi..
License:		MIT
URL:			https://github.com/lexiforest/curl_cffi
Source0:                %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  curl-impersonate-chrome-devel

Packager:	    Metcya <metcya@gmail.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
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
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/*
%{python3_sitelib}/%{pypi_name}/*.{py,so,typed}
%{python3_sitelib}/%{pypi_name}/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}/requests/*.py
%{python3_sitelib}/%{pypi_name}/requests/__pycache__/*.pyc

%changelog
* Sun Nov 02 2025 Metcya <metcya@gmail.com>
- Initial commit
