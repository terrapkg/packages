%undefine __brp_mangle_shebangs

Name:           kittyCAD-cli
Version:        0.2.162
Release:        1%{?dist}
Summary:        The Zoo command line tool for KittyCAD
URL:            https://github.com/KittyCAD/cli
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        MIT
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
