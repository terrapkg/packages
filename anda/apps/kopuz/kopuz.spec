Name:           kopuz
Version:        0.16.1
Release:        1%{?dist}
Summary:        Modern, lightweight, music player application
# TODO - Next release is EUPL-1.2
SourceLicense:  MIT
License:        MIT
URL:            https://github.com/Kopuz-org/kopuz
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros

%description
Kopuz is a modern, lightweight, music player application
built with Rust and the Dioxus framework. It provides a
clean and responsive interface for managing and
enjoying your local music collection.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/kopuz                     %{buildroot}%{_bindir}/kopuz
install -Dm644 data/moe.kopuz.kopuz.desktop         %{buildroot}%{_appsdir}/moe.kopuz.kopuz.desktop
install -Dm644 data/moe.kopuz.kopuz.metainfo.xml    %{buildroot}%{_metainfodir}/moe.kopuz.kopuz.metainfo.xml
install -Dm644 packaging/systemd/kopuz-web.service  %{buildroot}%{_unitdir}/kopuz-web.service
install -Dm644 crates/kopuz/assets/logo.png         %{buildroot}%{_hicolordir}/256x256/apps/moe.kopuz.kopuz.png

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post kopuz-web.service

%preun
%systemd_preun kopuz-web.service

%postun
%systemd_postun_with_restart kopuz-web.service

%files
%doc README.md CONTRIBUTING.md docs/matugen-pywal.md
%lang(pt_PT) %doc docs/README-PT-PT.md
%lang(ml) %doc docs/README-ML.md
%lang(tr) %doc docs/README-TR.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/kopuz
%{_appsdir}/moe.kopuz.kopuz.desktop
%{_metainfodir}/moe.kopuz.kopuz.metainfo.xml
%{_unitdir}/kopuz-web.service
%{_hicolordir}/256x256/apps/moe.kopuz.kopuz.png

%changelog
* Thu Aug 27 2026 Owen Zimmerman <owen@fyralabs.com> - 0.16.1-1
- Initial commit
