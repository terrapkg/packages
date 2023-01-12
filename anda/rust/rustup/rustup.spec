Name:           rustup
Version:        1.25.1
Release:        %autorelease
URL:            https://rust-lang.github.io/rustup/
License:        MIT, Apache-2.0
Summary:        The Rust toolchain installer
Source0:        https://github.com/rust-lang/rustup/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo pkgconfig(openssl)

%description
Rustup installs The Rust Programming Language from the official release channels,
enabling you to easily switch between stable, beta, and nightly compilers and keep them updated.
It makes cross-compiling simpler with binary builds of the standard library for common platforms.


%prep
%setup -n rustup-%{version}


%build
cargo build --release --features no-self-update --bin rustup-init


%install
install -Dm755 target/release/rustup-init %{buildroot}/usr/bin/rustup

_binlinks=('cargo' 'rustc' 'rustdoc' 'rust-gdb' 'rust-lldb' 'rls' 'rustfmt' 'cargo-fmt' 'cargo-clippy' 'clippy-driver' 'cargo-miri')
cd %{buildroot}
for link in "${_binlinks[@]}"; do
    ln %{buildroot}/usr/bin/rustup usr/bin/${link}
done

# Generate completion files.
mkdir -p %{buildroot}/usr/share/bash-completion/completions
%{buildroot}/usr/bin/rustup completions bash > %{buildroot}/usr/share/bash-completion/completions/rustup
%{buildroot}/usr/bin/rustup completions bash cargo > %{buildroot}/usr/share/bash-completion/completions/cargo
mkdir -p %{buildroot}/usr/share/fish/vendor_completions.d
%{buildroot}/usr/bin/rustup completions fish > %{buildroot}/usr/share/fish/vendor_completions.d/rustup.fish
mkdir -p %{buildroot}/usr/share/zsh/site-functions
%{buildroot}/usr/bin/rustup completions zsh > %{buildroot}/usr/share/zsh/site-functions/_rustup
%{buildroot}/usr/bin/rustup completions zsh cargo > %{buildroot}/usr/share/zsh/site-functions/_cargo


%post
echo "You may need to run rustup update stable"
echo "and possibly also rustup self upgrade-data"


%files
%doc README.md
%license LICENSE-MIT
%license LICENSE-APACHE
/usr/bin/rustup
/usr/bin/{cargo,rustc,rustdoc,rust-gdb,rust-lldb,rls,rustfmt,cargo-fmt,cargo-clippy,clippy-driver,cargo-miri}
/usr/share/bash-completion/completions/{rustup,cargo}
/usr/share/fish/vendor_completions.d/rustup.fish
/usr/share/zsh/site-functions/{_cargo,_rustup}


%changelog
* Sun Dec 4 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
