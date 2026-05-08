%global pypi_name milc
%global _desc Batteries-Included Python 3 CLI Framework.

Name:			python-%{pypi_name}
Version:		1.9.1
Release:		1%?dist
Summary:		Batteries-Included Python 3 CLI Framework
License:		MIT
URL:			https://github.com/clueboard/milc
Source0:		%url/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Requires:       python3-platformdirs
Requires:       python3-argcomplete
Requires:       python3-colorama
Requires:       python3-halo

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       milc
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n milc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files milc

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md COMPARISONS.md CHANGELOG.rst
%license LICENSE
%{_bindir}/milc-color
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/milc-%version.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
