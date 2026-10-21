%global crate cargo-binstall

%undefine __brp_mangle_shebangs

Name:           cargo-binstall
Version:        1.26.0
Release:        1%{?dist}
Summary:        Binary installation for rust projects
License:        GPL-3.0-only
URL:            https://crates.io/crates/cargo-binstall
Source:         %{terra_crates_source}
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%files
%doc README.md
%license LICENSE
%{_bindir}/cargo-binstall

%changelog
* Tue Oct 20 2026 Owen Zimmerman <owen@fyralabs.com> - 1.26.0-1
- Initial commit
