%global pypi_name solidpython

%global _desc SolidPython is a generalization of Phillip Tiefenbacher's openscad module. It generates valid OpenSCAD code from Python code.

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        1%{?dist}
Summary:        Python interface to the OpenSCAD declarative geometry language
License:        LGPL-2.1-or-later
URL:            https://github.com/SolidCode/SolidPython
Source0:        %{pypi_source}
Source1:        https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
Patch0:         importlib-metadata.patch
Patch1:         invalid-escapes.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(euclid3)
BuildRequires:  python3dist(ply)
BuildRequires:  python3dist(prettytable)
BuildRequires:  python3dist(pypng)
BuildRequires:  python3dist(pytest)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm pyproject.toml
cp %{SOURCE1} LICENSE
%py3_shebang_fix solid
find solid -depth \( -name .mypy_cache -o -name .vscode -o -name '*.egg-info' \) -exec rm -rf {} +
sed -i \
  -e "s/'PrettyTable==0.7.2'/'PrettyTable'/" \
  -e "s/'pypng>=0.0.19,<0.0.20'/'pypng>=0.0.19'/" \
  setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files solid

%check
%pytest solid/test -k 'not test_generator_scad and not test_generator_no_scad'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com> - 1.1.3-1
- Initial package
