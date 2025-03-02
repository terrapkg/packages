Name:          pokeget-rs
Version:       1.6.3
Release:       1%{?dist}
SourceLicense: MIT
License:       MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
Summary:       A better Rust version of pokeget.
URL:           https://github.com/talwat/%{name}
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: git
BuildRequires: mold
Provides:      pokeget
Packager:      Gilver E. <rockgrub@disroot.org>

%description
Successor to pokeget, written in Rust.

%prep
%autosetup -n %{name}-%{version}
git clone -b c5aaa610ff2acdf7fd8e2dccd181bca8be9fcb3e https://github.com/msikma/pokesprite.git data/pokesprite
rm -rf data/pokesprite/.git
%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/pokeget %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies data/pokesprite/license.md
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Mar 01 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
