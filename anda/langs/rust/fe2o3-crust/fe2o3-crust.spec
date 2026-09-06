%global debug_package %{nil}
%global crate fe2o3-crust

Name:           rust-fe2o3-crust
Version:        0.1.46
Release:        1%{?dist}
Summary:        Rust TUI library
URL:            https://github.com/isene/crust
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://unlicense.org/UNLICENSE
License:        Unlicense AND (Apache-2.0 OR MIT) AND MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
BuildRequires:  cargo-rpm-macros
Requires:       %{name}-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Rust TUI library. Feature clone of rcurses
for terminal pane management, input, colors, and Unicode.

%package devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.


%prep
%autosetup -C
%cargo_prep_online

%build

%install
%cargo_install
%{cargo_license_online} > LICENSE.dependencies
cp %{S:1} LICENSE

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%files devel
%{crate_instdir}/

%changelog
* Fri Jul 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
