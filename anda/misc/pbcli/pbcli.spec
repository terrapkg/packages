%global _description %{expand:
pbcli is a command line client which allows to upload and download pastes from privatebin directly from the command line.}

Name:           pbcli
Version:        2.8.0
Release:        3%?dist
Summary:        A PrivateBin commandline upload and download utility
SourceLicense:  Unlicense OR MIT
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND ISC AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
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

%package        devel
Summary:        Development libraries for %{name}
Requires:       %{name}

%description    devel
This package contains the development files for %{name}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build -f uniffi
%{cargo_license_online -f uniffi} > LICENSE.dependencies

%install
install -Dm755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 target/rpm/lib%{name}.so %{buildroot}%{_libdir}/lib%{name}.so
install -Dm644 target/rpm/lib%{name}.a %{buildroot}%{_libdir}/lib%{name}.a

%files
%doc README.md
%license LICENSE-MIT
%license LICENSE-UNLICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}

%files devel
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so

%changelog
* Sat Mar 14 2025 Gilver E. <rockgrub@disroot.org>
- Enable uniffi support
- Package development files
* Sat Dec 21 2024 Gilver E. <rockgrub@disroot.org>
- Initial package
