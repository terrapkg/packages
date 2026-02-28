%global pypi_name materialyoucolor
%bcond test 0

Name:           python-%{pypi_name}
Version:        2.0.10
Release:        2%{?dist}
Summary:        Material You color generation algorithms in pure python!
License:        MIT
URL:            https://github.com/T-Dynamos/materialyoucolor-python
Source0:        %{pypi_source}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(setuptools)
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Material You color generation algorithms in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Material You color generation algorithms in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%endif

# Test image isn't included and I'm not supplying one
%if %{with test}
%check
%pytest test_image.jpg 1
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}/
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%endif


%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org> - 2.0.10-1
- Initial package.
