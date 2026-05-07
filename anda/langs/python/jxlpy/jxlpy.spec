%global pypi_name jxlpy
%global _desc Cython bindings and Pillow plugin for JPEG XL.

Name:			python-%{pypi_name}
Version:		0.9.5
Release:		1%?dist
Summary:		Cython bindings and Pillow plugin for JPEG XL
License:		MIT
URL:			https://github.com/olokelo/jxlpy
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-cython
BuildRequires:  libjxl-devel
BuildRequires:  gcc-c++

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitearch}/_jxlpy.cpython-314-%{_arch}-linux-gnu.so

%changelog
* Sat Mar 28 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
