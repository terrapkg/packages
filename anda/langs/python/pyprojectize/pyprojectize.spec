%global pypi_name pyprojectize
%global _desc Convert a spec file from py3_build etc. macros to pyproject_*.

Name:			python-%{pypi_name}
Version:		1a7
Release:		1%?dist
Summary:		Convert a spec file from py3_build etc. macros to pyproject_*
License:		MIT-0
URL:			https://github.com/hroncok/pyprojectize
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-hatchling
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyprojectize

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pyprojectize

%changelog
* Mon Mar 09 2026 Owen Zimmerman <owen@fyralabs.com> - 1a7-1
- Initial commit
