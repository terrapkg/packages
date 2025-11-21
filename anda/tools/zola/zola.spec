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
target/rpm/zola completion bash > %{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.bash -t %{elvish_completions_dir}/%{name}
target/rpm/zola completion elvish > %{elvish_completions_dir}/%{name}.elv
install -Dpm 0644 %{name}.elv -t %{elvish_completions_dir}/%{name}.elv
target/rpm/zola completion fish > %{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.fish -t %{fish_completions_dir}/%{name}.fish
target/rpm/zola completion zsh > %{zsh_completions_dir}/_%{name}
install -Dpm 0644 %{name}.zsh -t %{zsh_completions_dir}/_%{name}

%pkg_completion -Befz %{name}

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
* Thu Nov 20 2025 arbormoss <arbormoss@woodsprite.dev>
- Add Shell Completions

* Wed Nov 19 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
