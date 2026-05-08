%global pypi_name synapse-s3-storage-provider
%global _desc Synapse storage provider to fetch and store media in Amazon S3.

Name:			python-%{pypi_name}
Version:		1.6.0
Release:		1%?dist
Summary:		Synapse storage provider to fetch and store media in Amazon S3
License:		Apache-2.0
URL:			https://github.com/matrix-org/synapse-s3-storage-provider
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       synapse-s3-storage-provider
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files s3_storage_provider

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%{_bindir}/s3_media_upload

%changelog
* Thu Oct 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
