%global pypi_name smbus2
%global _desc A drop-in replacement for smbus-cffi/smbus-python in pure Python.

Name:			python-%{pypi_name}
Version:		0.5.0
Release:		1%?dist
Summary:		A drop-in replacement for smbus-cffi/smbus-python in pure Python
License:		MIT
URL:			https://github.com/kplindegaard/smbus2
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       smbus2
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n smbus2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files smbus2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/smbus2-%version.dist-info/*

%changelog
* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
