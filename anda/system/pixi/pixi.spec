Name:           pixi
Version:        0.62.0
Release:        1%{?dist}
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
%cargo_license_online > LICENSE.dependencies

%install
%crate_install_bin
target/release/%{name} completion bash > %bash_completion_dir 
target/release/%{name} completion elvish > %elvish_completion_dir 
target/release/%{name} completion fish > %fish_completion_dir 
target/release/%{name} completion zsh > %zsh_completion_dir 

%files
%doc README.md SECURITY.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Wed Dec 17 2025 metcya <metcya@gmail.com> - 0.62.0
- Initial package
