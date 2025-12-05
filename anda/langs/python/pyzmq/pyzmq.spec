%define debug_package %{nil}

%global pypi_name pyzmq
%global _desc Python bindings for zeromq.

Name:			python-%{pypi_name}
Version:		27.1.0
Release:		1%?dist
Summary:		Python bindings for zeromq
License:		MIT
URL:			https://github.com/zeromq/pyzmq
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-scikit-build-core
BuildRequires:  python3-cython

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       pyzmq
Provides:       %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zmq

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md AUTHORS.md CONTRIBUTING.md SECURITY.md
%license LICENSE.md

%changelog
* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
