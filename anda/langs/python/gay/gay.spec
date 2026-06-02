%global pypi_name gay
%global _desc Colour your text / terminal to be more gay.

Name:			python-%{pypi_name}
Version:		1.3.4
Release:		2%?dist
Summary:		Colour your text / terminal to be more gay
License:		MIT
URL:			https://github.com/ms-jpq/gay
Source0:		%{pypi_source}
BuildArch:      noarch

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

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/gay
%python3_sitelib/gay-%{version}.dist-info/*

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
