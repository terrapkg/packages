Name:           brush-shell
Version:        0.4.0
Release:        1%{?dist}
Summary:        bash/POSIX-compatible shell implemented in Rust
URL:            https://github.com/reubeno/brush
Source0:        %{url}/archive/refs/tags/%{name}-v%{version}.tar.gz
License:        ((MIT OR Apache-2.0) AND NCSA) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND WTFPL AND Zlib AND (Zlib OR Apache-2.0 OR MIT)

BuildRequires:  cargo-rpm-macros

Provides:       brush
Packager:       Its-J <jonah@fyralabs.com>

%description
brush-shell is a modern bash- and POSIX- compatible shell written in Rust.
Run your existing scripts and .bashrc unchanged
with built-in syntax highlighting and auto-suggestions.

%prep
%autosetup -n brush-%{name}-v%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/brush %{buildroot}%{_bindir}/brush
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/brush
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sun May 10 2026 Its-J <jonah@fyralabs.com>
- Package brush
