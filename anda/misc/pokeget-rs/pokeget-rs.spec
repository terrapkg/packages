%global pname pokesprite
%global pcommit c5aaa610ff2acdf7fd8e2dccd181bca8be9fcb3e
%global shortcommit %(c=%{pcommit}; echo ${c:0:7})

Name:          pokeget-rs
Version:       1.6.3
Release:       1%{?dist}
SourceLicense: MIT
License:       MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
Summary:       A better Rust version of pokeget.
URL:           https://github.com/talwat/%{name}
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz
Source1:       https://github.com/msikma/%{pname}/archive/%{pcommit}/%{pname}-%{pcommit}.tar.gz#/%{pname}-%{shortcommit}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: git
BuildRequires: mold
Provides:      pokeget
Provides:      bundled(%{pname})
Packager:      Gilver E. <rockgrub@disroot.org>

%description
Successor to pokeget, written in Rust.

%prep
%setup %{SOURCE0} -T -D -n %{name}-%{version}
%setup %{SOURCE1} -D -c data/%{pname}

%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/pokeget %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies data/%{pname}/license.md
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Mar 01 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
