%undefine __brp_mangle_shebangs

Name:           subatomic-v1
Version:        1.0.0
Release:        1%{?dist}
Summary:        A modern package delivery system
SourceLicense:  AGPL-3.0-or-later
License:        (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND bzip2-1.0.6 AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND AGPL-3.0-or-later AND (0BSD OR MIT OR Apache-2.0) AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND Unicode-3.0 AND MPL-2.0+ AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND MIT AND BSD-3-Clause AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/FyraLabs/subatomic
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  ostree-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Subatomic is a package delivery system which supports multiple package formats.
It manages a repository of packages, handling updating, signing, and other
tasks.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
pushd crates/kiritan
%cargo_build
popd

%install
install -Dm 755 target/rpm/subatomic    %{buildroot}%{_bindir}/subatomic
install -Dm 755 target/rpm/kiritan      %{buildroot}%{_bindir}/kiritan
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md docs/*
%license LICENSE LICENSE.dependencies
%{_bindir}/subatomic
%{_bindir}/kiritan

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com> - 1.0.0-1
- Convert to rust format

* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
