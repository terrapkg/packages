Name:           codex
Version:        0.162.1
Release:        1%{?dist}
Summary:        Lightweight coding agent that runs in your terminal

SourceLicense:  Apache-2.0
License:        (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR BSD-3-Clause (*)) AND Apache-2.0 (*) AND (Apache-2.0 OR ISC OR MIT (*)) AND (Apache-2.0 OR ISC OR MIT) AND Unicode-3.0 (*) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0) AND ISC (*) AND (Unlicense OR MIT (*)) AND (MIT OR Zlib OR Apache-2.0 (*)) AND BSL-1.0 (*) AND (Zlib OR Apache-2.0 OR MIT (*)) AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 OR BSL-1.0) AND (ISC AND (Apache-2.0 OR ISC) (*)) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 (*) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND CDLA-Permissive-2.0 (*) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception (*)) AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT (*)) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND MIT AND BSD-3-Clause AND Apache-2.0 AND ISC (*) AND BSL-1.0 AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Apache-2.0) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause (*)) AND (Apache-2.0 OR MIT (*)) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 (*)) AND BSD-3-Clause (*) AND (Unlicense OR MIT) AND MIT (*)

URL:            https://github.com/openai/codex
Source0:        %{url}/archive/refs/tags/rust-v%{version}.tar.gz

Packager:       Jaiden Riordan <jade@fyralabs.com>

BuildRequires:  anda-srpm-macros cargo-rpm-macros gcc gcc-c++ pkgconfig(openssl) pkgconfig(dbus-1)

Requires:       bubblewrap

Recommends:     ripgrep git

%description
%summary.

%prep
%autosetup -n codex-rust-v%{version} -p1
cd codex-rs
sed -i 's/^version = "0\.0\.0"$/version = "%{version}"/' Cargo.lock
%cargo_prep_online

%build
cd codex-rs
export CODEX_SKIP_BWRAP_BUILD=1
# we had to do this for zed too
# tl;dr it doesn't catch non-direct licences, so we do this
%{__cargo} tree                                                          \
    -Z avoid-dev-deps                                                    \
    --package codex-cli                                                  \
    --edges no-build,no-dev,no-proc-macro                                \
    --target all                                                         \
    --prefix none                                                        \
    --format "{l}: {p}"                                                  \
    | sed -e "s: ($(pwd)[^)]*)::g" -e ":b; s/^\([^:]*\)*\//\1 OR /; tb;" \
    | sed -e '/.*(\*).*/d'                                               \
    | sort -u                                                            \
> ../LICENSE.dependencies
%cargo_build -- --package codex-cli

%install
install -Dm755 codex-rs/target/rpm/codex %{buildroot}%{_bindir}/codex

mkdir -p %{buildroot}%{bash_completions_dir} \
         %{buildroot}%{zsh_completions_dir} \
         %{buildroot}%{fish_completions_dir}
%{buildroot}%{_bindir}/codex completion bash > %{buildroot}%{bash_completions_dir}/codex
%{buildroot}%{_bindir}/codex completion zsh  > %{buildroot}%{zsh_completions_dir}/_codex
%{buildroot}%{_bindir}/codex completion fish > %{buildroot}%{fish_completions_dir}/codex.fish

%files
%license LICENSE NOTICE LICENSE.dependencies
%doc README.md
%{_bindir}/codex

%pkg_completion -Bzf

%changelog
* Mon Oct 12 2026 Jaiden Riordan <jade@fyralabs.com>
- Initial package
