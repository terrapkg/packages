%global pypi_name wireviz

Name:           wireviz
Version:        0.4.1
Release:        1%{?dist}
Summary:        Generate wiring harness documentation from YAML descriptions
URL:            https://github.com/wireviz/WireViz
Source0:        https://github.com/wireviz/WireViz/archive/refs/tags/v%{version}.tar.gz
License:        GPL-3.0-only
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cairosvg)
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{evr}
Requires:       graphviz

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
WireViz generates wiring harness documentation from YAML descriptions. It
produces connection tables and graphical schematics in common output formats.

%package -n     python3-%{pypi_name}
Summary:        Python library for WireViz
Requires:       python3dist(cairosvg)
Requires:       python3dist(graphviz)
Requires:       python3dist(pillow)
Requires:       python3dist(pyyaml)

%description -n python3-%{pypi_name}
Python library for generating wiring harness documentation with WireViz.

%prep
%autosetup -n WireViz-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files
%license LICENSE
# readme is in docs/
%doc docs/*
%{_bindir}/wireviz

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc docs/*

%changelog
* Sat Sep 19 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
