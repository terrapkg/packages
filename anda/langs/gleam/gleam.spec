Name:           gleam
Version:        1.18.1
Release:        1%?dist
Summary:        A friendly language for building type-safe, scalable systems!
URL:            https://gleam.run/
Source0:        https://github.com/gleam-lang/gleam/archive/refs/tags/v%{version}.tar.gz
# licences/
SourceLicense:  Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0-or-later AND Unicode-3.0 AND Zlib
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (LGPL-3.0-or-later OR MPL-2.0) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND MPL-2.0+ AND CC0-1.0 AND Apache-2.0 AND ISC AND BSL-1.0 AND ISC AND BSD-3-Clause AND (Unlicense OR MIT)
BuildRequires:  cargo-rpm-macros
Requires:       erlang

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build

%install
%crate_install_bin

%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md CHANGELOG.md docs/*
%license LICENCE LICENSE.dependencies licences/*
%{_bindir}/gleam

%changelog
* Sat Feb 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
