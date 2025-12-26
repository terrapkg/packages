%global pypi_name yamale
%global _desc A schema and validator for YAML.

Name:			python-%{pypi_name}
Version:		6.1.0
Release:		2%?dist
Summary:		A schema and validator for YAML
License:		MIT
URL:			https://github.com/23andMe/Yamale
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       yamale
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n yamale-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yamale

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md SECURITY.md
%license LICENSE
%{_bindir}/yamale
%python3_sitelib/yamale-%version.dist-info/*

%changelog
* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
