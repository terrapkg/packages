%global pypi_name skidl
%global _desc A Python package for textually describing electronic circuit schematics.

Name:			python-%{pypi_name}
Version:		2.3.0
Release:		1%{?dist}
Summary:		A Python package for textually describing electronic circuit schematics
License:		MIT
URL:			https://devbisme.github.io/skidl/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

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

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md HISTORY.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/netlist_to_skidl
%{_bindir}/skidl-part-search

%changelog
* Sun Sep 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
