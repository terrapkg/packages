%global pypi_name numba

Name:			python-%{pypi_name}
Version:		0.64.0
Release:		1%?dist
Summary:	    NumPy aware dynamic Python compiler using LLVM
License:		BSD-2-Clause AND MIT AND BSD-3-Clause
URL:			https://numba.pydata.org
# PyPi source does not include all files
Source0:		https://github.com/numba/numba/archive/refs/tags/%version.tar.gz
# This package is intentionally not noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling
BuildRequires:  python3-numpy
BuildRequires:  gcc-c++

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc. It uses the LLVM compiler project to generate machine code from Python syntax.

Numba can compile a large subset of numerically-focused Python, including many NumPy functions. Additionally, Numba has support for automatic parallelization of loops, generation of GPU-accelerated code, and creation of ufuncs and C callbacks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       numba
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc. It uses the LLVM compiler project to generate machine code from Python syntax.

Numba can compile a large subset of numerically-focused Python, including many NumPy functions. Additionally, Numba has support for automatic parallelization of loops, generation of GPU-accelerated code, and creation of ufuncs and C callbacks.

%prep
%autosetup -n numba-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files numba

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGE_LOG SECURITY.md CONTRIBUTING.md
%license LICENSE LICENSES.third-party
%{_bindir}/numba

%changelog
* Fri Dec 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
