%global pypi_name upiano
%global _desc Terminal Piano App.

Name:			python-%{pypi_name}
Version:		0.1.2
Release:		1%?dist
Summary:		Terminal Piano App
License:		MIT
URL:			https://github.com/eliasdorneles/upiano
Source0:		%{pypi_source}
Source1:        %url/blob/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n upiano-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files upiano

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/upiano

%changelog
* Sat Jan 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
