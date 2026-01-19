%global pypi_name treetable
%global _desc Print in ascii art a table with a tree-like structure.

Name:			python-%{pypi_name}
Version:		0.2.6
Release:		1%?dist
Summary:		Print in ascii art a table with a tree-like structure
License:		Unlicense
URL:			https://github.com/adefossez/treetable
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
%pyproject_save_files treetable

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jan 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
