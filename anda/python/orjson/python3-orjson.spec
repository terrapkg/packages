Name:			python3-orjson
Version:		3.8.5
Release:		%autorelease
Summary:		Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:		MIT or APACHE-2.0
URL:			https://github.com/ijl/orjson
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:		noarch
BuildRequires:	maturin cargo python3.11 python3-pip
Requires:		libc

%description
orjson is a fast, correct JSON library for Python. It benchmarks as the fastest Python library
for JSON and is more correct than the standard json library or other third-party libraries. It
serializes dataclass, datetime, numpy, and UUID instances natively.

%prep
%autosetup -n orjson-%{version}

%build
maturin build --release --strip

%install
pip install .

%files
%doc README.md
%license LICENSE-APACHE
%license LICENSE-MIT

%changelog
* Sun Jan 08 2023 windowsboy111 <wboy111@outlook.com> - 3.8.4-1
- Initial package.
