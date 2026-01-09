%global pypi_name shibuya
%global _description %{expand:
A responsive, good looking with modern design documentation theme for Sphinx, with great supports for many sphinx extensions.}
# I would love to enable the docs but Fedora has stopped maintaining their jupyter-sphinx package with 42 and it is required to build them
%bcond docs 0

Name:           python-%{pypi_name}
Version:        2026.1.9
Release:        1%?dist
Summary:        A clean, responsive, and customizable Sphinx documentation theme with light/dark mode
License:        BSD-3-Clause
URL:            https://shibuya.lepture.com
%if %{with docs}
Source0:        https://github.com/lepture/shibuya/archive/refs/tags/%{version}.tar.gz
%else
Source0:        %{pypi_source}
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3dist(babel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
%if %{with docs}
BuildRequires:  python3dist(jupyter-sphinx)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(shibuya)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-design)
BuildRequires:  python3dist(sphinx-togglebutton)
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
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%if %{with docs}
sphinx-build docs build/_html -b dirhtml -a
pybabel extract -F babel.cfg src/shibuya/theme -o src/shibuya/locale/sphinx.pot
for l in de en es fr ja ko pt pt_BR zh zh_TW; do
pybabel init -D sphinx -i src/shibuya/locale/sphinx.pot -d src/shibuya/locale -l $l
pybabel update -D sphinx -i src/shibuya/locale/sphinx.pot -d src/shibuya/locale -l $l
pybabel compile -D sphinx -d src/shibuya/locale
done
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%endif

%if %{with docs}
%files -n python3-%{pypi_name}-doc
%doc build/_html/*
%doc src/shibuya/locale/{de,en,es,fr,ja,ko,pt,pt_BR,zh,zh_TW}
%endif

%changelog
* Sat May 10 2025 Gilver E. <rockgrub@disroot.org> - 2025.4.25-1
- Initial package.
