%global pypi_name useful-types
%global _desc A collection of useful types.

Name:			python-%{pypi_name}
Version:		0.2.1
Release:		1%{?dist}
Summary:		A collection of useful types
License:		MIT
URL:			https://github.com/hauntsaninja/useful_types
Source0:		%{pypi_source useful_types}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
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
%pyproject_save_files useful_types

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Wed Sep 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
