Name:           framework-system
Version:        0.4.5
Release:        2%?dist
Summary:        Rust libraries and tools to interact with the Framework Computer systems
URL:            https://github.com/FrameworkComputer/framework-system
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND MIT AND MPL-2.0 AND (Unlicense OR MIT)
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold
BuildRequires:  rust-udev-devel
BuildRequires:  rust
BuildRequires:  systemd-devel
BuildRequires:  hidapi-devel
Requires:       rustup
Provides:       framework_tool
ExclusiveArch:  x86_64

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%pkg_completion -bz framework_tool

%prep
%autosetup -n framework-system-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/framework_tool %{buildroot}%{_bindir}/framework_tool
install -Dm 644 completions/bash/framework_tool %{buildroot}%{bash_completions_dir}/framework_tool.bash
install -Dm 644 completions/zsh/_framework_tool %{buildroot}%{zsh_completions_dir}/_framework_tool
%{cargo_license_online} > LICENSE.dependencies

%files
%doc EXAMPLES.md EXAMPLES_ADVANCED.md README.md support-matrices.md
%license LICENSE.md
%license LICENSE.dependencies
%{_bindir}/framework_tool

%changelog
* Tue Dec 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
