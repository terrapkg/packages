%undefine __brp_mangle_shebangs

%global _build_id_links none

%global toolchain clang

Name:           twintaillauncher

Version:        1.1.15
Release:        1%{?dist}
Summary:        A multi-platform launcher for your anime games
Packager:        Yoong Jin <solomoncyj@gmail.com>

SourceLicense: GPL-3.0-or-later
License:        GPL-3.0-or-later AND (((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR CC0-1.0) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR LGPL-2.1-or-later OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 WITH LLVM-exception) AND (BSD-2-Clause) AND (BSD-3-Clause) AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT) AND CC0-1.0 AND (CC0-1.0 OR MIT-0) AND (CDLA-Permissive-2.0) AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND (LGPL-3.0-or-later OR MIT) AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND  Unicode-3.0 AND Zlib AND bzip2-1.0.6)
URL:            https://twintaillauncher.app/
Source0:        https://github.com/TwintailTeam/TwintailLauncher/archive/refs/tags/ttl-v%{version}.tar.gz

ExclusiveArch: x86_64

Requires:       hicolor-icon-theme

# Build requires
BuildRequires:  pnpm
BuildRequires: %{tauri_buildrequires}
BuildRequires: protobuf-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:       desktop-file-utils
BuildRequires:       hicolor-icon-theme
BuildRequires:       perl
BuildRequires:       zlib-ng-devel
BuildRequires:       clang
BuildRequires:       mold

Provides: ttl

%description
Twintaillauncher is a multi-platform launcher that brings mod support, quality-of-life improvements, and advanced features to a variety of anime-styled games.
TTL is an all-in-one tool for downloading, managing, and launching your favorite anime games. It’s designed with flexibility, ease of use, and customization in mind.

%prep
%autosetup -n TwintailLauncher-ttl-v%{version}
cd src-tauri
cargo update
cd ..
%tauri_prep

%build
%pnpm_build


%install
%tauri_install
mkdir -p %{buildroot}/%{_libdir}/twintaillauncher/resources
mv %{buildroot}/%{_datadir}/cargo/registry/twintaillauncher-%{version}/resources/ %{buildroot}/%{_libdir}/twintaillauncher/resources
rm -rf %{buildroot}/%{_datadir}/cargo/registry/twintaillauncher-%{version}


%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%desktop_file_install -f  ./twintaillauncher.desktop

install -Dm644   public/launcher-icon.png %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png
install -Dm644 public/launcher-icon-128.png %{buildroot}%{_hicolordir}/128x128/apps/%{name}.png



%files
%license LICENSE.dependencies
%license LICENSE
%doc README.md

%{_bindir}/twintaillauncher
%{_libdir}/twintaillauncher/resources
%{_hicolordir}/512x512/apps/%{name}.png
%{_hicolordir}/128x128/apps/%{name}.png
%_appsdir/twintaillauncher.desktop




%changelog
* Thu Feb 19 2026 Yoong Jin <solomoncyj@gmail.com> - 1.1.15-1
- Fix resources
* Tue Feb 3 2026 Yoong Jin <solomoncyj@gmail.com> - 1.1.15-0
- Initial Package
