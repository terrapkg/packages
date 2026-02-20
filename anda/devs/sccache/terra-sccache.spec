%global crate sccache
%global _description %{expand:
Sccache is a ccache-like tool. It is used as a compiler wrapper and
avoids compilation when possible. Sccache has the capability to utilize
caching in remote storage environments, including various cloud storage
options, or alternatively, in local storage.
This build actually enables caching to remote storage.}
%bcond dist %["%{_target_cpu}" == "x86_64"]

Name:          terra-sccache
Version:       0.14.0
Release:       1%{?dist}
Summary:       Remote caching enabled builds of sccache
SourceLicense: Apache-2.0 AND (Apache-2.0 OR MIT)
License:       ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:           https://crates.io/crates/sccache
Source0:       %{crates_source}
BuildRequires: anda-srpm-macros
BuildRequires: cargo
BuildRequires: cargo-rpm-macros
BuildRequires: mold
%if %{with dist}
BuildRequires: perl
%endif
BuildRequires: rust
BuildRequires: rust-srpm-macros
BuildRequires: pkgconfig(openssl)
Provides:      %{crate} = %{evr}
Packager:      Gilver E. <roachy@fyralabs.com>

%description %_description

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%cargo_build -f all%{?with_dist:,dist-server}

%install
find target/rpm \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

%cargo_license_summary_online -f all%{?with_dist:,dist-server}
%{cargo_license_online -f all%{?with_dist:,dist-server}} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc README.md
%{_bindir}/sccache
%if %{with dist}
%{_bindir}/sccache-dist
%endif

%changelog
* Fri Feb 20 2026 Gilver E. <roachy@fyralabs.com> - 0.14.0-1
- Initial package
