%global pypi_name haishoku
%global _description1 %{expand:
Haishoku is a development tool for grabbing the dominant color or representative color palette from an image, it depends on Python3 and Pillow.}
%global _description2 %{expand:
Haishoku is a development tool for grabbing the dominant color or representative color palette from an image.}

Name:           python-%{pypi_name}
Version:        1.1.8
Release:        1%{?dist}
Summary:        A development tool for grabbing the dominant color or representative color palette from an image
License:        MIT
URL:            https://github.com/LanceGin/haishoku
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

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
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
# This project does have README files but they are not included in the PyPi source
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Thu May 22 2025 Gilver E. <rockgrub@disroot.org> - 1.1.8-1
- Initial package.
