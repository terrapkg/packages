%global pypi_name hierplace
%global _desc KiCad PCBNEW plugin that arranges parts into groups that reflect the design hierarchy.

Name:			python-%{pypi_name}
Version:		1.1.0
Release:		1%{?dist}
Summary:		KiCad PCBNEW plugin that arranges parts into groups that reflect the design hierarchy
License:		MIT
URL:			https://github.com/devbisme/HierPlace
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
%doc README.rst
%license LICENSE

%changelog
* Sun Sep 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
