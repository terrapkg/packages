%global crate cargo-binstall

%undefine __brp_mangle_shebangs

Name:           cargo-binstall
Version:        1.26.2
Release:        1%{?dist}
Summary:        Binary installation for rust projects
SourceLicense:  GPL-3.0-only
License:        Apache-2.0 WITH LLVM-exception AND (ISC AND (Apache-2.0 OR ISC)) AND bzip2-1.0.6 AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND BSD-3-Clause AND MIT AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Apache-2.0) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://crates.io/crates/cargo-binstall
Source:         %{terra_crates_source}
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cargo-binstall

%changelog
* Tue Oct 20 2026 Owen Zimmerman <owen@fyralabs.com> - 1.26.0-1
- Initial commit
