%global pypi_name ratelimit
%global _desc API Rate Limit Decorator.

Name:			python-%{pypi_name}
Version:		2.2.1
Release:		1%?dist
Summary:		API Rate Limit Decorator
License:		MIT
URL:			https://github.com/tomasbasham/ratelimit
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
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
