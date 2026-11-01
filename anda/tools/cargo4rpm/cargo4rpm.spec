Name:          cargo4rpm
Version:       0.1.0
Release:       1%{?dist}
Summary:       A cargo2rpm-like tool that works with Cargo instead of against it
SourceLicense: EUPL-1.2
License:       (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND EUPL-1.2 AND ISC AND MIT AND (MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND MPL-2.0-or-later AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:           https://codeberg.org/GildedRoach/cargo4rpm
Source0:       https://codeberg.org/GildedRoach/cargo4rpm/archive/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo
BuildRequires: cargo-rpm-macros
%if %["%{toolchain}" == "clang"]
BuildRequires:  clang
%else
BuildRequires:  gcc
%endif
BuildRequires:  pkgconfig(openssl)
Packager:       Gilver E. <roachy@fyralabs.com>

%description
%{name} is a cargo2rpm-like tool that works with Cargo instead of against it.

%prep
%autosetup -n %{name}
%cargo_prep_online

%build
%cargo_build

%install
%terra_cargo_install

%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Sun Nov 1 2026 Gilver E. <roachy@fyralabs.com> - 0.1.0-1
- Initial package
