Name:           weave
Version:        0.5.1
Release:        2%?dist
Summary:        Entity-level git merge driver

License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://ataraxy-labs.github.io/weave/
Source0:        https://github.com/ataraxy-labs/weave/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
Provides:       weave-driver = %evr

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(openssl)

%description
Entity-level semantic merge driver for Git.
Resolves merge conflicts that Git can't by understanding code structure via tree-sitter. 


%prep
%autosetup
%cargo_prep_online


%build
cargo update
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies


%install
pushd crates/weave-cli
%cargo_install
popd
pushd crates/weave-driver
%cargo_install
popd


#check
#cargo_check


%files
%license LICENSE-APACHE LICENSE-MIT LICENSE.dependencies
%doc README.md
%_bindir/weave
%_bindir/weave-driver

%changelog
* Mon Jul 20 2026 madonuko <mado@fyralabs.com> - 0.3.6-1
- Initial package
