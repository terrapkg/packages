Name:           pixi
Version:        0.65.0
Release:        1%?dist
Summary:        A cross-platform, multi-language package manager
License:        BSD-3-Clause
URL:            https://pixi.sh
Source:         https://github.com/prefix-dev/pixi/archive/refs/tags/v%{version}.tar.gz
Packager:       metcya <metcya@gmail.com>

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold

%pkg_completion -Befz

%description
pixi is a cross-platform, multi-language package manager and workflow tool
built on the foundation of the conda ecosystem. It provides developers with an
exceptional experience similar to popular package managers like cargo or npm,
but for any language.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
for shell in bash elvish fish zsh; do
    target/rpm/%{name} completion --shell $shell > completions.$shell
done
%dnl %cargo_license_online > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 completions.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dm 644 completions.elvish %{buildroot}%{elvish_completions_dir}/%{name}.elv
install -Dm 644 completions.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dm 644 completions.zsh %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%doc README.md SECURITY.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed Dec 17 2025 metcya <metcya@gmail.com> - 0.62.0
- Initial package
