Name:          krabby
Version:       0.3.0
Release:       2%{?dist}
SourceLicense: GPL-3.0-or-later
License:       (MIT OR Apache-2.0) AND GPL-3.0-or-later AND MIT AND (Unlicense OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND MPL-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
Summary:       Print Pokémon sprites in your terminal
URL:           https://github.com/yannjor/krabby
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: mold
Packager:      Gilver E. <roachy@fyralabs.com>

%description
Krabby is mostly a Rust rewrite of phoney badger's pokemon-colorscripts with some extra features.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build

%install
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
