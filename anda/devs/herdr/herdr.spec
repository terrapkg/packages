Name:           herdr
Version:        0.9.5
Release:        1%{?dist}
Summary:        Terminal workspace manager for AI coding agents

License:        ((Apache-2.0 OR MIT) AND Unicode-3.0) AND (0BSD OR Apache-2.0 OR MIT) AND (0BSD OR Apache-2.0) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR LGPL-2.1-or-later OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND 0BSD AND Apache-2.0 AND MIT AND Zlib
SourceLicense:  Apache-2.0
URL:            https://herdr.dev
Source0:        https://github.com/herdrdev/herdr/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-disable-self-update-for-rpm-installs.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.96
BuildRequires:  zig >= 0.16.0

Recommends:     openssh-clients

Packager:       Zeldris <80939130+zeldrisho@users.noreply.github.com>

%description
Herdr is a terminal workspace manager for AI coding agents. It keeps terminals
running in a background server when the client closes or an SSH connection
drops, organizes them into workspaces, tabs and panes, detects the coding
agents running inside them, and exposes the current session to agents through
a CLI and socket API.

%pkg_completion -Bzf

%prep
%autosetup -p1 -n %{name}-%{version}
# Upstream pins its toolchain through rustup; use the distribution rust/cargo.
rm -f rust-toolchain.toml
# Preserve both licenses: RPM flattens %%license paths into one directory.
cp -p vendor/libghostty-vt/LICENSE LICENSE.libghostty-vt
%cargo_prep_online
# The vendored libghostty-vt build pulls its Zig dependencies from the network.
# Fetch and unpack them once here so the cargo build script can build the
# library without needing network access during %%build.
export ZIG_GLOBAL_CACHE_DIR=%{_builddir}/zig-global-cache
(cd vendor/libghostty-vt && zig build -Demit-lib-vt -Doptimize=ReleaseFast --summary none)

%build
export ZIG_GLOBAL_CACHE_DIR=%{_builddir}/zig-global-cache
# Match the profile upstream ships in its release binaries.
export LIBGHOSTTY_VT_OPTIMIZE=ReleaseFast
export LIBGHOSTTY_VT_SIMD=true
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dpm755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{bash_completions_dir} \
         %{buildroot}%{zsh_completions_dir} \
         %{buildroot}%{fish_completions_dir}
target/rpm/%{name} completion bash > %{buildroot}%{bash_completions_dir}/%{name}
target/rpm/%{name} completion zsh  > %{buildroot}%{zsh_completions_dir}/_%{name}
target/rpm/%{name} completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish

%files
%license LICENSE
%license LICENSE.dependencies
%license LICENSE.libghostty-vt
%license vendor/portable-pty/LICENSE.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}

%changelog
* Fri Nov 13 2026 Zeldris <80939130+zeldrisho@users.noreply.github.com> - 0.9.5-1
- Initial package
