%global commit eb527ec951e3d02c828efdb56e9f78e364c109b2
%global commit_date 20200219
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name log_symbols
%global _desc Colored symbols for various log levels for Python.

Name:			python-%{pypi_name}
Version:		%commit_date.%shortcommit
Release:		1%?dist
Summary:		Colored symbols for various log levels for Python
License:		MIT
URL:			https://github.com/manrajgrover/py-log-symbols
Source0:		%url/archive/%commit/py-log-symbols-%commit.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       log_symbols
Provides:       py-log-symbols
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n py-log-symbols-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files log_symbols

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md DEVELOPMENT.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/log_symbols-0.0.14.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
