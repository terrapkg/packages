%define debug_package %{nil}

%global pypi_name soxr
%global _desc Fast and high quality sample-rate conversion library for Python.

Name:			python-%{pypi_name}
Version:		1.0.0
Release:		1%?dist
Summary:		Fast and high quality sample-rate conversion library for Python
License:		LGPL-2.1
URL:			https://github.com/dofuuz/python-soxr
Source0:		https://github.com/dofuuz/python-soxr/archive/refs/tags/v%version.tar.gz
# This package is intentionally not noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-scikit-build-core
BuildRequires:  python3-pybind11
BuildRequires:  python3-nanobind
BuildRequires:  gcc-c++
BuildRequires:  cmake

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%git_clone

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files soxr

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md BUILDING.md
%license LICENSE.txt COPYING.LGPL

%changelog
* Fri Dec 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
