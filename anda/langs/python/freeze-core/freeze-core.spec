%global pypi_name freeze-core
%global _desc Core dependency for cx_Freeze.
%define debug_package %{nil}

Name:			python-%{pypi_name}
Version:		0.8.1
Release:		1%{?dist}
Summary:		Core dependency for cx_Freeze
License:		MIT
URL:			https://marcelotduarte.github.io/cx_Freeze/
Source0:		%{pypi_source freeze_core}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gcc

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C
%pyproject_patch_dependency filelock:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files freeze_core

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Oct 29 2026 Owen Zimmerman <owen@fyralabs.com> - 0.8.1-1
- Initial commit
