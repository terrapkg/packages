%global ver 0.1.0
%global commitdate 20260224
%global commit fc6e8c80568011dc05eb4f4f1dab626772f69c73
%global shortcommit %{sub %{commit} 0 7}
%global appid org.codeberg.wfx.Noctua

Name:           noctua
Version:        %{ver}^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        An image viewer application for the COSMIC™ desktop

SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND NCSA) AND Unlicense AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND GPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

URL:            https://github.com/cosmic-utils/noctua
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  poppler-glib-devel
BuildRequires:  desktop-file-utils

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/noctua                                                   %{buildroot}%{_bindir}/noctua
%desktop_file_install resources/org.codeberg.wfx.Noctua.desktop
install -Dm0644 resources/org.codeberg.wfx.Noctua.metainfo.xml                      %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 resources/icons/hicolor/scalable/apps/org.codeberg.wfx.Noctua.svg   %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%terra_appstream

%files
%license LICENSE LICENSE.dependencies
%doc README.md docs/*
%{_bindir}/noctua
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
