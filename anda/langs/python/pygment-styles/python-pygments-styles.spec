%global pypi_name pygments_styles
%global real_name pygments-styles

Name:           python-%{real_name}
Version:        0.3.0
Release:        2%{?dist}
Summary:        A collection of Pygments styles
License:        BSD-3-Clause
URL:            https://pygments-styles.org
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
A curated collection of Pygments styles based on VS Code themes.

%package -n     python3-%{real_name}
Summary:        %{summary}
Requires:       python3dist(pygments)
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
A curated collection of Pygments styles based on VS Code themes.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{real_name} -f %{pyproject_files}
%doc     PKG-INFO
%doc     README.md
%license LICENSE

%changelog
* Wed Dec 10 2025 Gilver E. <rockgrub@disroot.org> - 0.3.0-1
- Initial package.
