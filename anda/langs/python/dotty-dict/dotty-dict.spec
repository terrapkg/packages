%global pypi_name dotty_dict
%global _desc Dictionary wrapper for quick access to deeply nested keys.

Name:			python-%{pypi_name}
Version:		1.3.1
Release:		1%?dist
Summary:		Dictionary wrapper for quick access to deeply nested keys
License:		MIT
URL:			https://github.com/pawelzny/dotty_dict
Source0:		%url/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-poetry-core
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       dotty_dict
Provides:       dotty-dict
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n dotty_dict-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dotty_dict

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS.rst CONTRIBUTING.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/dotty_dict-%version.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
