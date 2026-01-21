%global pypi_name hydra-colorlog
%global _desc Hydra is a framework for elegantly configuring complex applications.

%define debug_package %{nil}

Name:			python-%{pypi_name}
Version:		1.2.0
Release:		1%?dist
Summary:		Hydra is a framework for elegantly configuring complex applications
License:		MIT
URL:			https://github.com/facebookresearch/hydra
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
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
%autosetup -n hydra-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hydra

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jan 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
