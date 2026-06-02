%global pypi_name proxy_tools
%global _desc Simple (hopefuly useful) Proxy (as in the GoF design pattern) implementation for Python.

Name:			python-%{pypi_name}
Version:		0.1.0
Release:		1%?dist
Summary:		Simple (hopefuly useful) Proxy (as in the GoF design pattern) implementation for Python
License:		BSD-2-clause
URL:			https://github.com/jtushman/proxy_tools
Source0:		%{pypi_source}
Source1:		https://github.com/jtushman/proxy_tools/blob/master/LICENSE.txt
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}
cp %{S:1} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Wed Feb 25 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
