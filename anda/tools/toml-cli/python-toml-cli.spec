Name:           python-toml-cli
Version:        0.8.2
Release:        1%{?dist}
Summary:        Read and write keys/values to/from toml files

License:        MIT
URL:            https://github.com/mrijken/toml-cli
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/toml-cli-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-hatchling
BuildRequires:  python3-jmespath
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-typer
BuildRequires:  python3-tomlkit

%global _description %{expand:
Command line interface for toml files.}

%description %_description

%package -n     python3-toml-cli
Summary:        %{summary}

%description -n python3-toml-cli %_description

%package -n     toml-cli
Summary:        %{summary}
Requires:       python3-toml-cli
# Provides a binary at the same path
Conflicts:      libtoml

%description -n toml-cli %_description

%prep
%autosetup -p1 -n toml-cli-%{version}

# Don't try to write test files to /tmp
sed -i 's|test_toml_path = .*|test_toml_path = pathlib.Path("%{rpmbuilddir}") / "test.toml"|g' tests/toml_cli/test_init.py

# Drop version constraints
sed -i 's|regex>=.*[0-9]|regex|g;s|tomlkit>=.*[0-9]|tomlkit|g;s|typer>=.*[0-9]|typer|g' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L toml_cli

%check
# Skip two tests that fail upstream and one that fails only on EL
%pytest -v -k 'not (test_search or test_set_in_out_of_order_table or test_get_value)'

%files -n python3-toml-cli -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files -n toml-cli
%{_bindir}/toml

%changelog
* Mon Nov 9 2026 Gilver E. <roachy@fyralabs.com>
- Initial port to Terra
