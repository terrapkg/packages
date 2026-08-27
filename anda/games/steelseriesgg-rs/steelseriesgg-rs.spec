Name:           steelseriesgg-rs
Version:        0.1.5
Release:        1%{?dist}
Summary:        Open-source SteelSeries GG replacement for Linux
URL:            https://github.com/Ven0m0/steelseriesgg-rs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        (Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND MIT AND BSD-3-Clause AND (Unlicense OR MIT)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Open-source SteelSeries GG replacement for Linux. Control
SteelSeries keyboards and headsets: RGB lighting,
GameSense-compatible server, profiles, and
(optional) audio/Sonar integration.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/ssgg              %{buildroot}%{_bindir}/ssgg
install -Dm644 assets/ssgg.service          %{buildroot}%{_unitdir}/ssgg.service
install -Dm644 assets/99-steelseries.rules  %{buildroot}%{_udevrulesdir}/99-steelseries.rules

%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post ssgg.service

%preun
%systemd_preun ssgg.service

%postun
%systemd_postun_with_restart ssgg.service

%files
%doc README.md CHANGELOG.md PLAN.md TODO.md docs/development/*
%license LICENSE
%{_bindir}/ssgg
%{_unitdir}/ssgg.service
%{_udevrulesdir}/99-steelseries.rules

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
