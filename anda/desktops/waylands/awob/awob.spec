Name:           awob
Version:        0.1.8
Release:        1%{?dist}
Summary:        Another Wayland Overlay Bar
Patch0:         0001-fix-service-binary-exec.patch
SourceLicense:  MIT
License:        %{sourcelicense} AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND CC0-1.0 AND ISC AND BSD-3-Clause AND (Unlicense OR MIT)
URL:            https://jmylchreest.github.io/awob/
Source0:        https://github.com/jmylchreest/awob/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Another Wayland Overlay Bar — drop-in replacement for wob with
richer theming, typed IPC, and an event-source listener ecosystem.

%prep
%autosetup -C -p1
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build

%install
for bin in awob awob-daemon \
           awob-listener-pipewire \
           awob-listener-battery \
           awob-listener-backlight \
           awob-listener-keyboard-backlight \
           awob-listener-power-profile \
           awob-listener-wob; do
    install -Dm755 "target/rpm/${bin}" "%{buildroot}%{_bindir}/${bin}"
done
install -dm755 %{buildroot}%{_datadir}/awob
cp -r themes %{buildroot}%{_datadir}/awob/
install -Dm644 contrib/systemd/awob.service     %{buildroot}%{_userunitdir}/awob.service

%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md docs/docs/*
%license LICENSE LICENSE.dependencies
%{_bindir}/awob
%{_bindir}/awob-daemon
%{_bindir}/awob-listener-pipewire
%{_bindir}/awob-listener-battery
%{_bindir}/awob-listener-backlight
%{_bindir}/awob-listener-keyboard-backlight
%{_bindir}/awob-listener-power-profile
%{_bindir}/awob-listener-wob
%{_datadir}/awob/
%{_userunitdir}/awob.service

%changelog
* Tue Sep 15 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.8-1
- Initial commit
