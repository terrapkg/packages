%global pypi_name PyMeta3

%global _desc PyMeta is an implementation of OMeta, an object-oriented pattern-matching language, for Python 3 and 2.

Name:           python-pymeta3
Version:        0.5.1
Release:        1%{?dist}
Summary:        Pattern-matching language based on OMeta for Python 3 and 2
License:        MIT
URL:            https://github.com/wbond/pymeta3
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{_desc}

%package -n     python3-pymeta3
Summary:        %{summary}
%{?python_provide:%python_provide python3-pymeta3}

%description -n python3-pymeta3
%{_desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymeta

%check
%pyproject_check_import

%files -n python3-pymeta3 -f %{pyproject_files}
%doc README NEWS
%license LICENSE

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com> - 0.5.1-1
- Initial package
