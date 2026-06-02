## Taken from Fedora, but updated because this project isn't actually abandoned

%global giturl  https://github.com/jupyter/jupyter-sphinx

# Tests fail in Anda due to an expected /tmp file not existing there?
%bcond test 0

Name:           python-jupyter-sphinx
Version:        0.5.3
Release:        2%{?dist}
Summary:        Jupyter Sphinx extensions
License:        BSD-3-Clause
URL:            https://jupyter-sphinx.readthedocs.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/jupyter-sphinx-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(bash-kernel)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(ipywidgets)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%global _desc %{expand:
Jupyter-Sphinx enables running code embedded in Sphinx documentation and
embedding output of that code into the resulting document.  It has
support for rich output such as images and even Jupyter interactive
widgets.}

%description %_desc

%package -n python3-jupyter-sphinx
Summary:        %{summary}

%description -n python3-jupyter-sphinx %_desc

%package        doc
# The content is BSD-3-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.

%prep
%autosetup -n jupyter-sphinx-%{version} -p1

%build
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files jupyter_sphinx

%if %{with test}
%check
export JUPYTER_PLATFORM_DIRS=1
%pytest
%endif

%files -n python3-jupyter-sphinx -f %{pyproject_files}
%doc README.md

%files doc
%doc doc/build/html

%changelog
* Mon May 26 2025 Gilver E. <rockgrub@disroot.org> - 0.5.3-1
- Initial port from Fedora
