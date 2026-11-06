Name:           spotifast
Version:        0.17.1
Release:        1%{?dist}
Summary:        A native Spotify client
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND OFL-1.1 AND Ubuntu-font-1.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (LGPL-3.0-or-later OR MPL-2.0) AND (MIT AND ISC) AND (MIT AND OFL-1.1) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR BSD-3-Clause) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND LGPL-3.0-or-later AND MIT AND MPL-2.0 AND Unicode-3.0 AND Unlicense AND Zlib
URL:            https://github.com/crmne/spotifast
Source0:        https://github.com/crmne/spotifast/archive/refs/tags/v0.17.1.tar.gz
SourceLicense:  MIT
BuildRequires:  cargo
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros

Packager:       kiritanya <kiritanya@proton.me>

%description
A native Spotify client

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/spotifast %{buildroot}%{_bindir}/spotifast
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/spotifast

%changelog
* Fri Nov 06 2026 kiritanya <kiritanya@proton.me> - 0.17.1-1
- initial package
