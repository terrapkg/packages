%global pypi_name zipstream-ng
%global _desc 🔉 A modern and easy to use streamable zip file generator

Name:			python-%{pypi_name}
Version:		1.9.0
Release:		1%?dist
Summary:		A modern and easy to use streamable zip file generator
License:		LGPL-3.0-only
URL:			https://github.com/pR0Ps/zipstream-ng
Source0:		%url/archive/refs/tags/v%version.tar.gz
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
Provides:       zipstream-ng
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n zipstream-ng-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zipstream

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md docs/zipserver.rst
%license LICENSE
%{_bindir}/zipserver
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/zipstream_ng-%version.dist-info/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
