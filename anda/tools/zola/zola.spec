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
mkdir -p completions
for shell in bash zsh elvish fish; do
    target/rpm/%{crate} completion $shell > completions/%{crate}-completion.$shell
done

%install
install -Dm755 target/rpm/zola %{buildroot}%{_bindir}/zola
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies
install -Dm644 completions/%{crate}-completion.bash %{bash_completions_dir}/%{crate}
install -Dm644 completions/%{crate}-completion.zsh %{zsh_completions_dir}/_%{crate}
install -Dm644 completsion/%{crate}-completion.elvish %{elvish_completions_dir}/%{crate}.elv
install -Dm644 completions/%{crate}-completion.fish %{fish_completions_dir}/%{crate}.fish

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md EXAMPLES.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/zola

%pkg_completion -Bzef

%changelog
* Wed Nov 19 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
