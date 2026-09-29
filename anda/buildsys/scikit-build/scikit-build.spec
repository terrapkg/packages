%global pypi_name scikit-build
%global _desc Improved build system generator for Python C/C++/Fortran/Cython extensions.

Name:			python-%{pypi_name}
Version:		0.19.1
Release:		1%{?dist}
Summary:		Improved build system generator for Python C/C++/Fortran/Cython extensions
License:		MIT
URL:			https://scikit-build.readthedocs.io/
Source0:		%{pypi_source scikit_build}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-hatchling
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
BuildRequires:  python3dist(hatch-vcs)

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files skbuild

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/*
%license LICENSE

%changelog
* Wed Sep 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
