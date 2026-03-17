%global pypi_name whey
%global _desc A simple Python wheel builder for simple projects.

Name:			python-%{pypi_name}
Version:		0.1.1
Release:		1%?dist
Summary:		A simple Python wheel builder for simple projects
License:		MIT
URL:			https://github.com/deepin-community/python-whey
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-devel

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n whey-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files whey

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/whey

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
