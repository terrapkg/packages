%global pypi_name srctools
%global _desc Modules for working with Valve's Source Engine file formats.

Name:			python-%{pypi_name}
Version:		2.7.0
Release:		1%{?dist}
Summary:		Modules for working with Valve's Source Engine file formats
License:		MIT
URL:			https://srctools.readthedocs.io/en/stable/
Source0:		%{pypi_source}

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-cython

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
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/src_build_scenes
%{_bindir}/src_collapse_manifest
%{_bindir}/src_diff
%{_bindir}/src_dump_parms
%{_bindir}/src_find_deps
%{_bindir}/src_mdl_mkdir

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
