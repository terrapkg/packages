%global pypi_name pyee
%global _desc A rough port of Node.js's EventEmitter to Python with a few tricks of its own.

Name:			python-%{pypi_name}
Version:		13.0.1
Release:		1%?dist
Summary:		A rough port of Node.js's EventEmitter to Python with a few tricks of its own
License:		MIT
URL:			https://github.com/jfhbrook/pyee
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
Provides:       pyee
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyee

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md DEVELOPMENT.md CONTRIBUTORS.md CHANGELOG.md
%license LICENSE
%python3_sitelib/%{pypi_name}/__pycache__/*.cpython-*.pyc
%python3_sitelib/%{pypi_name}/*.py

%changelog
* Sun Nov 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
