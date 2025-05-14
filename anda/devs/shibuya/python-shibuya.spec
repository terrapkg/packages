%global pypi_name shibuya
%global _description %{expand:
A responsive, good looking with modern design documentation theme for Sphinx, with great supports for many sphinx extensions.}
%bcond docs 0

Name:           python-%{pypi_name}
Version:        2025.4.25
Release:        1%{?dist}
Summary:        A clean, responsive, and customizable Sphinx documentation theme with light/dark mode
License:        BSD-3-Clause
URL:            https://shibuya.lepture.com
%if %{with docs}
Source0:        https://github.com/lepture/shibuya/archive/refs/tags/%{version}.tar.gz
%else
Source0:        %{pypi_source}
%endif
BuildRequires:  python3-devel
BuildRequires:  python3dist(babel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
%if %{with docs}
BuildRequires:  python3dist(shibuya)
%endif
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(sphinx)
# This project is best used with its addons, hence this laundry list of weak deps
Recommends:     python3dist(babel)
Recommends:     python3dist(ipykernel)
Recommends:     python3dist(jupyter-sphinx)
Recommends:     python3dist(matplotlib)
Recommends:     python3dist(myst-parser)
Recommends:     python3dist(nbsphinx)
Recommends:     python3dist(numpy)
Recommends:     python3dist(numpydoc)
Recommends:     python3dist(pandas)
Recommends:     python3dist(sphinx-click)
Recommends:     python3dist(sphinx-contributors)
Recommends:     python3dist(sphinx-copybutton)
Recommends:     python3dist(sphinx-design)
Recommends:     python3dist(sphinx-docsearch)
Recommends:     python3dist(sphinx-sitemap)
Recommends:     python3dist(sphinx-sqlalchemy)
Recommends:     python3dist(sphinx-togglebutton)
Recommends:     python3dist(sphinxcontrib-mermaid)
Recommends:     python3dist(sphinxcontrib-video)
Recommends:     python3dist(sphinxcontrib-youtube)

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package -n     python3-%{pypi_name}-doc
Summary:        Doc files for Shibuya

%description -n python3-%{pypi_name}-doc
This package contains the official docs for Shibuya.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with docs}
PYTHONPATH=${PWD} sphinx-build docs build/_html -b dirhtml -a
%endif

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python3-%{pypi_name}-doc
%endif

%changelog
* Sat May 10 2025 Gilver E. <rockgrub@disroot.org> - 2025.4.25-1
- Initial package.
