# NOT made with pyp2rpm because it had no freaking clue what to do with this project
# Looking at the sources the real name should be sphinxcontrib-moderncmakedomain but it builds as sphinxcontrib_moderncmakedomain????
%global pypi_name sphinxcontrib_moderncmakedomain
%global real_name sphinxcontrib-moderncmakedomain

# Tests fail on EL even with Pytest due to the package versions
%if 0%{?rhel}
%bcond test 0
%else
%bcond test 1
%endif

Name:           python-%{real_name}
Version:        3.29.0
Release:        3%{?dist}
Summary:        Sphinx domain for modern CMake
License:        BSD-3-Clause
URL:            https://github.com/scikit-build/moderncmakedomain
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling)
%if 0%{?fedora}
BuildRequires:  python3dist(nox)
%endif
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Modern CMake domain entries, originally from Kitware.

%package -n     python3-%{real_name}
Summary:        %{summary}
Requires:       python3dist(hatchling)
Requires:       python3dist(sphinx)
Obsoletes:      python3-%{pypi_name} < 3.29.0-2
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
Modern CMake domain entries, originally from Kitware.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with test}
%check
nox -s tests
%endif

%files -n python3-%{real_name}
%doc     PKG-INFO
%doc     README.md
%license LICENSE
%{python3_sitelib}/sphinxcontrib/moderncmakedomain
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Sat May 10 2025 Gilver E. <rockgrub@disroot.org> - 3.29.0-1
- Initial package.
