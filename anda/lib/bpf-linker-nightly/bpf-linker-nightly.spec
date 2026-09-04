%global crate bpf-linker
%global llvm_version 22.1.8
%bcond check 0

Name:           bpf-linker-nightly
Version:        0.11.0
Release:        1%{?dist}
Summary:        BPF static linker built with Rust nightly
URL:            https://github.com/aya-rs/bpf-linker
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT OR Apache-2.0
License:        (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)

BuildRequires:  cargo-rpm-macros
BuildRequires:  rustup
BuildRequires:  llvm-devel
BuildRequires:  clang-devel

Conflicts:      bpf-linker

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
bpf-linker is a bitcode linker for statically linking BPF object files and
performing optimizations needed to target older kernels. This package is built
with the Rust nightly toolchain and installs the command as
bpf-linker.

%prep
%autosetup -n %{crate}-%{version}
%rustup_nightly
rust_toolchain=$(rustc +nightly --version | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | tail -n 1)
if [ -z "$rust_toolchain" ]; then
    echo "Unable to determine the Rust nightly toolchain date" >&2
    exit 1
fi
printf 'nightly-%s\n' "$rust_toolchain" > rust-toolchain
%cargo_prep_online

# Select the LLVM major version tracked for this buildroot.
llvm_version=%{llvm_version}
llvm_major=$(printf '%s\n' "$llvm_version" | sed 's/\..*//')
llvm_config=%{_bindir}/llvm-config-$llvm_major
if [ ! -x "$llvm_config" ]; then
    echo "No llvm-config found for LLVM $llvm_version" >&2
    exit 1
fi
if ! grep -q "^llvm-$llvm_major =" Cargo.toml; then
    echo "bpf-linker does not support Rust nightly LLVM $llvm_major" >&2
    exit 1
fi
sed -i -E "s/^default = \\[\"llvm-[0-9]+\"\\]/default = [\"llvm-$llvm_major\"] /" Cargo.toml
mkdir -p .cargo/bin
ln -s "$llvm_config" .cargo/bin/llvm-config

%build
export PATH="$PWD/.cargo/bin:%{_bindir}:$PATH"
export LLVM_CONFIG_PATH="$PWD/.cargo/bin/llvm-config"
%cargo_build

%install
install -Dm755 target/rpm/%{crate} %{buildroot}%{_bindir}/bpf-linker
install -Dm644 rust-toolchain %{buildroot}%{_datadir}/%{name}/rust-toolchain
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bpf-linker
%{_datadir}/%{name}/rust-toolchain

%changelog
* Mon Aug 10 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
