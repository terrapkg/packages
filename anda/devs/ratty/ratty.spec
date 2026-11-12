%global crate   ratty

Name:           %{crate}
Version:        0.6.0
Release:        2%{?dist}
Summary:        A GPU-rendered terminal emulator with inline 3D graphics
SourceLicense:  MIT
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Zlib AND (MIT OR Apache-2.0)) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT-0 AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://ratty-term.org/
Source0:        %{crates_source}
Source1:        %{crate}.desktop
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  wayland-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%install -a
%desktop_file_install %{S:1}
magick assets/ratty.ico[0] ratty.png
install -Dm644 ratty.png %{buildroot}%{_hicolordir}/256x256/apps/ratty.png

%check -a
%desktop_file_validate %{buildroot}%{_appsdir}/%{crate}.desktop

%files
%doc README.md protocols/graphics.md SECURITY.md CHANGELOG.md config/ratty.toml
%license LICENSE LICENSE.dependencies
%{_bindir}/%{crate}
%{_bindir}/%{crate}-mcp
%{_appsdir}/%{crate}.desktop
%{_hicolordir}/256x256/apps/ratty.png

%changelog
* Wed Oct 28 2026 Owen Zimmerman <owen@fyralabs.com> - 0.6.0-1
- Initial commit
