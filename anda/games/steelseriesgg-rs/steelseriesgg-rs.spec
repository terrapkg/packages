Name:           steelseriesgg-rs
Version:        0.1.13
Release:        1%{?dist}
Summary:        Open-source SteelSeries GG replacement for Linux
URL:            https://github.com/Ven0m0/steelseriesgg-rs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        (Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND MIT AND BSD-3-Clause AND (Unlicense OR MIT)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros

# GUI
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Open-source SteelSeries GG replacement for Linux. Control
SteelSeries keyboards and headsets: RGB lighting,
GameSense-compatible server, profiles, and
(optional) audio/Sonar integration.

%package        gui
Summary:        GUI for steelseriesgg-rs
Requires:       %{name} = %{evr}

%description    gui
GUI for steelseriesgg-rs.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build -- --features desktop --bin ssgg --bin ssgg-gui

%install
install -Dm755 target/rpm/ssgg              %{buildroot}%{_bindir}/ssgg
install -Dm755 target/rpm/ssgg-gui          %{buildroot}%{_bindir}/ssgg-gui
install -Dm644 assets/ssgg.service          %{buildroot}%{_unitdir}/ssgg.service
install -Dm644 assets/70-steelseries.rules  %{buildroot}%{_udevrulesdir}/70-steelseries.rules

%desktop_file_install assets/ssgg-gui.desktop

%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post ssgg.service

%preun
%systemd_preun ssgg.service

%postun
%systemd_postun_with_restart ssgg.service

%files
%doc README.md CHANGELOG.md PLAN.md docs/development/*
%license LICENSE
%{_bindir}/ssgg
%{_unitdir}/ssgg.service
%{_udevrulesdir}/70-steelseries.rules

%files gui
%{_bindir}/ssgg-gui
%{_appsdir}/ssgg-gui.desktop

%changelog
* Sun Oct 25 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.10-1
- Add GUI subpackage

* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
