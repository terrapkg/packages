%global _description %{expand:
pbcli is a command line client which allows to upload and download pastes from privatebin directly from the command line.}

Name:           pbcli
Version:        2.8.0
Release:        2%?dist
Summary:        A PrivateBin commandline upload and download utility
SourceLicense:  Unlicense OR MIT
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/Mydayyy/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold
BuildRequires:  openssl-libs
BuildRequires:  perl-ExtUtils-MM-Utils
BuildRequires:  perl-FindBin
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  perl-IPC-Cmd
BuildRequires:  perl-lib
Packager:       Gilver E. <rockgrub@disroot.org>

%description %_description

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 target/rpm/lib%{name}.so %{buildroot}%{_libdir}/lib%{name}.so

%files
%doc README.md
%license LICENSE-MIT
%license LICENSE-UNLICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
* Sat Dec 21 2024 Gilver E. <rockgrub@disroot.org>
- Initial package
