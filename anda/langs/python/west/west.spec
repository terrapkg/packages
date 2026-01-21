%global pypi_name west
%global _desc West, Zephyr's meta-tool.

Name:			python-%{pypi_name}
Version:		1.5.0
Release:		2%?dist
Summary:		West, Zephyr's meta-tool
License:		Apache-2.0
URL:			https://github.com/zephyrproject-rtos/west
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-installer

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       west
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n west-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files west

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst MAINTAINERS.rst
%license LICENSE
%{_bindir}/west

%changelog
* Fri Oct 10 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
