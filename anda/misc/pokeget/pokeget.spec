%global pname pokesprite
%global pcommit c5aaa610ff2acdf7fd8e2dccd181bca8be9fcb3e
%global crate pokeget
%bcond check 1

Name:          %{crate}
Version:       1.6.4
Release:       3%?dist
SourceLicense: MIT
License:       (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
Summary:       A better Rust version of pokeget.
URL:           https://crates.io/crates/%{crate}
Source0:       %{crates_source}
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: mold
Provides:      bundled(%{pname}) = %{pcommit}
Obsoletes:     %{crate}-rs < %{version}-%{release}
Packager:      Gilver E. <rockgrub@disroot.org>, madonuko <mado@fyralabs.com>

%description
Successor to pokeget, written in Rust.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/%{crate} -t %{buildroot}%{_bindir}
%{cargo_license_online} > LICENSE.dependencies

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license data/%{pname}/license.md
%doc README.md
%doc OTHER_PROJECTS.md
%{_bindir}/%{crate}

%changelog
* Mon Mar 10 2025 Gilver E. <rockgrub@disroot.org>
- Rename package to drop the rs suffix as the original pokeget is fully obsoleted
- Update licenses
* Sat Mar 01 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
