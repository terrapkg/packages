%global pypi_name modern_colorthief
%bcond bootstrap 0
%bcond docs %{without bootstrap}
%bcond test %{without bootstrap}

# The srcrpm is not prefixed with Python because the source is mostly Rust
Name:          modern-colorthief
Version:       0.1.12
Release:       1%?dist
Summary:       ColorThief reimagined
SourceLicense: MIT
License:       (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND BSD-2-Clause AND (CC0-1.0 OR Apache-2.0) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:           https://modern-colorthief.readthedocs.io
Source0:       %{pypi_source}
BuildRequires: anda-srpm-macros
BuildRequires: cargo
BuildRequires: cargo-rpm-macros
BuildRequires: maturin
BuildRequires: mold
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python3dist(pip)
BuildRequires: python3dist(setuptools)
%if %{with docs}
BuildRequires: python3dist(modern-colorthief)
BuildRequires: python3dist(myst-parser)
BuildRequires: python3dist(shibuya)
BuildRequires: python3dist(sphinx)
%endif
%if %{with test}
%if 0%{?fedora} > 40
BuildRequires: poetry
BuildRequires: python3dist(poetry)
%endif
BuildRequires: python3dist(colorthief)
BuildRequires: python3dist(fast-colorthief)
BuildRequires: python3dist(pytest)
%endif

%description
Colorthief but with modern code.

%package -n      python3-%{name}
Summary:         %{summary}
License:         MIT

%description -n python3-%{name}
Colorthief but with modern code.

%if %{with docs}
%package -n      python3-%{name}-doc
Summary:         Doc files for Modern Colorthief
License:         MIT
BuildArch:       noarch

%description -n python3-%{name}-doc
Documentation for Modern Colorthief.
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
%cargo_prep_online

%build
%pyproject_wheel

%if %{with docs}
# Generates the docs in all languages Sphinx can translate most or all of the docs for this project in
for l in ca cs cy da de el en es et eu fa fr he hi hi_IN hr hu id it ja ko lt lv nb_NO nl pl pt pt_BR pt_PT ro ru sk sq sv tr zh_CN zh_TW; do
sphinx-build docs html/$l -D language=$l
# Remove the sphinx-build leftovers
rm -rf html/$l/.{doctrees,buildinfo}
done
%endif

%install
%pyproject_install

%{cargo_license_online} > LICENSE.dependencies

%if %{with test}
%check
# Poetry doesn't exist on EL and is too old on 40
%if 0%{?fedora} <= 40 || 0%{?rhel}
%pytest tests/*.py
%else
# This is in the wrong spot in pyproject.toml and Poetry hates it
# May seem like defeating the purpose of testing but the other tests can be useful
sed -iE 's/python = ">=3.9,<3.14"//' pyproject.toml
poetry run pytest
%endif
%endif

%files -n python3-%{name}
%doc DIFFERENCES.md
%doc PKG-INFO
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%if %{with docs}
%files -n python3-%{name}-doc
%doc html/*
%endif

%changelog
* Mon Sep 1 2025 Gilver E. <rockgrub@disroot.org> - 0.1.7-2
- Rebuilt for Python 3.14
* Tue May 13 2025 Gilver E. <rockgrub@disroot.org> - 0.1.7-1
- Initial package
