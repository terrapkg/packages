%global commit a73d561aa58b12afc3aa4ee80143dca87656688d
%global commit_date 20200219
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name py-spinners
%global _desc More than 60 spinners for terminal, python wrapper for amazing node library cli-spinners.

Name:			python-%{pypi_name}
Version:		0.11.1
Release:		1%?dist
Summary:		More than 60 spinners for terminal, python wrapper for amazing node library cli-spinners
License:		MIT
URL:			https://github.com/ManrajGrover/py-spinners
Source0:		%url/archive/%commit/py-spinners-%commit.tar.gz
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
Provides:       spinners
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n py-spinners-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spinners

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md DEVELOPMENT.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/spinners-0.0.24.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
