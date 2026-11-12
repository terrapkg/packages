%global crate resolvematrix-cli
%global __cargo_common_opts %{?_smp_mflags}
%global __cargo_license_avoid_dev_deps 0

Name:           resolvematrix
Version:        1.4.1
Release:        1%{?dist}
Summary:        A handy Matrix server resolution tool
URL:            https://forgejo.ellis.link/continuwuation/resolvematrix
Source0:        https://forgejo.ellis.link/continuwuation/resolvematrix/archive/v%{version}.tar.gz
SourceLicense:  MPL-2.0-no-copyleft-exception
License:        (ISC AND (Apache-2.0 OR ISC)) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND CDLA-Permissive-2.0 AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND ISC AND ((MIT OR Apache-2.0) AND Apache-2.0) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
BuildRequires:  cargo rust-srpm-macros anda-srpm-macros cargo-rpm-macros

Packager:       julian45 <julian@julian45.net>

%description
resolvematrix is a Rust library and CLI providing the ability to resolve
Matrix server-to-server endpoints from the server name. It conforms to
the "Server discovery" chapter of the Matrix specification.

%prep
%autosetup -n resolvematrix
# First round of dep grabs
%cargo_prep_online
# Move into CLI dir
cd cli
# Second round of deps
%cargo_fetch

%build
pushd cli
%cargo_build
popd
%cargo_license_summary_online

%install
install -Dm755 target/rpm/resolvematrix %{buildroot}%{_bindir}/resolvematrix
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/resolvematrix

%changelog
* Thu Nov 05 2026 julian45 <julian@julian45.net>
- Initial package
