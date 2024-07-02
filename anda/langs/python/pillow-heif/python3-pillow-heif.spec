%global py3_incdir %(RPM_BUILD_ROOT= %{python3} -Ic 'import sysconfig; print(sysconfig.get_path("include"))')

%global srcname pillow-heif

# Dependencies are missing to build the documentation
%bcond_with doc

Name:           python-%{srcname}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Python library for working with HEIF images and plugin for Pillow

License:        BSD-3-Clause
URL:            https://github.com/bigcat88/pillow_heif
Source0:        https://github.com/bigcat88/pillow_heif/archive/refs/tags/v%{version}/pillow-heif-%{version}.tar.gz
Source1:        test.py

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pillow-devel
BuildRequires:  libheif-devel
%if %{with doc}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-copybutton
BuildRequires:  python%{python3_pkgversion}-sphinx-issues
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%endif

%description
Python library for working with HEIF images and plugin for Pillow

There are two subpackages: devel (development) and doc (documentation).

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Python library for working with HEIF images and plugin for Pillow
Requires:       python%{python3_pkgversion}-pillow
Requires:       libheif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Python library for working with HEIF images and plugin for Pillow

There are two subpackages: devel (development) and doc (documentation).

%package -n python%{python3_pkgversion}-%{srcname}-devel
Summary:        Development files for %{srcname}
Requires:       python%{python3_pkgversion}-devel, libheif-devel
Requires:       python%{python3_pkgversion}-%{srcname}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-devel}

%description -n python%{python3_pkgversion}-%{srcname}-devel
Development files for %{srcname}.


%package -n python%{python3_pkgversion}-%{srcname}-doc
Summary:        Documentation for %{srcname}
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-doc}

%description -n python%{python3_pkgversion}-%{srcname}-doc
Documentation for %{srcname}.


%prep
%autosetup -p1 -n pillow_heif-%{version}


%build
# Native build
%py3_build

# Doc build
%if %{with doc}
PYTHONPATH=$(echo $PWD/build/lib.linux-*) make -C docs html BUILDDIR=_build_py3 SPHINXBUILD=sphinx-build-%python3_version
rm -f docs/_build_py3/html/.buildinfo
%endif


%install
# Native build
%py3_install

%check
# Check Python 3 modules
cp %{SOURCE1} $(echo $PWD/build/lib.linux-*)/
pushd build/lib.linux-*
PYTHONPATH=$PWD %{__python3} test.py
pytest pillow_heif && echo "Test done"
popd

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{python3_sitearch}/pillow_heif/
%{python3_sitearch}/pillow_heif-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/_pillow_heif.*.so

%files -n python%{python3_pkgversion}-%{srcname}-devel

%if %{with doc}
%files -n python%{python3_pkgversion}-%{srcname}-doc
%doc docs/_build_py3/html
%endif

%changelog
* Thu Jun 27 2024 Trung Lê <8@tle.id.au> - 0.16.0-1
- Initial RPM package
