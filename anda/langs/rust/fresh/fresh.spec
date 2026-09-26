%undefine __brp_mangle_shebangs

Name:           fresh
Version:        0.5.1
Release:        2%{?dist}
Summary:        Text editor for your terminal: easy, powerful and fast
URL:            https://getfresh.dev
Source0:        https://github.com/sinelaw/fresh/archive/refs/tags/v%version.tar.gz
SourceLicense:  GPL-2.0-only
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (BSD-2-Clause OR Apache-2.0) AND (0BSD OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND GPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND BSL-1.0 AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND 0BSD AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Apache-2.0 WITH LLVM-exception OR BSL-1.0) AND (Unlicense OR MIT)
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package    doc
Summary:    Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build

%install
install -Dm755 target/rpm/%{name}                                               %{buildroot}%{_bindir}/%{name}
install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.svg          %{buildroot}%{_scalableiconsdir}/io.github.sinelaw.fresh.svg
install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.desktop      %{buildroot}%{_appsdir}/io.github.sinelaw.fresh.desktop
install -Dm644 crates/fresh-editor/flatpak/io.github.sinelaw.fresh.metainfo.xml %{buildroot}%{_metainfodir}/io.github.sinelaw.fresh.metainfo.xml
%{cargo_license_online} > LICENSE.dependencies
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a docs/*                                                                    %{buildroot}%{_pkgdocdir}/

%files
%license LICENSE LICENSE.dependencies
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_scalableiconsdir}/io.github.sinelaw.fresh.svg
%{_appsdir}/io.github.sinelaw.fresh.desktop
%{_metainfodir}/io.github.sinelaw.fresh.metainfo.xml

%files doc
%{_pkgdocdir}/
%license LICENSE

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com> - 0.1.65-1
- Initial commit
