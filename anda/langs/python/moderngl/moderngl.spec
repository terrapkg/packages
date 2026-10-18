%define debug_package %{nil}

%global pypi_name moderngl
%global _desc Modern OpenGL binding for Python

Name:           python-%{pypi_name}
Version:        5.13.0
Release:        1%{?dist}
Summary:        Modern OpenGL binding for Python
License:        MIT
URL:            https://github.com/moderngl/moderngl
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++

Packager:       Jan200101 <sentrycraft123@gmail.com>

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
%{python3_sitearch}/__pycache__/_moderngl.cpython-*.opt-1.pyc
%{python3_sitearch}/__pycache__/_moderngl.cpython-*.pyc
%{python3_sitearch}/_moderngl.py
%{python3_sitearch}/%{pypi_name}-stubs

%changelog
