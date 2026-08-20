%undefine __brp_mangle_shebangs

Name:           wlctl
Version:        0.1.10
Release:        1%{?dist}
Summary:        TUI for managing wifi/ethernet/vpn on Linux with Network Manager
URL:            https://github.com/aashish-thapa/wlctl
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  GPL-3.0-or-later
License:        MIT AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CDLA-Permissive-2.0 AND MIT AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%crate_install_bin
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc Readme.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Sat Aug 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
