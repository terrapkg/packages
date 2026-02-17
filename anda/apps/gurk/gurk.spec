%undefine __brp_mangle_shebangs

Name:           gurk
Version:        0.8.1
Release:        1%?dist
Summary:        Signal Messenger client for terminal
License:        AGPL-3.0-or-later
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
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md
%license LICENSE-AGPL-3.0
%{_bindir}/gurk

%changelog
* Fri Feb 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
