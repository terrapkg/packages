%global crate typos-cli
%define _unpackaged_files_terminate_build 0

Name:           typos
Version:        1.40.0
Release:        1%{?dist}
Summary:        Source Code Spelling Correction

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typos-cli
Source0:        %{crates_source}
Source1:        https://raw.githubusercontent.com/crate-ci/%{name}/refs/tags/v%{version}/LICENSE-MIT
Source2:        https://raw.githubusercontent.com/crate-ci/%{name}/refs/tags/v%{version}/LICENSE-APACHE

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold

%global _description %{expand:
Source Code Spelling Correction.}

%description %{_description}

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
cp %{S:1} .
cp %{S:2} .

%files
%license LICENSE-MIT LICENSE-APACHE LICENSE.dependencies
%doc README.md
%{_bindir}/typos

%changelog
* Sun Dec 28 2025 metcya <metcya@gmail.com> - 1.40.0-1
- Initial package
