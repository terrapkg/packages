%global _description %{expand:
An editor that pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.}
%global crate edit
%bcond rust_nightly 1
%if %{with rust_nightly}
%define __cargo /usr/bin/env CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' $HOME/.cargo/bin/cargo
%define __rustc $HOME/.cargo/bin/rustc
%define __rustdoc $HOME/.cargo/bin/rustdoc
%endif

Name:          %{crate}
Version:       1.2.0
Release:       1%?dist
Summary:       A simple editor for simple needs.
SourceLicense: MIT
License:       MIT AND (MIT OR Apache-2.0)
URL:           https://github.com/microsoft/edit
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
%if %{with rust_nightly}
BuildRequires: rustup
%endif
BuildRequires: mold
Packager:      Gilver E. <rockgrub@disroot.org>

%description %_description

%prep
%autosetup -n %{name}-%{version}
%if %{with rust_nightly}
rustup-init -y
. "$HOME/.cargo/env"
rustup toolchain install nightly
rustup override set nightly
%endif
%cargo_prep_online

%build
%cargo_build

%install
%crate_install_bin
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

