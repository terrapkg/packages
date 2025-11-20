Name:           zola
Version:        0.21.0
Release:        1%?dist
Summary:        A fast static site generator in a single binary with everything built-in.
URL:            https://www.getzola.org
Source0:        https://github.com/getzola/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold glib2 libgcc clang

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
%autosetup -n %name-%version
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/zola %{buildroot}%{_bindir}/zola
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md EXAMPLES.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/zola

%changelog
* Wed Nov 19 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
