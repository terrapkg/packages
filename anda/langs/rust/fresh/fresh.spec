%undefine __brp_mangle_shebangs

Name:           fresh
Version:        0.2.5
Release:        1%?dist
Summary:        Text editor for your terminal: easy, powerful and fast
URL:            https://getfresh.dev
Source0:        https://github.com/sinelaw/fresh/archive/refs/tags/v%version.tar.gz
License:        GPL-2.0-only
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold
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
