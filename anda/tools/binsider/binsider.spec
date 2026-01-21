Name:          binsider
Version:       0.3.1
Release:       1%?dist
Summary:       Analyze ELF binaries like a boss 😼🕵️‍♂️
License:       Apache-2.0 AND MIT
URL:           https://github.com/orhun/binsider
Source0:       %url/archive/refs/tags/v%{version}.tar.gz

BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: gcc
BuildRequires: cargo
BuildRequires: mold

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
Binsider can perform static and dynamic analysis, inspect strings, examine
linked libraries, and perform hexdumps, within a terminal user interface.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/rpm/binsider %{buildroot}%{_bindir}/binsider
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md CODE_OF_CONDUCT.md RELEASE.md SECURITY.md
%license LICENSE-APACHE LICENSE-MIT
%license LICENSE.dependencies
%{_bindir}/binsider

%changelog
* Thu Nov 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
