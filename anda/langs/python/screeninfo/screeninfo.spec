%global pypi_name screeninfo
%global _desc Fetch location and size of physical screens.

Name:			python-%{pypi_name}
Version:		0.8.1
Release:		1%?dist
Summary:		Fetch location and size of physical screens
License:		MIT
URL:			https://github.com/rr-/screeninfo
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       screeninfo
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n screeninfo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files screeninfo

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
* Sun Nov 09 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
