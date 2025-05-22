%global _description %{expand:
An editor that pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.}
%bcond nightly 1

Name:          edit
Version:       1.0.0
Release:       1%{?dist}
Summary:       A simple editor for simple needs.
SourceLicense: MIT
License:       MIT
URL:           https://github.com/microsoft/edit
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: mold
Packager:      Gilver E. <rockgrub@disroot.org>

%description %_description

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build

%install
%if %{with nightly}
export RUSTC_BOOTSTRAP=1
%endif

%cargo_install

%{cargo_license_online} > LICENSE.dependencies

%files
%doc CODE_OF_CONDUCT.md
%doc README.md
%doc SECURITY.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Thu May 22 2025 Gilver E. <rockgrub@disroot.org> - 1.0.0-1
- Initial package

