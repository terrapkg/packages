%global pypi_name pyvcd
%global _desc Python package for writing Value Change Dump (VCD) files.

Name:			python-%{pypi_name}
Version:		0.4.1
Release:		1%?dist
Summary:		Python package for writing Value Change Dump (VCD) files
License:		MIT
URL:			https://github.com/SanDisk-Open-Source/pyvcd
Source0:		%url/releases/download/%version/pyvcd-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  git

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       pyvcd
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n pyvcd-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vcd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CODE_OF_CONDUCT.md CHANGELOG.rst
%license LICENSE.txt
%python3_sitelib/pyvcd-%version.dist-info/*

%changelog
* Sat Sep 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
