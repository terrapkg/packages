%global pypi_name buttplug
%global _desc Python implementation of core message system and client for the Buttplug Sex Toy Protocol Standard.

Name:			python-%{pypi_name}
Version:		1.0.0
Release:		1%?dist
Summary:		Python implementation of core message system and client for the Buttplug Sex Toy Protocol Standard
License:		BSD-3-Clause AND MIT AND Apache-2.0 AND X11
URL:			buttplug-py.docs.buttplug.io
Source0:		https://github.com/buttplugio/buttplug-py/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE

%changelog
* Fri Apr 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
