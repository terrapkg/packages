Name:           wasm-pack
Version:        0.15.0
Release:        1%{?dist}
Summary:        Your favorite Rust → Wasm workflow tool!
SourceLicense:  MIT OR Apache-2.0
License:        (%{sourcelicense}) AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/wasm-bindgen/wasm-pack
Source0:        https://github.com/wasm-bindgen/wasm-pack/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  cmake

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
This tool seeks to be a one-stop shop for building and working with rust-generated WebAssembly that
you would like to interop with JavaScript, in the browser or with Node.js. wasm-pack helps you build
rust-generated WebAssembly packages that you could publish to the npm registry, or otherwise use
alongside any javascript packages in workflows that you already use, such as webpack.

%prep
%autosetup -n wasm-pack-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/wasm-pack %{buildroot}/%{_bindir}/wasm-pack
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/wasm-pack
%license LICENSE-MIT LICENSE-APACHE
%license LICENSE.dependencies
%doc README.md CONTRIBUTING.md CHANGELOG.md CODE_OF_CONDUCT.md docs/*

%changelog
* Sat Sep 19 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
