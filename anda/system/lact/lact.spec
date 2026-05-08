%define appid io.github.ilya_zlobintsev.LACT

Name:           lact
Version:        0.9.0
Release:        1%{?dist}
Summary:        Linux GPU Configuration And Monitoring Tool
URL:            https://github.com/ilya-zlobintsev/LACT
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        MIT AND Zlib AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND LGPL-3.0-or-later AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR ISC OR MIT) AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only)
BuildRequires:  cargo-rpm-macros
BuildRequires:	systemd-rpm-macros
BuildRequires:	clang-devel
BuildRequires:	libadwaita-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(graphene-gobject-1.0)
BuildRequires:	pkgconfig(hwdata)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)

Provides:       LACT

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n LACT-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/lact %{buildroot}%{_bindir}/lact
install -Dm644 res/lactd.service %{buildroot}%{_unitdir}/lactd.service
install -Dm644 res/%{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 res/%{appid}.png %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png
install -Dm644 res/%{appid}.svg %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 res/%{appid}.metainfo.xml %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post lactd.service

%preun
%systemd_preun lactd.service

%postun
%systemd_postun_with_restart lactd.service

%files
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/lact
%{_unitdir}/lactd.service
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/512x512/apps/%{appid}.png
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu May 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
