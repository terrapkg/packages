%define debug_package %{nil}

%global pypi_name pyglm
%global _desc Fast OpenGL Mathematics (GLM) for Python

Name:           python-%{pypi_name}
Version:        2.8.3
Release:        1%{?dist}
Summary:        Fast OpenGL Mathematics (GLM) for Python
License:        Zlib
URL:            https://github.com/jared-hughes/isosurfaces
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  gcc gcc-c++

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
%{python3_sitearch}/glm
%{python3_sitearch}/%{pypi_name}-stubs

%changelog
