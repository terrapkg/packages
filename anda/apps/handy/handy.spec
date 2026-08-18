Name:           handy
Version:        0.9.5
Release:        1%?dist
Summary:        A free, open source, and extensible speech-to-text application that works completely offline
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR BSD-3-Clause) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  MIT
URL:            https://handy.computer
Source0:        https://github.com/cjpais/Handy/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyrlabs.com>
BuildRequires:  bun-bin %tauri_buildrequires
BuildRequires:  cmake(SPIRV-Headers)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(alsa)

%description
Handy is a cross-platform desktop application that provides simple, privacy-focused speech transcription. Press a shortcut, speak, and have your words appear in any text field. This happens on your own computer without sending any information to the cloud.

%prep
%autosetup -n Handy-%version
%tauri_prep

%build
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies
%bun_build

%install
%tauri_install

%files
%doc README.md
%license LICENSE
%_bindir/handy
%_appdir/%name.desktop

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 0.9.5-1
- Initial package
