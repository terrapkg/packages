%global debug_package %{nil}

Name:			python3-orjson
Version:		3.8.6
Release:		1%{?dist}
Summary:		Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:		MIT or APACHE-2.0
URL:			https://github.com/ijl/orjson
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:	python3-installer python3.11 python3-pip maturin cargo
%{?python_provide:%python_provide python3-orjson}
Provides:		python3.11dist(orjson) = %{version}

%description
orjson is a fast, correct JSON library for Python. It benchmarks as the fastest Python library
for JSON and is more correct than the standard json library or other third-party libraries. It
serializes dataclass, datetime, numpy, and UUID instances natively.

%prep
%autosetup -n orjson-%{version}

%build
maturin build --release --strip

%install
sed 's@^\s+"repository":.+?^@@' setup.py > setup.py
python3.11 -m installer --destdir="%{buildroot}" target/wheels/*.whl
rm -rf %{python3_sitelib}/orjson/__pycache__

%files
%doc README.md
%license /usr/lib64/python*/site-packages/orjson-%{version}.dist-info/license_files/LICENSE-MIT
%license /usr/lib64/python*/site-packages/orjson-%{version}.dist-info/license_files/LICENSE-APACHE
/usr/lib64/python*/site-packages/orjson-%{version}.dist-info/METADATA
/usr/lib64/python*/site-packages/orjson-%{version}.dist-info/RECORD
/usr/lib64/python*/site-packages/orjson-%{version}.dist-info/WHEEL
/usr/lib64/python*/site-packages/orjson/__init__.py
/usr/lib64/python*/site-packages/orjson/__init__.pyi
/usr/lib64/python*/site-packages/orjson/__pycache__/__init__.cpython-*.pyc
/usr/lib64/python*/site-packages/orjson/orjson.cpython-*-linux-gnu.so
/usr/lib64/python*/site-packages/orjson/py.typed

%changelog
* Sun Jan 08 2023 windowsboy111 <wboy111@outlook.com> - 3.8.4-1
- Initial package.
