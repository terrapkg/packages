%global pypi_name fast-colorthief
%global debug_package %{nil}
%bcond docs 1

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Faster version of Colorthief
License:        MIT
URL:            https://github.com/bedapisl/fast-colorthief
Source0:        %{pypi_source}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinxcontrib_moderncmakedomain
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-copybutton)
Packager:       Gilver E. <rockgrub@disroot.org>

%description
A Python module for selecting most dominant colors in the image.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(numpy)
Requires:       python3dist(pillow)

%description -n python3-%{pypi_name}
A Python module for selecting most dominant colors in the image.

A faster version of the original Colorthief.

%if %{with docs}
%package -n     python3-%{pypi_name}-doc
Summary:        Docs for %{pypi_name}
BuildArch:      noarch

%description -n python3-%{pypi_name}-doc
Documentation files for %{pypi_name}
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
# This is not a fully Python project and is mostly C++
%pyproject_wheel
%cmake
%cmake_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 pybind11/docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%cmake_install

%files -n python3-%{pypi_name}
%license pybind11/LICENSE
%doc PKG-INFO
%doc README.md
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/fast_colorthief.py
%{python3_sitearch}/version.py
%{python3_sitearch}/fast_colorthief_backend.cpython-*-%{_arch}-linux-gnu.so
%{python3_sitearch}/fast_colorthief-%{version}.dist-info

%if %{with docs}
%files -n python3-%{pypi_name}-doc
%doc html/*
%endif

%changelog
* Sun May 11 2025 Gilver E. <rockgrub@disroot.org> - 0.0.5-1
- Initial package.
