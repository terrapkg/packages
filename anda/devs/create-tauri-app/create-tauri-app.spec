%global crate create-tauri-app

Name:           rust-create-tauri-app
Version:        4.7.0
Release:        2%?dist
Summary:        Rapidly scaffold out a new tauri app project
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/create-tauri-app
Source:         %{crates_source}
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold
Suggests:       tauri
Packager:       Gilver E. <roachy@fyralabs.com>

%description
%{summary}.

%package -n     %{crate}
Summary:        %{summary}
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib

%description -n %{crate}
%{summary}.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/cargo-%{crate} %{buildroot}%{_bindir}/%{crate}
%{cargo_license_online} > LICENSE.dependencies

%files -n %{crate}
%license LICENSE.spdx
%license LICENSE_APACHE-2.0
%license LICENSE_MIT
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/%{crate}

%changelog
* Fri Dec 26 2025 Gilver E. <roachy@fyralabs.com> - 4.6.2-1
- Initial package
