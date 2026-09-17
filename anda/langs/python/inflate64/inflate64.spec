%global pypi_name inflate64
%global _desc deflate64 compression/decompression library.

Name:			python-%{pypi_name}
Version:		1.0.4
Release:		1%{?dist}
Summary:		deflate64 compression/decompression library
License:		LGPL-2.1-or-later
URL:			https://inflate64.readthedocs.io/
Source0:		%{pypi_source}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

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
%doc README.rst
%license COPYING

%changelog
* Wed Sep 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
