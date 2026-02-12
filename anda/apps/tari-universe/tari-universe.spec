%undefine __brp_mangle_shebangs

%global toolchain clang

Name:           tari-universe

Version:        1.6.10
Release:        1%{?dist}
Summary:        Desktop Mining Application for Tari
Packager:        Yoong Jin <solomoncyj@gmail.com>

SourceLicense: CPAL-1.0
License:        CPAL-1.0 AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Apache-2.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD) AND (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR CC0-1.0) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-1-Clause OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR LGPL-2.1-or-later OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 WITH LLVM-exception) AND BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT) AND BSL-1.0 AND CC0-1.0 AND (CDLA-Permissive-2.0) AND ISC AND MIT AND (MIT AND BSD-3-Clause) AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND WTFPL AND Zlib)
URL:           https://www.tari.com/
Source0:        https://github.com/tari-project/universe/archive/refs/tags/v%{version}.tar.gz
Source1: tari-universe.desktop


Requires:       hicolor-icon-theme

# Build requires
BuildRequires:  pnpm
BuildRequires: %{tauri_buildrequires}
BuildRequires:       desktop-file-utils
BuildRequires:       hicolor-icon-theme
BuildRequires: protobuf-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:       perl
BuildRequires:       zlib-ng-devel
BuildRequires:       clang
BuildRequires:       mold
BuildRequires:       ninja
BuildRequires:       cmake



%description
Tari Universe is a desktop application that allows users to mine Tari tokens (XTM) using their Mac or PC.
The application features a user-friendly interface with one-click mining setup.

%prep
%autosetup -n universe-%{version}
%tauri_prep

%build
%pnpm_build


%install
%tauri_install_bin
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%desktop_file_install -f  %{S:1}

install -Dm644   public/tari.svg %{buildroot}%{_hicolordir}/scalable/apps/



%files
%license LICENSE.dependencies
%license LICENSE
%doc README.md

%{_bindir}/twintaillauncher
%{_hicolordir}/scalable/apps/tari.svg
%_appsdir/tari-universe.desktop




%changelog
* Wed Feb 11 2026 Yoong Jin <solomoncyj@gmail.com> - 1.6.10-0
- Initial Package
