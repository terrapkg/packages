Name:           shadowenv
Version:        3.4.0
Release:        1%?dist
License:        MIT
Summary:        Reversible directory-local environment variable manipulations
URL:            https://shopify.github.io/shadowenv/
Source0:        https://github.com/Shopify/shadowenv/archive/refs/tags/%version.tar.gz
BuildRequires:  cargo cargo-rpm-macros mold

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5/
install -Dm755 target/rpm/shadowenv  %{buildroot}%{_bindir}/shadowenv
install -Dm644 man/man1/shadowenv.1  %{buildroot}%{_mandir}/man1/
install -Dm644 man/man5/shadowlisp.5 %{buildroot}%{_mandir}/man5/
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/shadowenv
%{_mandir}/man1/shadowenv.*.*
%{_mandir}/man5/shadowlisp.*.*

%changelog
* Thu Jan 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
