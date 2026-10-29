%global pypi_name skia-pathops
%global _desc Python bindings for the Skia library's Path Ops.

Name:           python-%{pypi_name}
Version:        0.9.2
Release:        1%{?dist}
Summary:        Python bindings for the Skia library's Path Ops
License:        BSD-3-Clause
URL:            https://github.com/jared-hughes/isosurfaces
Source0:        %{pypi_source skia_pathops}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cython
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
sed -i 's/name="%{pypi_name}"/name="%{pypi_name}", version="%{version}"/' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pathops


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Oct 23 2026 Jan200101 <sentrycraft123@gmail.com> - 0.9.2-1
- Initial package
