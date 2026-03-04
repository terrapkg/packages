%global pypi_name haishoku
%global _description1 %{expand:
Haishoku is a development tool for grabbing the dominant color or representative color palette from an image, it depends on Python3 and Pillow.}
%global _description2 %{expand:
Haishoku is a development tool for grabbing the dominant color or representative color palette from an image.}

Name:           python-%{pypi_name}
Version:        1.1.8
Release:        2%{?dist}
Summary:        A development tool for grabbing the dominant color or representative color palette from an image
License:        MIT
URL:            https://github.com/LanceGin/haishoku
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description %_description1

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(pillow)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description2

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

%files -n python3-%{pypi_name}
# This project does have README files but they are not included in the PyPi source
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%endif

%changelog
* Thu May 22 2025 Gilver E. <rockgrub@disroot.org> - 1.1.8-1
- Initial package.
