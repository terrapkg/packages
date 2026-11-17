%global pypi_name pybars3

%global _desc pybars3 is a Python implementation of the Handlebars.js templating language.

Name:           python-%{pypi_name}
Version:        0.9.7
Release:        1%{?dist}
Summary:        Handlebars.js templating for Python 3 and 2
License:        LGPL-3.0-only
URL:            https://github.com/wbond/pybars3
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pymeta3)
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
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pybars

%check
%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc readme.md changelog.md
%license LICENSE

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com> - 0.9.7-1
- Initial package
