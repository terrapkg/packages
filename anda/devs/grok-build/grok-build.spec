%global commit 97f190f644ae1ba07fd6ee185ef54c650e142666
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260929
%global ver 1.0.45

# Fedora injects -Cdebuginfo=2 via RUSTFLAGS; with debuginfo included rustc
# peaks >9 GB RSS and gets OOM-killed on x86_64 while compiling
# xai-grok-shell, so debuginfo stays off. Strip symbols at link time
# (~36 MB of .symtab/.strtab saved). Thin LTO + one codegen unit mirror
# upstream's release-dist shipping profile. These are set via
# CARGO_PROFILE_RPM_* env vars rather than RUSTFLAGS: %%cargo_build compiles
# with the "rpm" cargo profile set up by %%cargo_prep_online, and profile
# settings hold regardless of -C argument ordering.
%global debug_package %{nil}
%global build_rustflags -Copt-level=3 -Cforce-frame-pointers=yes -Clink-arg=-specs=/usr/lib/rpm/redhat/redhat-package-notes --cap-lints=warn
%global cargo_dist_env CARGO_PROFILE_RPM_DEBUG=0 CARGO_PROFILE_RPM_STRIP=symbols CARGO_PROFILE_RPM_LTO=thin CARGO_PROFILE_RPM_CODEGEN_UNITS=1

Name:           grok-build
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Terminal AI coding agent by xAI
# Legal-Review-Notice (boo#1273104): licences of the statically linked Rust
# dependencies, verified against the vendored tree with
# "cargo tree -p xai-grok-pager-bin -e normal" (1009 crates in this graph,
# 1245 vendored):
#  - pdf_oxide IS shipped (pulled with its "rendering" feature), but it is
#    "MIT OR Apache-2.0" and carries no GPL code. Its src/decoders/jbig2.rs is
#    a pass-through stub ("no actual decoding performed"); its sole GPL-3.0
#    string is a doc comment naming the jbig2dec crate as an implementation
#    option upstream deliberately did NOT take.
#  - The JBIG2 decoder that "rendering" really pulls in is hayro-jbig2, which
#    is "Apache-2.0 OR MIT".
#  - MPL-2.0 below covers the 8 statically linked MPL-2.0 crates: cssparser,
#    cssparser-macros, dtoa-short, nucleo, nucleo-matcher, option-ext,
#    selectors and smartstring (MPL-2.0+).
#  - colored_json (EPL-2.0) is NOT in this binary's dependency graph; it is
#    reachable only from xai-ratatui-inline, which this package does not build.
#  - GPL-2.0 WITH Linking-exception and LGPL-2.1-or-later cover the libgit2 C
#    sources that libgit2-sys bundles and links statically: libgit2 itself is
#    GPL-2.0 with the linking exception, and its deps/xdiff (LibXDiff) is
#    LGPL-2.1-or-later. The LGPL-covered deps/winhttp is Windows-only and is
#    not compiled here.
#  - aws-lc-sys, rust-stemmers and zstd-sys ship a GPL licence text but none
#    applies: aws-lc expressly elects ISC over GPL-2.0, rust-stemmers' GPL-3.0
#    covers only its test_data, and zstd is dual BSD-3-Clause/GPL-2.0.
License:        Apache-2.0 AND MPL-2.0 AND GPL-2.0 WITH Linking-exception AND LGPL-2.1-or-later
SourceLicense:  Apache-2.0
URL:            https://github.com/xai-org/grok-build
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         0001-disable-self-updater.patch
Patch1:         0002-disable-telemetry-by-default.patch
Patch2:         0003-protoc-dep-compat.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(oniguruma) >= 6.9.3
BuildRequires:  protobuf-compiler
BuildRequires:  ripgrep
BuildRequires:  rust >= 1.85

# grok shells out to ripgrep at runtime for its in-tree code search; the build
# is also pointed at the system rg (see GROK_*_BUNDLE_RG_PATH in %%build).
Requires:       ripgrep

Packager:       Leo Douglas <douglarek@gmail.com>

%description
Grok is xAI's terminal-based AI coding agent: an interactive TUI that pairs
with the Grok models to read, edit and reason about code in your working
directory, run shell commands and drive common developer workflows from the
command line.

This package ships the agent as the %{_bindir}/grok command.

%pkg_completion -Bzf grok

%prep
%autosetup -p1 -n %{name}-%{commit}
# Upstream pins an exact toolchain via rustup; drop it so the distribution
# rust/cargo is used instead of trying to invoke rustup at build time.
rm -f rust-toolchain.toml
# The bundled bin/protoc is a dotslash launcher that downloads protoc from the
# network at build time. Use the system protoc instead (see PROTOC export in
# %%build, protobuf-compiler).
rm -f bin/protoc
# Keep the snapshot's dependency lock: %%cargo_prep_online removes Cargo.lock,
# which would float every one of the ~1200 vendored crates to the latest
# semver-compatible release on crates.io and make builds unreproducible (the
# license review above is pinned to the lockfile).
cp -p Cargo.lock Cargo.lock.rpmsave
%cargo_prep_online
mv -f Cargo.lock.rpmsave Cargo.lock

%build
export PROTOC=%{_bindir}/protoc
# syntect's regex engine is onig_sys, which otherwise compiles the oniguruma C
# sources it bundles; link the system library instead (pre-generated bindings,
# so no bindgen is pulled in).
export RUSTONIG_SYSTEM_LIBONIG=1
# The xai-grok-tools and xai-grok-shell build scripts embed a ripgrep binary
# and otherwise download it from GitHub at build time. Point both at the
# system ripgrep so the build stays offline (see BuildRequires: ripgrep).
export GROK_TOOLS_BUNDLE_RG_PATH=%{_bindir}/rg
export GROK_SHELL_BUNDLE_RG_PATH=%{_bindir}/rg
export CARGO_INCREMENTAL=0
export %{cargo_dist_env}
# Cap parallel rustc jobs by available memory: the xai-grok-shell rustc grows
# with the parallel LLVM threads it gets from the cargo jobserver (28 GB RSS
# with 32 jobs), so bind it at one job per 8 GB.
%limit_build -m 8000
%cargo_build -- --package xai-grok-pager-bin

%install
install -D -m 0755 target/rpm/xai-grok-pager %{buildroot}%{_bindir}/grok
# Shell completions, generated by the binary's own clap_complete generator.
mkdir -p %{buildroot}%{bash_completions_dir} \
         %{buildroot}%{zsh_completions_dir} \
         %{buildroot}%{fish_completions_dir}
target/rpm/xai-grok-pager completions bash \
  > %{buildroot}%{bash_completions_dir}/grok
target/rpm/xai-grok-pager completions zsh \
  > %{buildroot}%{zsh_completions_dir}/_grok
target/rpm/xai-grok-pager completions fish \
  > %{buildroot}%{fish_completions_dir}/grok.fish

%files
%license LICENSE
%doc README.md THIRD-PARTY-NOTICES
%{_bindir}/grok

%changelog
* Tue Sep 29 2026 Leo Douglas <douglarek@gmail.com> - 1.0.45^20260929git.97f190f-1
- Initial package
