%global commit 4413a0225966c2f9d19f0bcbcd754e2d62d56941
%global commit_date 20260213
%global shortcommit %{sub %{commit} 0 7}

%undefine __brp_mangle_shebangs

Name:           alipad
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Robust event check-in system
URL:            https://git.sr.ht/~malicean/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz
SourceLicense:  BSD-3-Clause
License:        %{SourceLicense} AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Zlib OR Apache-2.0) AND (0BSD OR MIT OR Apache-2.0) AND Zlib AND MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MPL-2.0 AND (# (MIT OR Apache-2.0) AND Unicode-3.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (GPL-3.0 OR MIT) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  cargo-rpm-macros
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  rust-udev-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A low-budget and robust event check-in system built atop a Proxmark3 and
set of ISO/IEC 14443-3 compliant smartcards which your attendees bring
(NTAG, Mifare, Ventra, generic NFC, and more), in order to simplify and
speed-up the check-in process. To the attendees, it's faster, easier, and has a charm!

%prep
%autosetup -n %{name}-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_license_summary_online
install -Dm755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Sep 25 2026 Its-J <jonah@fyralabs.com>
- Added dep licenses

* Sat Feb 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
