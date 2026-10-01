%global crate cargo-about

Name:           cargo-about
Version:        0.9.2
Release:        1%{?dist}
Summary:        Cargo plugin for generating a license listing for all dependencies of a crate
SourceLicense:  MIT OR Apache-2.0
License:        (Apache-2.0 AND ISC) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND MIT AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://github.com/EmbarkStudios/cargo-about
Source0:        %{crates_source}
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold
Packager:       Gilver E. <roachy@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build -f cli

%install
%crate_install_bin
%{cargo_license_online -f cli} > LICENSE.dependencies

%files
%doc README.md
%doc SECURITY.md
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Wed Sep 30 2026 Gilver E. <roachy@fyralabs.com> - 0.9.2-1
- Initial package
