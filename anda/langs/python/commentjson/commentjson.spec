%global pypi_name commentjson

%global _desc commentjson is a Python package that helps you create JSON files with Python and JavaScript style inline comments.

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Add Python and JavaScript style comments in your JSON files
License:        MIT
URL:            https://github.com/vaidik/commentjson
# using the github source because the pypi source is missing the test file
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(lark)
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
sed -i "s/'lark-parser>=0.7.1,<0.8.0'/'lark>=0.7.1'/" setup.py
sed -i \
  -e '/^from six import iteritems$/d' \
  -e 's/iteritems(self\.test_json)/self.test_json.items()/' \
  commentjson/tests/test_commentjson.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest commentjson/tests --ignore=commentjson/tests/test_json

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
* Mon Nov 16 2026 Cypress Reed <cypress@fyralabs.com> - 0.9.0-1
- Initial package
