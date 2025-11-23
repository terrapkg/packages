%global pypi_name pyzmq
%global _desc Python bindings for zeromq.

Name:			python-%{pypi_name}
Version:		27.1.0
Release:		1%?dist
Summary:		Python bindings for zeromq
License:		MIT
URL:			https://github.com/zeromq/pyzmq
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-scikit-build-core
BuildRequires:  cmake gcc gcc-c++ python3-cython

BuildRequires:  python3-wheel
BuildRequires:  python3-pyproject-metadata
BuildRequires:  python3-importlib-metadata

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
%python3_sitelib/zmq/*.py
%python3_sitelib/zmq/auth/*.py
%python3_sitelib/zmq/auth/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/backend/*.py
%python3_sitelib/zmq/backend/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/devices/*.py
%python3_sitelib/zmq/devices/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/eventloop/*.py
%python3_sitelib/zmq/eventloop/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/green/*.py
%python3_sitelib/zmq/green/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/log/*.py
%python3_sitelib/zmq/log/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/ssh/*.py
%python3_sitelib/zmq/ssh/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/sugar/*.py
%python3_sitelib/zmq/sugar/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/tests/*.py
%python3_sitelib/zmq/tests/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/utils/*.py
%python3_sitelib/zmq/utils/__pycache__/*.cpython-*.pyc
%python3_sitelib/__pycache__/*.cpython-*.pyc
%python3_sitelib/zmq/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/spinners-%{version}.dist-info/*
%python3_sitelib/zmq/constants.py
%python3_sitelib/zmq/decorators.py
%python3_sitelib/zmq/error.py
%python3_sitelib/zmq/py.typed

%changelog
* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
