# NOT made with pyp2rpm because it had no freaking clue what to do with this project
# Looking at the sources the real name should be sphinxcontrib-moderncmakedomain but it builds as sphinxcontrib_moderncmakedomain????
%global pypi_name sphinxcontrib_moderncmakedomain
%global real_name sphinxcontrib-moderncmakedomain

Name:           python-%{real_name}
Version:        3.29.0
Release:        1%{?dist}
Summary:        Sphinx domain for modern CMake
License:        BSD-3-Clause
URL:            https://github.com/scikit-build/moderncmakedomain
Source0:        %{pypi_source}
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Modern CMake domain entries, originally from Kitware.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(hatchling)
Requires:       python3dist(sphinx)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Modern CMake domain entries, originally from Kitware.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest tests/*.py

%files -n python3-%{pypi_name}
%doc     PKG-INFO
%doc     README.md
%license LICENSE
%{python3_sitelib}/sphinxcontrib/moderncmakedomain
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Sat May 10 2025 Gilver E. <rockgrub@disroot.org> - 3.29.0-1
- Initial package.
