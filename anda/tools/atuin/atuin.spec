Name:           atuin
Version:        18.12.1
Release:        1%?dist
Epoch:          1
Summary:        Magical shell history 
URL:            https://github.com/atuinsh/atuin
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       atuin
Packager:       Riley Loo <dev@zackerthescar.com>

%description
%summary.

%prep
%autosetup -n atuin-%version
%cargo_prep_online

%build
%cargo_build -- --package atuin

%install
install -Dm755 target/rpm/atuin %{buildroot}%{_bindir}/atuin
%{cargo_license_online} > LICENSE.dependencies

%files
%_bindir/atuin
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat Feb 24 2026 Riley Loo <dev@zackerthescar.com>
- Initial package