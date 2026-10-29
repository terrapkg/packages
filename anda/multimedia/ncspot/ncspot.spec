%global crate ncspot
%global cargo_features cover

Name:           ncspot
Version:        1.5.0
Release:        1%{?dist}
Summary:        Cross-platform ncurses Spotify client written in Rust
Packager:       like-engels <higashikataengels@icloud.com>
License:        BSD-2-Clause AND (MIT OR Apache-2.0) AND (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND MIT AND (LGPL-3.0-or-later OR MPL-2.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND (Unlicense OR MIT)
URL:            https://crates.io/crates/%{crate}
Source0:        https://github.com/hrkfdn/ncspot/archive/refs/tags/v%version.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  binutils
BuildRequires:  dbus-devel
BuildRequires:  libxcb-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  desktop-file-utils

Requires:       dbus
Requires:       libxcb
Requires:       openssl

%global _description %{expand:
ncurses Spotify client written in Rust using librespot.
It is heavily inspired by ncurses MPD clients, such as ncmpc.
It provides a simple and resource-friendly alternative to the
official Spotify client.}

%description %{_description}

%pkg_completion -bfz

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{crate}
%{_appsdir}/%{crate}.desktop
%{_mandir}/man1/*.1.gz

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%cargo_build -f "%{cargo_features}"
%{__cargo} run --manifest-path xtask/Cargo.toml -- generate-manpage
%{__cargo} run --manifest-path xtask/Cargo.toml -- generate-shell-completion
%{cargo_license_online} > LICENSE.dependencies

%install
%crate_install_bin
install -Dm644 misc/*.1 -t %{buildroot}%{_mandir}/man1
%desktop_file_install misc/%{crate}.desktop
install -Dm755 misc/%{crate}.bash -t %{buildroot}%{bash_completions_dir}
install -Dm755 misc/%{crate}.fish -t %{buildroot}%{fish_completions_dir}
install -Dm755 misc/_%{crate} -t %{buildroot}%{zsh_completions_dir}

%changelog
* Tue Oct 13 2026 Owen Zimmerman <owen@fyralabs.com> - 1.5.0-1 
- Clean up spec

* Wed Mar 18 2026 like-engels <higashikataengels@icloud.com> - 1.3.3-1
- Initial package
