%undefine __brp_mangle_shebangs

Name:           gurk
Version:        0.8.1
Release:        1%?dist
Summary:        Signal Messenger client for terminal
License:        AGPL-3.0-or-later AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CDLA-Permissive-2.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/boxdot/gurk-rs
Source:         %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  glibc-devel mold perl openssl-devel protobuf-devel
Requires:       glibc libgcc sqlcipher

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n gurk-rs-%{version}
%cargo_prep_online

%build

%install
export LC_ALL=C.UTF-8
export LANG=C
unset RUSTC_WRAPPER
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md
%license LICENSE-AGPL-3.0
%{_bindir}/gurk

%changelog
* Fri Feb 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
