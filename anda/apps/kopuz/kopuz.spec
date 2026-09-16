%undefine __brp_mangle_shebangs

# rustix 0.37.x enables the obsolete rustc_attrs cfg when RUSTC_BOOTSTRAP=1.
# The cargo macros set that variable for -Z avoid-dev-deps, which is not
# needed here and is incompatible with the system compiler.
%global __cargo_common_opts %{?_smp_mflags}

Name:           kopuz
Version:        0.16.2
Release:        1%{?dist}
Summary:        Modern, lightweight, music player application
SourceLicense:  EUPL-1.2
License:        %{sourcelicense} AND MIT AND (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND NCSA) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND LGPL-3.0-or-later AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND MIT AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/Kopuz-org/kopuz
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  libxdo-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(alsa)

%description
Kopuz is a modern, lightweight, music player application
built with Rust and the Dioxus framework. It provides a
clean and responsive interface for managing and
enjoying your local music collection.

%prep
%autosetup -C
%cargo_prep_online

%build
%global __cargo /usr/bin/env AWS_LC_SYS_CMAKE_BUILDER=1 CARGO_HOME=.cargo RUSTFLAGS='%{build_rustflags}' /usr/bin/cargo
%cargo_build

%install
install -Dm755 target/rpm/kopuz                     %{buildroot}%{_bindir}/kopuz
install -Dm644 data/moe.kopuz.kopuz.desktop         %{buildroot}%{_appsdir}/moe.kopuz.kopuz.desktop
install -Dm644 data/moe.kopuz.kopuz.metainfo.xml    %{buildroot}%{_metainfodir}/moe.kopuz.kopuz.metainfo.xml
install -Dm644 packaging/systemd/kopuz-web.service  %{buildroot}%{_unitdir}/kopuz-web.service
install -Dm644 crates/kopuz/assets/logo.png         %{buildroot}%{_hicolordir}/256x256/apps/moe.kopuz.kopuz.png

# cargo_license_online still uses -Z avoid-dev-deps, so restore bootstrap for
# this cargo tree-only operation after the build has completed.
%global __cargo /usr/bin/env AWS_LC_SYS_CMAKE_BUILDER=1 CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' /usr/bin/cargo
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
