%global _description %{expand:
An editor that pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.}
%global crate edit
%bcond rust_nightly 0
%global appid com.microsoft.edit
%global org com.microsoft
%global appstream_component console-application

Name:          %{crate}
Version:       1.2.1
Release:       3%{?dist}
Summary:       A simple editor for simple needs.
SourceLicense: MIT
License:       MIT AND (MIT OR Apache-2.0)
URL:           https://github.com/microsoft/edit
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:       %{appid}.metainfo.xml
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
%if %{with rust_nightly}
BuildRequires: rustup
%endif
BuildRequires: mold
Packager:      Gilver E. <roachy@fyralabs.com>

%description %_description

%prep
%autosetup -n %{name}-%{version}
%if %{with rust_nightly}
%rustup_nightly
%endif
%cargo_prep_online

%build
%cargo_build

%install
%crate_install_bin
%{cargo_license_online} > LICENSE.dependencies
install -Dm644 assets/edit.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{appid}.svg

sed -i "s|^Icon=edit$|Icon=%{appid}|g" assets/%{appid}.desktop
install -Dm644 assets/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
%terra_appstream -o %{SOURCE1}

%files
%doc CODE_OF_CONDUCT.md
%doc README.md
%doc SECURITY.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{name}
%{_metainfodir}/%{appid}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/applications/%{appid}.desktop

%changelog
* Thu May 22 2025 Gilver E. <rockgrub@disroot.org> - 1.0.0-1
- Initial package

