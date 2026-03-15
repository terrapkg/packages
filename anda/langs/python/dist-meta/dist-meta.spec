%global pypi_name dist-meta
%global _desc Parse and create Python distribution metadata.

Name:			python-%{pypi_name}
Version:		0.9.0
Release:		1%?dist
Summary:		Parse and create Python distribution metadata
License:		MIT
URL:			https://dist-meta.readthedocs.io/en/latest/
Source0:		https://github.com/repo-helper/dist-meta/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-hatch-requirements-txt

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
%pyproject_save_files dist_meta

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
