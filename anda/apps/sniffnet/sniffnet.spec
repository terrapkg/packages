Name:           sniffnet
Version:        1.5.1
Release:        2%{?dist}
Summary:        Comfortably monitor your Internet traffic
URL:            https://github.com/GyulyVGC/sniffnet
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT AND Apache-2.0
License:        MIT AND Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND NCSA AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND (MIT AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later)) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR X11 OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpcap)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/sniffnet                        %{buildroot}%{_bindir}/sniffnet
install -Dm644 resources/logos/raw/icon.png               %{buildroot}%{_hicolordir}/1024x1024/apps/sniffnet.png
install -Dm644 resources/logos/raw/icon.svg               %{buildroot}%{_scalableiconsdir}/sniffnet.svg
install -Dm644 resources/packaging/linux/sniffnet.desktop %{buildroot}%{_appsdir}/sniffnet.desktop

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%license LICENSE.dependencies
%{_bindir}/sniffnet
%{_hicolordir}/1024x1024/apps/sniffnet.png
%{_scalableiconsdir}/sniffnet.svg
%{_appsdir}/sniffnet.desktop

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com> - 1.5.1-1
- Initial commit
