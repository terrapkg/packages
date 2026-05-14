%undefine __brp_mangle_shebangs

Name:           kittyCAD-cli
Version:        0.2.169
Release:        1%{?dist}
Summary:        The Zoo command line tool for KittyCAD
URL:            https://github.com/KittyCAD/cli
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        MIT AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND NCSA) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND 0BSD AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception AND MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause) AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND EPL-2.0 AND ISC AND LGPL-3.0-or-later AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (MPL-2.0 OR MIT OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
BuildRequires:  cargo-rpm-macros

Provides:       kittycad-cli
Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n cli-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/release/zoo %{buildroot}%{_bindir}/zoo
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/zoo
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Thu Apr 30 2026 Its-J <jonah@fyralabs.com>
- Package KittyCAD CLI
