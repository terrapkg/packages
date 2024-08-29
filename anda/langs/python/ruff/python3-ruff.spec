%define debug_package %{nil}

Name:			python3-ruff
Version:		0.6.3
Release:		1%?dist
Summary:		An extremely fast Python linter, written in Rust
License:		MIT
URL:			https://beta.ruff.rs/
Source0:		https://github.com/astral-sh/ruff/archive/refs/tags/%{version}.tar.gz
BuildRequires:	python3-installer python3-pip maturin cargo
Provides:		python3.11dist(ruff) = %{version}

%description
Ruff aims to be orders of magnitude faster than alternative tools while
integrating more functionality behind a single, common interface.

%prep
%autosetup -n ruff-%{version}

%build
maturin build --release --strip --all-features # --locked

%install
pip3 install --root=%{buildroot} target/wheels/*.whl
rm -rf %{python3_sitelib}/ruff/__pycache__

%files
%doc README.md
%license LICENSE
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/METADATA
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/RECORD
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/WHEEL
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/INSTALLER
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/REQUESTED
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/direct_url.json
/usr/lib64/python*/site-packages/ruff-%{version}.dist-info/license_files/LICENSE
/usr/lib64/python*/site-packages/ruff/__init__.py
/usr/lib64/python*/site-packages/ruff/__main__.py
/usr/lib64/python*/site-packages/ruff/__pycache__/*.cpython-*.opt-1.pyc
/usr/lib64/python*/site-packages/ruff/__pycache__/*.cpython-*.pyc
/usr/bin/ruff

%changelog
* Mon Jan 23 2023 windowsboy111 <wboy111@outlook.com> - 0.0.229
- Initial package.

