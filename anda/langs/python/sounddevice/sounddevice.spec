%global pypi_name sounddevice
%global _desc 🔉 Play and Record Sound with Python 🐍.

Name:			python-%{pypi_name}
Version:		0.5.5
Release:		1%?dist
Summary:		🔉 Play and Record Sound with Python 🐍
License:		MIT
URL:			https://python-sounddevice.rtfd.io/
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
Provides:       sounddevice
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n sounddevice-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sounddevice

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CONTRIBUTING.rst NEWS.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/sounddevice-%version.dist-info/*

%changelog
* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
