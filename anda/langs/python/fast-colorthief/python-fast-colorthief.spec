%global pypi_name fast-colorthief
%global debug_package %{nil}
%bcond docs 1
# Fedora packages pybind11 but not the test module kill me
%bcond test 0

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        2%{?dist}
Summary:        Faster version of Colorthief
License:        MIT
URL:            https://github.com/bedapisl/fast-colorthief
Source0:        %{pypi_source}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pybind11-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
# This package is not buildable on EL due to this dep. There's unfortunately not much I can do about this.
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3dist(breathe)
%if %{with test}
BuildRequires:  python3dist(colorthief)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pybind11-tests)
%endif
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-moderncmakedomain)
BuildRequires:  python3dist(sphinx-copybutton)
Packager:       Gilver E. <roachy@fyralabs.com>

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
## This is not a fully Python project and is mostly C++
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%if %{with docs}
# Generate docs
# Only works in English currently. Sad.
PYTHONPATH=${PWD} sphinx-build pybind11/docs html -D language=en
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%endif

%if %{with test}
%check
%pytest
%endif

%files -n python3-%{pypi_name}
%license pybind11/LICENSE
%doc PKG-INFO
%doc README.md
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/fast_colorthief.py
%{python3_sitearch}/version.py
%{python3_sitearch}/fast_colorthief_backend.cpython-*-%{_arch}-linux-gnu.so
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitearch}/fast_colorthief-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitearch}/fast_colorthief-%{version}.dist-info/
%endif

%if %{with docs}
%files -n python3-%{pypi_name}-doc
%doc html/*
%endif

%changelog
* Sun May 11 2025 Gilver E. <rockgrub@disroot.org> - 0.0.5-1
- Initial package.
