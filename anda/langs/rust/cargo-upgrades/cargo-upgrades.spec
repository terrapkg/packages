%global crate cargo-upgrades

Name:                   cargo-upgrades
Version:                3.1.0
Release:                1%{?dist}
Summary:                Binary installation for rust projects
# Cargo.toml, kornelski/cargo-upgrades#16
SourceLicense:          GPL-3.0-or-later
License:                %{sourcelicense}
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

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cargo-upgrades

%changelog
* Sun Nov 01 2026 Owen Zimmerman <owen@fyralabs.com> - 3.1.0-1
- Initial commit
