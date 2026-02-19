%global pypi_name av
%global _desc Pythonic bindings for FFmpeg's libraries.

Name:			python-%{pypi_name}
Version:		16.1.0
Release:		1%?dist
Summary:		Pythonic bindings for FFmpeg's libraries
License:		BSD-3-Clause
URL:			https://pyav.basswood-io.com/docs/stable/
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-poetry-core
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cython
BuildRequires:  gcc
BuildRequires:  pkgconfig(libavdevice)

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n av-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files av

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md AUTHORS.rst
%license LICENSE.txt
%{python3_sitearch}/av-%version.dist-info/licenses/__pycache__/*
%{_bindir}/pyav

%changelog
* Fri Jan 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
