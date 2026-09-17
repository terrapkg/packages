Name:           rust-motd
Version:        2.1.2
Release:        1%?dist
Summary:        Beautiful, useful, configurable MOTD generation with zero runtime dependencies
URL:            https://github.com/rust-motd/rust-motd
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold perl

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md DEVELOPING.md CHANGELOG.md example_config.toml example_config.kdl
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/rust-motd

%changelog
* Thu Oct 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Intial Commit
