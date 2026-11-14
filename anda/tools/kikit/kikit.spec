%global pypi_name kikit

%global _desc KiKit is a Python library, KiCAD plugin and a CLI tool to automate several tasks in a standard KiCAD workflow.

Name:           python-%{pypi_name}
Version:        1.8.1
Release:        1%{?dist}
Summary:        Automation for KiCAD boards
License:        MIT
URL:            https://github.com/yaqwsx/KiKit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(versioneer)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} = %{evr}
# kikit drives pcbnew, which only ships with KiCad
Requires:       kicad

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n KiKit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENCE
%{_bindir}/kikit
%{_bindir}/kikit-info

%changelog
* Fri Nov 13 2026 Cypress Reed <cypress@fyralabs.com> - 1.8.1-1
- Initial package
