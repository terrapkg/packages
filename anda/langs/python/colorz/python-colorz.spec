%global pypi_name colorz

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Color scheme generator
License:        MIT
URL:            https://github.com/metakirby5/colorz
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
A k-means color scheme generator.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(pillow)
Requires:       python3dist(scipy)
Requires:       python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}


%description -n python3-%{pypi_name}
A k-means color scheme generator.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc PKG-INFO
%doc README.rst
%{_bindir}/colorz
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Thu May 22 2025 Gilver <rockgrub@disroot.org> - 1.0.3-1
- Initial package.
