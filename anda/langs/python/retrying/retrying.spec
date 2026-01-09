%global pypi_name retrying
%global _desc General-purpose retrying library.

%define debug_package %{nil}

Name:			python-%{pypi_name}
Version:		1.4.2
Release:		1%?dist
Summary:		General-purpose retrying library
License:		Apache-2.0
URL:			https://github.com/groodt/retrying
Source0:		%{pypi_source}

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

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files retrying

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
