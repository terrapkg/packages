%global pypi_name spinners
%global _desc More than 60 spinners for terminal, python wrapper for amazing node library cli-spinners.

Name:			python-%{pypi_name}
Version:		0.0.24
Release:		1%?dist
Summary:		More than 60 spinners for terminal, python wrapper for amazing node library cli-spinners
License:		MIT
URL:			https://pypi.org/project/spinners/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       py-spinners
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
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/spinners-%{version}.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
