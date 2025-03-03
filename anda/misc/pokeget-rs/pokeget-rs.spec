%global pname pokesprite
%global pcommit c5aaa610ff2acdf7fd8e2dccd181bca8be9fcb3e
%global pshortcommit %(c=%{pcommit}; echo ${c:0:7})
%global pcommit_date 20220622
%global shortname pokeget

Name:          %{shortname}-rs
Version:       1.6.3
Release:       2%{?dist}
SourceLicense: MIT
License:       MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
Summary:       A better Rust version of pokeget.
URL:           https://github.com/talwat/%{name}
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz
Source1:       https://github.com/msikma/%{pname}/archive/%{pcommit}/%{pname}-%{pcommit}.tar.gz#/%{pname}-%{pshortcommit}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: mold
Provides:      pokeget = %{version}-%{release}
Provides:      bundled(%{pname}) = 2.7.0^%{pcommit_date}.%{pshortcommit}
Packager:      Gilver E. <rockgrub@disroot.org>

%description
Successor to pokeget, written in Rust.

%prep
%autosetup -n %{name}-%{version}
mkdir -p data/%{pname}
pushd data/%{pname}
/usr/bin/gzip -dc '%{SOURCE1}' | /usr/bin/tar -xof - --strip-components=1
popd
%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/%{shortname} -t %{buildroot}%{_bindir}
ln -sf %{shortname} %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies data/%{pname}/license.md
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{shortname}

%changelog
* Sat Mar 01 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
