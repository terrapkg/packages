%undefine __brp_mangle_shebangs

Name:           rfc_reader
Version:        0.11.2
Release:        1%?dist
Summary:        An RFC viewer with TUI
URL:            https://github.com/ozan2003/rfc_reader
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CDLA-Permissive-2.0 AND MIT AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(openssl)
# Build fails without this, all deps are listed above.
AutoReqProv:    0

Provides:       rfc-reader

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build

%install
%cargo_install
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/rfc_reader
%ghost %{_datadir}/cargo/registry/%{name}-%{version}/*
%ghost %{_datadir}/cargo/registry//%{name}-%{version}/.cargo-checksum.json

%changelog
* Thu Feb 05 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
