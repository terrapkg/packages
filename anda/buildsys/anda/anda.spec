# Work around a bug in rustc 1.95.0 with GCC
%global toolchain clang
%global crate anda

Name:           anda
Version:        0.5.4
Release:        2%{?dist}
Summary:        Andaman Build toolchain
SourceLicense:  MIT
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0-or-later AND MPL-2.0-only AND Unicode-3.0 AND (Unlicense OR MIT)
URL:            https://crates.io/crates/anda
Source0:        https://github.com/FyraLabs/anda/archive/refs/tags/%{version}.tar.gz
%if %["%{toolchain}" == "clang"]
BuildRequires:  clang
%else
BuildRequires:  gcc
%endif
BuildRequires:  rust-packaging >= 21
BuildRequires:  anda-srpm-macros
BuildRequires:  openssl-devel
%if %{defined fedora}
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  git-core
BuildRequires:  libgit2-devel
BuildRequires:  libssh2-devel
BuildRequires:  mold
Requires:       mock
Requires:       rpm-build
Requires:       createrepo_c
Requires:       git-core
Requires:       libgit2
%if 0%{?fedora} >= 42
Requires:       mock-filesystem
Requires:       util-linux-script
%endif
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
Andaman Build toolchain.

%pkg_completion -bfz

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online
%{__cargo} fetch --locked

%build
%{cargo_build} --frozen
%{cargo_license_online} > LICENSE.dependencies
%{__cargo} run --release -p xtask -- manpage
%{__cargo} run --release -p xtask -- completion

%install
%crate_install_bin

# Install shell completions
COMPDIR="target/assets/completion"

install -Dm644 $COMPDIR/bash/anda.bash -t %{buildroot}%{bash_completions_dir}
install -Dm644 $COMPDIR/zsh/_anda -t %{buildroot}%{zsh_completions_dir}
install -Dm644 $COMPDIR/fish/anda.fish -t %{buildroot}%{fish_completions_dir}

# Install man pages
install -Dm644 target/assets/man_pages/* -t %{buildroot}%{_mandir}/man1

%files
%doc README.md
%license LICENSE.dependencies LICENSE.md
%{_bindir}/anda
%{_mandir}/man1/anda*.1.*

%changelog
* Sun May 3 2026 Gilver E. <roachy@fyralabs.com> - 0.5.4-2
- Fix build on Fedora 43
- Add shell completions subpackages
