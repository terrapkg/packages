%global pypi_name euclid3

%global _desc euclid3 is a 2D and 3D vector, matrix, quaternion and geometry module, updated for Python 3.

Name:           python-%{pypi_name}
Version:        0.01
Release:        1%{?dist}
Summary:        2D and 3D vector, matrix, quaternion and geometry module
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/euclid3
Source0:        %{pypi_source}
Source1:        https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf build %{pypi_name}.egg-info
cp %{SOURCE1} LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README
%license LICENSE

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com> - 0.01-1
- Initial package
