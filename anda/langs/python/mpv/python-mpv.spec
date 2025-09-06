%define debug_package %nil
%global pypi_name mpv
%global _desc python-mpv is a ctypes-based python interface to the mpv media player. It gives you more or less full control of all features of the player, just as the lua interface does.

Name:			python-%{pypi_name}
Version:		1.0.8
Release:		1%?dist
Summary:		Python interface to the awesome mpv media player
License:		GPL-2.0+ OR LGPL-2.1+
URL:			https://github.com/jaseg/python-mpv
Source0:		https://github.com/jaseg/python-mpv/archive/refs/tags/v%version.tar.gz
Requires:       mpv-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pip

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n python-mpv-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mpv

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.GPL LICENSE.LGPL
%ghost %python3_sitelib/__pycache__/mpv.cpython-*.pyc
%python3_sitelib/mpv.py

%changelog
%autochangelog
