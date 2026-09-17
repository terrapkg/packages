%global pypi_name pybcj
%global _desc BCJ(Branch-Call-Jump) filter for python.

Name:			python-%{pypi_name}
Version:		1.0.8
Release:		1%{?dist}
Summary:		BCJ(Branch-Call-Jump) filter for python
License:		LGPL-2.1-or-later
URL:			https://github.com/miurahr/pybcj
Source0:		%{pypi_source}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
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
%pyproject_save_files bcj

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Wed Sep 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
