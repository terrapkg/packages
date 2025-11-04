%global pypi_name fowl
%global _desc Forward over Wormhole: streams over magic-wormhole Dilation connections.

Name:			python-%{pypi_name}
Version:		25.7.0
Release:		1%?dist
Summary:		Forward over Wormhole: streams over magic-wormhole Dilation connections
License:		MIT
URL:			https://github.com/meejah/fowl
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       fowl
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n fowl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fowl
ls -la

%files -n python3-%{pypi_name} -f %{pyproject_files}
# Includes README
%doc docs/*.rst
%license LICENSE
%{_bindir}/fowl
%{_bindir}/fowld
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/fowl-%version.dist-info/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
