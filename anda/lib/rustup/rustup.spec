%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

Name:           rustup
Version:        1.29.0
Release:        1%{?dist}
Summary:        Manage multiple rust installations with ease
Packager:       Cypress Reed <cypress@fyralabs.com>

SourceLicense:  MIT OR Apache-2.0
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND Unicode-3.0 AND Unicode-DFS-2016 AND Zlib AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/rust-lang/rustup
Source0:        %{url}/archive/%{version}/rustup-%{version}.tar.gz

# non-upstreamable patches:
# * drop Windows-specific dependencies
Patch:          0001-Drop-Windows-specific-dependencies.patch
# * drop unavailable "openssl/vendored" feature
Patch:          0002-Drop-feature-for-statically-linking-against-vendored.patch
# * remove unused tracing support and unnecessary "rs_tracing" dependency
Patch:          0003-Remove-unused-tracing-support.patch
# * remove unused git-based versioning and unnecessary "git-testament" dependency
Patch:          0004-Remove-unused-git-based-versioning.patch
# * Revert back to rustls/ring instead of aws_lc_rs
Patch:          0005-Revert-back-to-rustls-ring-instead-of-aws_lc_rs.patch
# * Disable tests/suite/static_roots to avoid a few dev-deps
Patch:          0006-Disable-tests-suite-static_roots.patch
# * Unpin tracing-subscriber
#   https://github.com/rust-lang/rustup/pull/4745
#   https://github.com/tokio-rs/tracing/issues/3369
Patch:          0007-Unpin-tracing-subcriber.patch

# Upgrade to rustls-platform-verifier 0.7
# (without changes to Cargo.lock)
# https://github.com/rust-lang/rustup/commit/4d7b4b68b9736aa1dccf43c4b6df0976e88b3c8a
Patch:          0008-Upgrade-to-rustls-platform-verifier-0.7.patch

ExcludeArch:    %{ix86}

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(openssl)

%description
Manage multiple rust installations with ease.

%pkg_completion -bfz

%prep
%autosetup -n rustup-%{version} -p1
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install -f no-self-update

# Generate and install shell completions for %pkg_completion.
cp -pav target/rpm/rustup-init target/rpm/rustup
target/rpm/rustup completions bash > rustup.bash
target/rpm/rustup completions fish > rustup.fish
target/rpm/rustup completions zsh > _rustup

install -Dpm 0644 rustup.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 rustup.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 _rustup -t %{buildroot}%{zsh_completions_dir}

%if %{with check}
%check
# * skip tests that require internet access
# * skip tests for the "rustup" binary that is not built in this package
# * skip harmless test failures due to mismatch with the "platforms" crate
%cargo_test -f test -- -- --skip suite::cli_exact::check_updates --skip suite::cli_ui::rustup_ui_doc_text_tests --skip suite::known_tuples::gen_known_tuples
%endif

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md

%{_bindir}/rustup-init

%changelog
* Mon Aug 10 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package from Fedora rustup
