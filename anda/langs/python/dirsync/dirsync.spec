%global pypi_name dirsync
%global _desc Advanced directory tree synchronisation tool.

Name:			python-%{pypi_name}
Version:		2.2.6
Release:		1%{?dist}
Summary:		Advanced directory tree synchronisation tool
License:		MIT
URL:			https://github.com/domdfcoding/deprecation-alias
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildArch:      noarch

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
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/%{pypi_name}

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
