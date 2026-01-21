%global crate typos-cli
%define debug_package %{nil}

Name:           typos
Version:        1.42.1
Release:        1%?dist
Summary:        Source Code Spelling Correction

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typos-cli
Source0:        %{crates_source}
Source1:        https://raw.githubusercontent.com/crate-ci/%{name}/refs/tags/v%{version}/LICENSE-MIT
Source2:        https://raw.githubusercontent.com/crate-ci/%{name}/refs/tags/v%{version}/LICENSE-APACHE

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold

%description
Finds and corrects spelling mistakes among source code.

%prep
%autosetup -n %{crate}-%{version}
cp %{S:1} .
cp %{S:2} .
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE-MIT LICENSE-APACHE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Dec 28 2025 metcya <metcya@gmail.com> - 1.40.0-1
- Initial package
