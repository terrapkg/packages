Name:           zola
Version:        0.22.1
Release:        1%?dist
Summary:        A fast static site generator in a single binary with everything built-in
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
target/rpm/zola completion bash > completions/%{name}
target/rpm/zola completion elvish > completions/%{name}.elv
target/rpm/zola completion fish > completions/%{name}.fish
target/rpm/zola completion zsh > completions/_%{name}

%install
install -Dm755 target/rpm/zola %{buildroot}%{_bindir}/zola
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies
install -Dpm 0644 completions/%{name} -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 completions/%{name}.elv -t %{buildroot}%{elvish_completions_dir}
install -Dpm 0644 completions/%{name}.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 completions/_%{name} -t %{buildroot}%{zsh_completions_dir}

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md EXAMPLES.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/zola
%pkg_completion -Befz %{name}

%changelog
* Thu Nov 20 2025 arbormoss <arbormoss@woodsprite.dev>
- Add Shell Completions

* Wed Nov 19 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
