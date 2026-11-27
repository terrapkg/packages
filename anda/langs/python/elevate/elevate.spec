%global pypi_name elevate
%global _desc Python library for requesting root privileges.

Name:			python-%{pypi_name}
Version:		0.1.3
Release:		2%{?dist}
Summary:		Python library for requesting root privileges
License:		MIT
URL:			https://github.com/barneygale/elevate
Source0:		%{pypi_source}
Source1:        https://raw.githubusercontent.com/barneygale/elevate/master/COPYING.txt
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

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
cp %{S:1} LICENSE

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sun Nov 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.3-1
- Initial commit
