%global crate cargo-upgrades

Name:                   cargo-upgrades
Version:                3.1.0
Release:                2%{?dist}
Summary:                Binary installation for rust projects
# Cargo.toml, kornelski/cargo-upgrades#16
SourceLicense:          GPL-3.0-or-later
License:                %{sourcelicense} AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (0BSD OR MIT OR Apache-2.0) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND Unicode-3.0 AND GPL-3.0+ AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:                    https://crates.io/crates/cargo-upgrades
Source0:                %{terra_crates_source}
Source1:                https://github.com/sundarnagarajan/licenses/blob/master/GPL-3.txt
BuildSystem:            terra_cargo
BuildRequires:          cargo-rpm-macros
BuildRequires:          pkgconfig(openssl)
# Temporary
BuildRequires:          cargo4rpm
Packager:               Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%install -a
cp %{S:1} LICENSE
%cargo_license_summary_online

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cargo-upgrades

%changelog
* Sun Nov 01 2026 Owen Zimmerman <owen@fyralabs.com> - 3.1.0-1
- Initial commit
