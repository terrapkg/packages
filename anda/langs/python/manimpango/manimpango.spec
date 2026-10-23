%define debug_package %{nil}

%global pypi_name manimpango
%global _desc ManimPango is a C binding for Pango using Cython

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        ManimPango is a C binding for Pango using Cython
License:        MIT
URL:            https://www.manim.community/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cython
BuildRequires:  gcc
BuildRequires:  pkgconfig(pango)

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

%changelog
