%global commit 4413a0225966c2f9d19f0bcbcd754e2d62d56941
%global commit_date 20260213
%global shortcommit %{sub %{commit} 0 7}

%undefine __brp_mangle_shebangs

Name:           alipad
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Robust event check-in system
URL:            https://git.sr.ht/~malicean/alipad
Source0:        https://git.sr.ht/~malicean/alipad/archive/%{commit}.tar.gz
License:        BSD-3-Clause
BuildRequires:  cargo-rpm-macros cargo gcc rust-udev-devel

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
install -Dm755 target/rpm/alipad %{buildroot}%{_bindir}/alipad

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/alipad

%changelog
* Sat Feb 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
