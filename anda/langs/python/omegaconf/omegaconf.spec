%global pypi_name omegaconf
%global _desc Flexible Python configuration system. The last one you will ever need.

Name:			python-%{pypi_name}
Version:		2.3.0
Release:		1%?dist
Summary:		Flexible Python configuration system. The last one you will ever need
License:		BSD-3-Clause
URL:			https://github.com/omry/omegaconf
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  java-21-openjdk-devel

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n omegaconf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files omegaconf

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitelib}/pydevd_plugins/

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
