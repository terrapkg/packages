%global appid dev.khcrysalis.PlumeImpactor
%undefine __brp_mangle_shebangs

Name:           plumeimpactor
Version:        2.6.5
Release:        1%{?dist}
Summary:        Cross-platform & feature rich iOS/iPadOS/tvOS sideloading application
URL:            https://github.com/claration/Impactor
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT AND MPL-2.0 AND Apache-2.0 AND 
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND bzip2-1.0.6 AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (Apache-2.0 OR GPL-2.0-only) AND BlueOak-1.0.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND (CC0-1.0 OR MIT-0) AND BSL-1.0 AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
%dnl install -Dm755 target/rpm/plumesign 					%{buildroot}%{_bindir}/plumesign
install -Dm755 target/rpm/plumeimpactor 				%{buildroot}%{_bindir}/plumeimpactor
install -Dm644 package/linux/%{appid}.desktop 				%{buildroot}%{_appsdir}/%{appid}.desktop
for size in 16 32 48 64 128 256 512; do
	install -Dm644 package/linux/icons/hicolor/${size}x${size}/apps/%{appid}.png %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%{_bindir}/plumeimpactor
%{_hicolordir}/*x*/apps/%{appid}.png
%{_appsdir}/%{appid}.desktop

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
