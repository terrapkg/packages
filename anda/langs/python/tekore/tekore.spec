%global pypi_name tekore
%global _desc Spotify Web API client for Python 3.

Name:			python-%{pypi_name}
Version:		6.1.1
Release:		1%?dist
Summary:		Spotify Web API client for Python 3
License:		MIT
URL:			https://tekore.readthedocs.io/en/stable/
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
%doc readme_pypi.rst
%license LICENSE

%changelog
* Thu Oct 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
