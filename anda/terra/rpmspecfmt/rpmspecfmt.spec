Name:     rpmspecfmt
Version:  0.2.0
Release:  1%{?dist}
Summary:  Formatter for RPM spec files
License:  (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND AGPL-3.0-or-later AND Apache-2.0 AND MIT
URL:      https://github.com/kiritanya/rpmspecfmt
Packager: kiritanya <kiritanya@proton.me>

Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: anda-srpm-macros
BuildRequires: cargo
BuildRequires: cargo-rpm-macros

SourceLicense: AGPL-3.0-or-later

%description
Formatter for RPM spec files.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/rpmspecfmt %{buildroot}%{_bindir}/rpmspecfmt
install -Dm755 target/rpm/rpmspeclint %{buildroot}%{_bindir}/rpmspeclint
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/rpmspecfmt
%{_bindir}/rpmspeclint

%changelog
* Sat Nov 21 2026 kiritanya <kiritanya@proton.me> - 0.2.0-1
- initial package
